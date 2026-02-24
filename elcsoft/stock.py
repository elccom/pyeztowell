from __future__ import annotations

from typing import Any, Dict, Optional

from elcsoft.core.client import SwaggerClient

# Auto-generated from http://localhost:3001/api-docs.json
# Router: stock

def delete_stock_stock_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """DELETE /stock/{stock_id}"""
    return client.call(
        method="DELETE",
        path="/stock/{stock_id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/"""
    return client.call(
        method="GET",
        path="/stock/",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_guide_apis(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/guide/apis"""
    return client.call(
        method="GET",
        path="/stock/guide/apis",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_institutional_foreign_net_buy(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/institutional/foreign/net-buy"""
    return client.call(
        method="GET",
        path="/stock/institutional/foreign/net-buy",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_institutional_foreign_net_sell(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/institutional/foreign/net-sell"""
    return client.call(
        method="GET",
        path="/stock/institutional/foreign/net-sell",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_institutional_institution_net_buy(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/institutional/institution/net-buy"""
    return client.call(
        method="GET",
        path="/stock/institutional/institution/net-buy",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_institutional_institution_net_sell(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/institutional/institution/net-sell"""
    return client.call(
        method="GET",
        path="/stock/institutional/institution/net-sell",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_institutional_stock_stock_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/institutional/stock/{stockCode}"""
    return client.call(
        method="GET",
        path="/stock/institutional/stock/{stockCode}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_last_market_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/last/{market}/{code}"""
    return client.call(
        method="GET",
        path="/stock/last/{market}/{code}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_latest_type_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/latest/{type}/{code}"""
    return client.call(
        method="GET",
        path="/stock/latest/{type}/{code}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_master_count(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/master/count"""
    return client.call(
        method="GET",
        path="/stock/master/count",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_master_search(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/master/search"""
    return client.call(
        method="GET",
        path="/stock/master/search",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_methods(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/methods"""
    return client.call(
        method="GET",
        path="/stock/methods",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_naver_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/naver/{code}"""
    return client.call(
        method="GET",
        path="/stock/naver/{code}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_naver_search_keyword(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/naver/search/{keyword}"""
    return client.call(
        method="GET",
        path="/stock/naver/search/{keyword}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_program_buy_top(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/program/buy-top"""
    return client.call(
        method="GET",
        path="/stock/program/buy-top",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_program_sell_top(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/program/sell-top"""
    return client.call(
        method="GET",
        path="/stock/program/sell-top",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_program_stock_trend_stock_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/program/stock-trend/{stockCode}"""
    return client.call(
        method="GET",
        path="/stock/program/stock-trend/{stockCode}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_query_type_code_trading_date(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/query/{type}/{code}/{trading_date}"""
    return client.call(
        method="GET",
        path="/stock/query/{type}/{code}/{trading_date}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_fall(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/fall"""
    return client.call(
        method="GET",
        path="/stock/ranking/fall",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_gainers_type(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/gainers/{type}"""
    return client.call(
        method="GET",
        path="/stock/ranking/gainers/{type}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_losers_type(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/losers/{type}"""
    return client.call(
        method="GET",
        path="/stock/ranking/losers/{type}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_market_cap(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/market-cap"""
    return client.call(
        method="GET",
        path="/stock/ranking/market-cap",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_rise(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/rise"""
    return client.call(
        method="GET",
        path="/stock/ranking/rise",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_transaction_amount(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/transaction-amount"""
    return client.call(
        method="GET",
        path="/stock/ranking/transaction-amount",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_volume(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/volume"""
    return client.call(
        method="GET",
        path="/stock/ranking/volume",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_ranking_volume_type(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/ranking/volume/{type}"""
    return client.call(
        method="GET",
        path="/stock/ranking/volume/{type}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_stats_summary(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/stats/summary"""
    return client.call(
        method="GET",
        path="/stock/stats/summary",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_stats_type_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/stats/{type}/{code}"""
    return client.call(
        method="GET",
        path="/stock/stats/{type}/{code}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_stock_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/{stock_id}"""
    return client.call(
        method="GET",
        path="/stock/{stock_id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_theme_by_stock_stock_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/theme/by-stock/{stockCode}"""
    return client.call(
        method="GET",
        path="/stock/theme/by-stock/{stockCode}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_theme_hot(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/theme/hot"""
    return client.call(
        method="GET",
        path="/stock/theme/hot",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_theme_list(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/theme/list"""
    return client.call(
        method="GET",
        path="/stock/theme/list",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_theme_ranking(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/theme/ranking"""
    return client.call(
        method="GET",
        path="/stock/theme/ranking",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def get_stock_theme_stocks_theme_code(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """GET /stock/theme/stocks/{themeCode}"""
    return client.call(
        method="GET",
        path="/stock/theme/stocks/{themeCode}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def patch_stock_stock_id_deactivate(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """PATCH /stock/{stock_id}/deactivate"""
    return client.call(
        method="PATCH",
        path="/stock/{stock_id}/deactivate",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_stock(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /stock/"""
    return client.call(
        method="POST",
        path="/stock/",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_stock_bulk(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /stock/bulk"""
    return client.call(
        method="POST",
        path="/stock/bulk",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_stock_call(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /stock/call"""
    return client.call(
        method="POST",
        path="/stock/call",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_stock_guide_call(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /stock/guide/call"""
    return client.call(
        method="POST",
        path="/stock/guide/call",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_stock_master_update(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /stock/master/update"""
    return client.call(
        method="POST",
        path="/stock/master/update",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def post_stock_upsert(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """POST /stock/upsert"""
    return client.call(
        method="POST",
        path="/stock/upsert",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )

def put_stock_stock_id(
    client: SwaggerClient,
    *,
    path_params: Optional[Dict[str, Any]] = None,
    query_params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    json_body: Optional[Any] = None,
    data: Optional[Any] = None,
    timeout: Optional[int] = None,
) -> Any:
    """PUT /stock/{stock_id}"""
    return client.call(
        method="PUT",
        path="/stock/{stock_id}",
        path_params=path_params,
        query_params=query_params,
        headers=headers,
        json_body=json_body,
        data=data,
        timeout=timeout,
    )
