import os
import re
from src.api import CoinMarketCapAPI
from src.repository import CryptoRepository
from src.serializer import export_to_csv, export_to_json, export_to_xml, get_file_size


def is_valid_directory(path):
    return os.path.isdir(path) and os.access(path, os.W_OK)


def is_valid_filename(filename):
    return bool(re.match(r'^[\w\-.]+$', filename))


def main():
    api = CoinMarketCapAPI()
    json_data = api.get_listings()

    if not json_data:
        print("Не удалось загрузить данные с сервера CoinMarketCap.")
        return

    repository = CryptoRepository()
    repository.load_data(json_data)

    format_export_map = {
        "csv": export_to_csv,
        "json": export_to_json,
        "xml": export_to_xml
    }

    while True:
        user_input = input("Введите названия или символы криптовалют (через запятую), либо exit/break/stop для выхода:\n> ").strip()

        if user_input.lower() in ("exit", "break", "stop"):
            print("Выход из программы...")
            break

        queries = [q.strip() for q in user_input.split(",") if q.strip()]
        all_results = []

        for query in queries:
            results = repository.search(query)
            if results:
                for crypto in results:
                    print(crypto)
                all_results.extend(results)
            else:
                print(f"Криптовалюта '{query}' не найдена.")

        if all_results:
            save_input = input("Сохранить результаты в файл? [y/n] ").strip().lower()
            if save_input == 'y':
                file_format = input("Введите формат файла (csv/json/xml): ").strip().lower()
                export_function = format_export_map.get(file_format)

                if not export_function:
                    print("Неподдерживаемый формат. Результаты не сохранены.")
                    continue

                file_name = input("Введите имя файла (без расширения): ").strip()
                if not is_valid_filename(file_name):
                    print("Недопустимое имя файла. Используйте только буквы, цифры, тире, подчёркивания и точки.")
                    continue

                file_path = input("Введите полный путь для сохранения файла (например, C:\\path\\to\\folder): ").strip()
                if not is_valid_directory(file_path):
                    print("Недопустимый путь. Убедитесь, что папка существует и доступна для записи.")
                    continue

                full_file_path = os.path.join(file_path, f"{file_name}.{file_format}")

                try:
                    export_function(all_results, full_file_path)
                    file_size = get_file_size(full_file_path)
                    print(f"Файл сохранён: {full_file_path}")
                    print(f"Размер файла: {file_size}")
                except Exception as e:
                    print(f"Ошибка при сохранении файла: {e}")


if __name__ == "__main__":
    main()
