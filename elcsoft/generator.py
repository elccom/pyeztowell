from __future__ import annotations

import argparse
import keyword
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

import requests

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


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


def _fetch_spec(spec_url: str, timeout: int) -> Dict[str, Any]:
    response = requests.get(spec_url, timeout=timeout)
    response.raise_for_status()

    data = response.json()
    if not isinstance(data, dict) or "paths" not in data:
        raise ValueError("유효한 OpenAPI/Swagger JSON이 아닙니다. (paths 누락)")
    return data


def _collect_operations(spec: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    operations: List[Tuple[str, str, str]] = []
    used_names: Set[str] = set()

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

            base_name = _to_snake_case(operation_id) if isinstance(operation_id, str) and operation_id else _default_method_name(method_lower, str(path))

            name = base_name
            suffix = 2
            while name in used_names:
                name = f"{base_name}_{suffix}"
                suffix += 1

            used_names.add(name)
            operations.append((name, method_lower.upper(), str(path)))

    operations.sort(key=lambda item: item[0])
    return operations


def _render_client_code(class_name: str, operations: List[Tuple[str, str, str]], source_spec_url: str) -> str:
    lines: List[str] = []
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any, Dict, Optional")
    lines.append("")
    lines.append("from elcsoft.client import SwaggerClient")
    lines.append("")
    lines.append("")
    lines.append(f"class {class_name}(SwaggerClient):")
    lines.append(f"    \"\"\"자동 생성된 API 클라이언트. source: {source_spec_url}\"\"\"")
    lines.append("")

    if not operations:
        lines.append("    pass")
        lines.append("")
        return "\n".join(lines)

    for method_name, http_method, path in operations:
        lines.append(f"    def {method_name}(")
        lines.append("        self,")
        lines.append("        *,")
        lines.append("        path_params: Optional[Dict[str, Any]] = None,")
        lines.append("        query_params: Optional[Dict[str, Any]] = None,")
        lines.append("        headers: Optional[Dict[str, str]] = None,")
        lines.append("        json_body: Optional[Any] = None,")
        lines.append("        data: Optional[Any] = None,")
        lines.append("        timeout: Optional[int] = None,")
        lines.append("    ) -> Any:")
        lines.append(f"        \"\"\"{http_method} {path}\"\"\"")
        lines.append("        return self.call(")
        lines.append(f"            method=\"{http_method}\",")
        lines.append(f"            path=\"{path}\",")
        lines.append("            path_params=path_params,")
        lines.append("            query_params=query_params,")
        lines.append("            headers=headers,")
        lines.append("            json_body=json_body,")
        lines.append("            data=data,")
        lines.append("            timeout=timeout,")
        lines.append("        )")
        lines.append("")

    return "\n".join(lines)


def generate_client_from_swagger(
    spec_url: str,
    output_file: str,
    class_name: str = "ManualApiClient",
    timeout: int = 30,
) -> str:
    spec = _fetch_spec(spec_url=spec_url, timeout=timeout)
    operations = _collect_operations(spec)
    code = _render_client_code(class_name=class_name, operations=operations, source_spec_url=spec_url)

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(code, encoding="utf-8")

    return str(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Swagger/OpenAPI JSON으로 API 공통 라이브러리 코드를 생성합니다.")
    parser.add_argument("--spec-url", required=True, help="Swagger/OpenAPI JSON URL")
    parser.add_argument("--output", required=True, help="생성할 Python 파일 경로")
    parser.add_argument("--class-name", default="ManualApiClient", help="생성할 클라이언트 클래스 이름")
    parser.add_argument("--timeout", type=int, default=30, help="Swagger JSON 조회 타임아웃(초)")

    args = parser.parse_args()
    output_path = generate_client_from_swagger(
        spec_url=args.spec_url,
        output_file=args.output,
        class_name=args.class_name,
        timeout=args.timeout,
    )
    print(f"Generated: {output_path}")


if __name__ == "__main__":
    main()
