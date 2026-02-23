from elcsoft.generator import generate_client_from_swagger


def main() -> None:
    output = generate_client_from_swagger(
        spec_url="http://localhost:3001/manual.json",
        output_file="elcsoft/generated/manual_api.py",
        class_name="ManualApiClient",
    )

    print("생성 완료:", output)
    print("이후 사용 예:")
    print("from elcsoft.generated.manual_api import ManualApiClient")
    print("client = ManualApiClient(spec_url='http://localhost:3001/manual.json', base_url='http://localhost:3001')")


if __name__ == "__main__":
    main()
