from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional, Tuple

import requests


class SwaggerSpecError(Exception):
    pass


@dataclass
class OperationInfo:
    path: str
    method: str


class SwaggerClient:
    def __init__(
        self,
        spec_url: str,
        base_url: Optional[str] = None,
        timeout: int = 30,
        default_headers: Optional[Dict[str, str]] = None,
        bearer_token: Optional[str] = None,
    ) -> None:
        self.spec_url = spec_url
        self.timeout = timeout
        self.session = requests.Session()
        self.default_headers = default_headers or {}

        if bearer_token:
            self.default_headers["Authorization"] = f"Bearer {bearer_token}"

        self.spec = self._load_spec()
        self.base_url = base_url or self._extract_base_url()
        self.operation_index = self._build_operation_index()

    def _load_spec(self) -> Dict[str, Any]:
        response = self.session.get(self.spec_url, timeout=self.timeout)
        response.raise_for_status()

        try:
            data = response.json()
        except ValueError as exc:
            raise SwaggerSpecError("Swagger JSON 파싱에 실패했습니다.") from exc

        if not isinstance(data, dict) or "paths" not in data:
            raise SwaggerSpecError("유효한 OpenAPI/Swagger 문서가 아닙니다. (paths 누락)")

        return data

    def _extract_base_url(self) -> str:
        servers = self.spec.get("servers")
        if isinstance(servers, list) and servers:
            url = servers[0].get("url")
            if isinstance(url, str) and url:
                return url.rstrip("/")

        host = self.spec.get("host")
        base_path = self.spec.get("basePath", "")
        schemes = self.spec.get("schemes")
        if host:
            scheme = "https"
            if isinstance(schemes, list) and schemes:
                scheme = schemes[0]
            return f"{scheme}://{host}{base_path}".rstrip("/")

        raise SwaggerSpecError(
            "base_url을 자동 추론할 수 없습니다. SwaggerClient 생성 시 base_url을 지정하세요."
        )

    def _build_operation_index(self) -> Dict[str, OperationInfo]:
        result: Dict[str, OperationInfo] = {}
        paths = self.spec.get("paths", {})

        for path, methods in paths.items():
            if not isinstance(methods, dict):
                continue

            for method, detail in methods.items():
                if method.lower() not in {
                    "get",
                    "post",
                    "put",
                    "patch",
                    "delete",
                    "head",
                    "options",
                }:
                    continue

                if not isinstance(detail, dict):
                    continue

                operation_id = detail.get("operationId")
                if operation_id and isinstance(operation_id, str):
                    result[operation_id] = OperationInfo(path=path, method=method.upper())

        return result

    def _resolve_path(
        self,
        raw_path: str,
        path_params: Optional[Dict[str, Any]],
    ) -> str:
        resolved = raw_path
        for key, value in (path_params or {}).items():
            resolved = resolved.replace("{" + key + "}", str(value))
        return resolved

    def _build_headers(self, headers: Optional[Dict[str, str]]) -> Dict[str, str]:
        merged = dict(self.default_headers)
        if headers:
            merged.update(headers)
        return merged

    def call(
        self,
        method: str,
        path: str,
        *,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_body: Optional[Any] = None,
        data: Optional[Any] = None,
        timeout: Optional[int] = None,
    ) -> Any:
        method_upper = method.upper()
        resolved_path = self._resolve_path(path, path_params)
        url = f"{self.base_url.rstrip('/')}/{resolved_path.lstrip('/')}"

        response = self.session.request(
            method=method_upper,
            url=url,
            params=query_params,
            headers=self._build_headers(headers),
            json=json_body,
            data=data,
            timeout=timeout or self.timeout,
        )
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            return response.json()

        return response.text

    def call_operation(
        self,
        operation_id: str,
        *,
        path_params: Optional[Dict[str, Any]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        json_body: Optional[Any] = None,
        data: Optional[Any] = None,
        timeout: Optional[int] = None,
    ) -> Any:
        info = self.operation_index.get(operation_id)
        if info is None:
            raise SwaggerSpecError(f"operationId '{operation_id}'를 찾을 수 없습니다.")

        return self.call(
            method=info.method,
            path=info.path,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            json_body=json_body,
            data=data,
            timeout=timeout,
        )

    def list_operations(self) -> Dict[str, Tuple[str, str]]:
        return {
            operation_id: (info.method, info.path)
            for operation_id, info in self.operation_index.items()
        }
