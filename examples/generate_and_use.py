from codegen.generator import generate_router_files_from_swagger


def main() -> None:
    output = generate_router_files_from_swagger(
        spec_url="http://localhost:3001/api-docs.json",
        output_dir="elcsoft",
    )

    print("생성 완료:", output)
    print("이후 사용 예:")
    print("from elcsoft import SwaggerClient")
    print("from elcsoft import users")
    print("client = SwaggerClient(spec_url='http://localhost:3001/api-docs.json', base_url='http://localhost:3001')")
    print("result = users.get_users(client, query_params={'page': 1})")


if __name__ == "__main__":
    main()
