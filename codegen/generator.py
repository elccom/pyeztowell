from __future__ import annotations

import argparse
import json
import keyword
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse
from typing import Any, Dict, List, Optional, Set, Tuple

import requests

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


@dataclass
class OperationMeta:
    router: str
    function_name: str
    method: str
    path: str
    operation_id: Optional[str]


def _to_snake_case(value: str) -> str:
    value = re.sub(r"[^0-9a-zA-Z_]+", "_", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    value = value.lower().strip("_")
    if not value:
        value = "operation"
    if value[0].isdigit():
        value = f"op_{value}"
    if keyword.iskeyword(value):
        value = f"{value}_op"
    return value


def _default_method_name(method: str, path: str) -> str:
    normalized_path = path.strip("/").replace("/", "_").replace("{", "").replace("}", "")
    if not normalized_path:
        normalized_path = "root"
    return _to_snake_case(f"{method}_{normalized_path}")


def _infer_router_name(path: str, detail: Dict[str, Any]) -> str:
    tags = detail.get("tags")
    if isinstance(tags, list) and tags:
        first_tag = tags[0]
        if isinstance(first_tag, str) and first_tag.strip():
            return _to_snake_case(first_tag)

    segments = [segment for segment in path.split("/") if segment and not segment.startswith("{")]
    if segments:
        return _to_snake_case(segments[0])

    return "default"


def _fetch_spec(spec_url: str, timeout: int) -> Dict[str, Any]:
    candidates: List[str] = [spec_url]

    parsed = urlparse(spec_url)
    base = f"{parsed.scheme}://{parsed.netloc}"
    path = parsed.path.rstrip("/")

    if path.endswith("/manual.json"):
        candidates.append(f"{base}{path[:-5]}")
        candidates.append(f"{base}{path[:-5]}/swagger-ui-init.js")
        candidates.append(f"{base}/api-docs.json")
    elif path.endswith("/manual"):
        candidates.append(f"{base}{path}.json")
        candidates.append(f"{base}{path}/swagger-ui-init.js")
        candidates.append(f"{base}/api-docs.json")
    elif path.endswith("/api-docs.json"):
        candidates.append(f"{base}/manual")
        candidates.append(f"{base}/manual/swagger-ui-init.js")
    else:
        candidates.append(f"{base}/api-docs.json")
        candidates.append(f"{base}/manual.json")
        candidates.append(f"{base}/manual")
        candidates.append(f"{base}/manual/swagger-ui-init.js")

    candidates.extend(
        [
            f"{base}/swagger.json",
            f"{base}/openapi.json",
            f"{base}/v3/api-docs",
        ]
    )

    unique_candidates = []
    seen: Set[str] = set()
    for candidate in candidates:
        if candidate not in seen:
            seen.add(candidate)
            unique_candidates.append(candidate)

    last_error: Optional[Exception] = None
    for candidate in unique_candidates:
        try:
            response = requests.get(candidate, timeout=timeout)
            response.raise_for_status()
            try:
                data = response.json()
                if isinstance(data, dict) and "paths" in data:
                    return data
            except ValueError:
                pass

            embedded = _extract_swagger_doc_from_js(response.text)
            if isinstance(embedded, dict) and "paths" in embedded:
                return embedded
        except Exception as exc:
            last_error = exc
            continue

    raise ValueError(f"유효한 OpenAPI/Swagger JSON을 찾지 못했습니다. 시도 URL: {unique_candidates}") from last_error


def _extract_swagger_doc_from_js(content: str) -> Optional[Dict[str, Any]]:
    marker = '"swaggerDoc":'
    marker_idx = content.find(marker)
    if marker_idx < 0:
        return None

    brace_start = content.find("{", marker_idx)
    if brace_start < 0:
        return None

    depth = 0
    in_string = False
    escape = False
    end_idx = -1

    for idx in range(brace_start, len(content)):
        ch = content[idx]

        if in_string:
            if escape:
                escape = False
            elif ch == "\\":
                escape = True
            elif ch == '"':
                in_string = False
            continue

        if ch == '"':
            in_string = True
            continue

        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                end_idx = idx
                break

    if end_idx < 0:
        return None

    json_text = content[brace_start : end_idx + 1]
    try:
        parsed = json.loads(json_text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        return None

    return None


def _collect_operations(spec: Dict[str, Any]) -> List[OperationMeta]:
    operations: List[OperationMeta] = []
    used_names_per_router: Dict[str, Set[str]] = {}

    for path, path_item in spec.get("paths", {}).items():
        if not isinstance(path_item, dict):
            continue

        for method, detail in path_item.items():
            method_lower = str(method).lower()
            if method_lower not in HTTP_METHODS:
                continue

            operation_id = None
            if isinstance(detail, dict):
                operation_id = detail.get("operationId")

            router = _infer_router_name(str(path), detail if isinstance(detail, dict) else {})

            base_name = _to_snake_case(operation_id) if isinstance(operation_id, str) and operation_id else _default_method_name(method_lower, str(path))

            if router not in used_names_per_router:
                used_names_per_router[router] = set()

            name = base_name
            suffix = 2
            while name in used_names_per_router[router]:
                name = f"{base_name}_{suffix}"
                suffix += 1

            used_names_per_router[router].add(name)
            operations.append(
                OperationMeta(
                    router=router,
                    function_name=name,
                    method=method_lower.upper(),
                    path=str(path),
                    operation_id=operation_id if isinstance(operation_id, str) else None,
                )
            )

    operations.sort(key=lambda item: (item.router, item.function_name))
    return operations


def _group_by_router(operations: List[OperationMeta]) -> Dict[str, List[OperationMeta]]:
    grouped: Dict[str, List[OperationMeta]] = {}
    for operation in operations:
        grouped.setdefault(operation.router, []).append(operation)
    return grouped


def _render_router_module(router: str, operations: List[OperationMeta], source_spec_url: str) -> str:
    lines: List[str] = []
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any, Dict, Optional")
    lines.append("")
    lines.append("from elcsoft.core.client import SwaggerClient")
    lines.append("")
    lines.append(f"# Auto-generated from {source_spec_url}")
    lines.append(f"# Router: {router}")
    lines.append("")

    for operation in operations:
        lines.append(f"def {operation.function_name}(")
        lines.append("    client: SwaggerClient,")
        lines.append("    *,")
        lines.append("    path_params: Optional[Dict[str, Any]] = None,")
        lines.append("    query_params: Optional[Dict[str, Any]] = None,")
        lines.append("    headers: Optional[Dict[str, str]] = None,")
        lines.append("    json_body: Optional[Any] = None,")
        lines.append("    data: Optional[Any] = None,")
        lines.append("    timeout: Optional[int] = None,")
        lines.append(") -> Any:")
        lines.append(f"    \"\"\"{operation.method} {operation.path}\"\"\"")
        lines.append("    return client.call(")
        lines.append(f"        method=\"{operation.method}\",")
        lines.append(f"        path=\"{operation.path}\",")
        lines.append("        path_params=path_params,")
        lines.append("        query_params=query_params,")
        lines.append("        headers=headers,")
        lines.append("        json_body=json_body,")
        lines.append("        data=data,")
        lines.append("        timeout=timeout,")
        lines.append("    )")
        lines.append("")

    return "\n".join(lines)


def _render_router_init(router_names: List[str], source_spec_url: str) -> str:
    lines: List[str] = []
    lines.append(f"# Auto-generated from {source_spec_url}")
    lines.append("")
    for router in router_names:
        lines.append(f"from . import {router}")
    lines.append("")
    lines.append("__all__ = [")
    for router in router_names:
        lines.append(f"    \"{router}\",")
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def generate_router_files_from_swagger(
    spec_url: str,
    output_dir: str,
    timeout: int = 30,
) -> str:
    spec = _fetch_spec(spec_url=spec_url, timeout=timeout)
    operations = _collect_operations(spec)
    grouped = _group_by_router(operations)

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    router_names = sorted(grouped.keys())

    current_router_set = set(router_names)
    for existing_file in output_path.glob("*.py"):
        if existing_file.name in {"__init__.py", "client.py", "generator.py"}:
            continue
        if existing_file.stem in current_router_set:
            continue
        try:
            content = existing_file.read_text(encoding="utf-8")
        except Exception:
            continue
        if "# Auto-generated from " in content:
            existing_file.unlink(missing_ok=True)

    for router in router_names:
        code = _render_router_module(router=router, operations=grouped[router], source_spec_url=spec_url)
        (output_path / f"{router}.py").write_text(code, encoding="utf-8")

    init_file = output_path / "__init__.py"
    if not init_file.exists():
        init_code = _render_router_init(router_names=router_names, source_spec_url=spec_url)
        init_file.write_text(init_code, encoding="utf-8")

    return str(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Swagger/OpenAPI JSON으로 API 공통 라이브러리 코드를 생성합니다.")
    parser.add_argument("--spec-url", required=True, help="Swagger/OpenAPI JSON URL")
    parser.add_argument("--output-dir", default="elcsoft", help="라우터별 파일 생성 디렉터리 (예: elcsoft -> elcsoft/users.py)")
    parser.add_argument("--timeout", type=int, default=30, help="Swagger JSON 조회 타임아웃(초)")

    args = parser.parse_args()
    output_dir = generate_router_files_from_swagger(
        spec_url=args.spec_url,
        output_dir=args.output_dir,
        timeout=args.timeout,
    )
    print(f"Generated router files: {output_dir}")


if __name__ == "__main__":
    main()
