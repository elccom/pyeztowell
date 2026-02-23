from __future__ import annotations

from typing import Any, Dict, Optional

from elcsoft.core.client import SwaggerClient

# Auto-generated from http://localhost:3001/api-docs.json
# Router: autotrade_account

def delete_autotrade_account_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """DELETE /autotrade_account/{id}"""
    return client.call(
        method="DELETE",
        path="/autotrade_account/{id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account"""
    return client.call(
        method="GET",
        path="/autotrade_account",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_2(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/"""
    return client.call(
        method="GET",
        path="/autotrade_account/",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_autotrade_account_id_owns(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/{autotrade_account_id}/owns"""
    return client.call(
        method="GET",
        path="/autotrade_account/{autotrade_account_id}/owns",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_autotrade_account_id_profits(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/{autotrade_account_id}/profits"""
    return client.call(
        method="GET",
        path="/autotrade_account/{autotrade_account_id}/profits",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_autotrade_account_id_trades(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/{autotrade_account_id}/trades"""
    return client.call(
        method="GET",
        path="/autotrade_account/{autotrade_account_id}/trades",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/{id}"""
    return client.call(
        method="GET",
        path="/autotrade_account/{id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_id_auth_status(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/{id}/auth-status"""
    return client.call(
        method="GET",
        path="/autotrade_account/{id}/auth-status",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_stats_summary(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/stats/summary"""
    return client.call(
        method="GET",
        path="/autotrade_account/stats/summary",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_autotrade_account_user_user_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /autotrade_account/user/{userId}"""
    return client.call(
        method="GET",
        path="/autotrade_account/user/{userId}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account"""
    return client.call(
        method="POST",
        path="/autotrade_account",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_2(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/"""
    return client.call(
        method="POST",
        path="/autotrade_account/",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_id_authenticate(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/{id}/authenticate"""
    return client.call(
        method="POST",
        path="/autotrade_account/{id}/authenticate",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_id_refresh_token(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/{id}/refresh-token"""
    return client.call(
        method="POST",
        path="/autotrade_account/{id}/refresh-token",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_refresh_tokens_all(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/refresh-tokens/all"""
    return client.call(
        method="POST",
        path="/autotrade_account/refresh-tokens/all",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_search(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/search"""
    return client.call(
        method="POST",
        path="/autotrade_account/search",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_trade_autotrade_account_trade_id_modify(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/trade/{autotrade_account_trade_id}/modify"""
    return client.call(
        method="POST",
        path="/autotrade_account/trade/{autotrade_account_trade_id}/modify",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_autotrade_account_update_balance(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /autotrade_account/update-balance"""
    return client.call(
        method="POST",
        path="/autotrade_account/update-balance",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def put_autotrade_account_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """PUT /autotrade_account/{id}"""
    return client.call(
        method="PUT",
        path="/autotrade_account/{id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def put_autotrade_account_id_balance(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """PUT /autotrade_account/{id}/balance"""
    return client.call(
        method="PUT",
        path="/autotrade_account/{id}/balance",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )
