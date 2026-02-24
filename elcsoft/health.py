from __future__ import annotations

from typing import Any, Dict, Optional

from elcsoft.core.client import SwaggerClient

# Auto-generated from http://localhost:3001/api-docs.json
# Router: health

def get_health(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /health"""
    return client.call(
        method="GET",
        path="/health",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )
