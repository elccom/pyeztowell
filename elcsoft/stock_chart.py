from __future__ import annotations

from typing import Any, Dict, Optional

from elcsoft.core.client import SwaggerClient

# Auto-generated from http://localhost:3001/api-docs.json
# Router: stock_chart

def get_stock_chart_chart_type_symbol(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock_chart/{chartType}/{symbol}"""
    return client.call(
        method="GET",
        path="/stock_chart/{chartType}/{symbol}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_chart_chart_type_symbol_date(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock_chart/{chartType}/{symbol}/{date}"""
    return client.call(
        method="GET",
        path="/stock_chart/{chartType}/{symbol}/{date}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )
