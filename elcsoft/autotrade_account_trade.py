from __future__ import annotations

from typing import Any, Dict, Optional

from elcsoft.core.client import SwaggerClient

# Auto-generated from http://localhost:3001/api-docs.json
# Router: autotrade_account_trade

def delete_autotrade_account_trade_autotrade_account_trade_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """DELETE /autotrade_account_trade/{autotrade_account_trade_id}"""
    return client.call(
        method="DELETE",
        path="/autotrade_account_trade/{autotrade_account_trade_id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_trade_autotrade_account_trade_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account_trade/{autotrade_account_trade_id}"""
    return client.call(
        method="GET",
        path="/autotrade_account_trade/{autotrade_account_trade_id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def patch_autotrade_account_trade_autotrade_account_trade_id_amend_direct(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """PATCH /autotrade_account_trade/{autotrade_account_trade_id}/amend_direct"""
    return client.call(
        method="PATCH",
        path="/autotrade_account_trade/{autotrade_account_trade_id}/amend_direct",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_trade_autotrade_account_trade_id_cancel(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account_trade/{autotrade_account_trade_id}/cancel"""
    return client.call(
        method="POST",
        path="/autotrade_account_trade/{autotrade_account_trade_id}/cancel",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_trade_autotrade_account_trade_id_check(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account_trade/{autotrade_account_trade_id}/check"""
    return client.call(
        method="POST",
        path="/autotrade_account_trade/{autotrade_account_trade_id}/check",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_trade_check_all(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account_trade/check-all"""
    return client.call(
        method="POST",
        path="/autotrade_account_trade/check-all",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def put_autotrade_account_trade_autotrade_account_trade_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """PUT /autotrade_account_trade/{autotrade_account_trade_id}"""
    return client.call(
        method="PUT",
        path="/autotrade_account_trade/{autotrade_account_trade_id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )
