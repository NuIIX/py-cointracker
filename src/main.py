import os
from src.api import CoinMarketCapAPI
from src.repository import CryptoRepository

def main():
    api = CoinMarketCapAPI()
    json_data = api.get_listings()

    if not json_data:
        print("Не удалось загрузить данные с сервера CoinMarketCap.")
        return

    repository = CryptoRepository()
    repository.load_data(json_data)

    while True:
        user_input = input("Введите названия или символы криптовалют (через запятую), либо exit/break/stop для выхода:\n> ").strip()

        if user_input.lower() in ("exit", "break", "stop"):
            print("Выход из программы...")
            break

        queries = [q.strip() for q in user_input.split(",")]
        all_results = []

        for query in queries:
            if not query:
                continue

            results = repository.search(query)
            if results:
                for crypto in results:
                    print(crypto)
                all_results.extend(results)
            else:
                print(f"Криптовалюта {query} не найдена.")

        if all_results:
            save_input = input("Сохранить результаты в файл? [y/n] ").strip().lower()
            if save_input == 'y':
                file_format = input("Введите формат файла (csv/json/xml): ").strip().lower()
                file_name = input("Введите имя файла (без расширения): ").strip()
                file_path = input("Введите полный путь для сохранения файла (например, C:\\path\\to\\folder): ").strip()

                full_file_path = f"{file_path.rstrip(os.sep)}{os.sep}{file_name}.{file_format}"

                from src.serializer import export_to_csv, export_to_json, export_to_xml, get_file_size

                if file_format == "csv":
                    export_to_csv(all_results, full_file_path)
                elif file_format == "json":
                    export_to_json(all_results, full_file_path)
                elif file_format == "xml":
                    export_to_xml(all_results, full_file_path)
                else:
                    print("Неподдерживаемый формат. Результаты не сохранены.")
                    continue

                file_size = get_file_size(full_file_path)
                print(f"Файл сохранён: {full_file_path}")
                print(f"Размер файла: {file_size}")
            else:
                print("Результаты не сохраняются.")

if __name__ == "__main__":
    main()
