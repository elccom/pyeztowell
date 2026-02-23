from elcsoft import SwaggerClient


def main() -> None:
    client = SwaggerClient(
        spec_url="http://localhost:3001/manual.json",
        base_url="http://localhost:3001",
    )

    operations = client.list_operations()
    for operation_id, (method, path) in operations.items():
        print(f"{operation_id}: {method} {path}")


if __name__ == "__main__":
    main()
