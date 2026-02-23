from elcsoft import SwaggerClient


def main() -> None:
    client = SwaggerClient(
        spec_url="http://localhost:3001/manual.json",
        base_url="http://localhost:3001",
        timeout=10,
    )

    # operationId가 없는 경우 path + method로 호출
    # 실제 엔드포인트는 manual.json에 맞게 변경해서 사용하세요.
    try:
        response = client.call("GET", "/health")
        print("GET /health =>", response)
    except Exception as exc:
        print("요청 실패:", exc)


if __name__ == "__main__":
    main()
