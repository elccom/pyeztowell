# 공통 라이브러리 (Swagger 참조 REST API 공통화)

`http://localhost:3001/manual.json` Swagger(OpenAPI) 문서를 참조해,
공통 라이브러리 안에 **실제 API 메서드 코드**를 생성하고,
다른 프로그램에서 import 해서 재사용하는 목적의 패키지입니다.

## 설치

```bash
pip install -e .
```

## 1) Swagger로 공통 API 클래스 생성

```bash
generate-common-api \
    --spec-url http://localhost:3001/manual.json \
    --output elcsoft/generated/manual_api.py \
    --class-name ManualApiClient
```

생성 결과: `elcsoft/generated/manual_api.py`

- Swagger의 각 엔드포인트(operationId 우선)를 Python 메서드로 생성
- 생성 메서드는 내부적으로 공통 HTTP 로직(`SwaggerClient`)을 사용

## 2) 생성된 공통 API를 다른 프로그램에서 사용

```python
from elcsoft.generated.manual_api import ManualApiClient

client = ManualApiClient(
        spec_url="http://localhost:3001/manual.json",
        base_url="http://localhost:3001",
        bearer_token="YOUR_TOKEN",  # 필요 시
)

# 생성된 메서드 이름 예시 (실제 이름은 Swagger 문서 기반)
# result = client.get_users(query_params={"page": 1})
# result = client.create_user(json_body={"name": "Kim"})
```

## 공통 로직(기반 클래스) 기능

- base URL 추론/설정
- path/query/header/json/body 파라미터 처리
- Bearer 토큰 기본 헤더 처리
- JSON/텍스트 응답 자동 변환

## 참고

현재 에이전트 세션에서는 `localhost:3001` 접근이 불가할 수 있으므로,
생성/실행은 사용자 로컬 환경에서 실행해 주세요.
