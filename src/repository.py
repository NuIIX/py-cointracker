from src.models import CryptoCurrency


class CryptoRepository:
    """Репозиторий для хранения и обработки данных о криптовалютах.

    Предоставляет методы для загрузки данных из JSON и поиска криптовалют по названию или символу.

    Attributes:
        data (list[CryptoCurrency]): Список объектов криптовалют, хранящихся в репозитории.
    """

    def __init__(self):
        """Инициализирует пустой репозиторий криптовалют."""
        self.data = []

    def load_data(self, json_data):
        """Загружает данные о криптовалютах из JSON-структуры.

        Args:
            json_data (dict): JSON-данные, полученные от API. Ожидается структура:
                {
                    "data": [
                        {
                            "name": str,
                            "symbol": str,
                            "circulating_supply": float,
                            "quote": {
                                "USD": {
                                    "price": float,
                                    "market_cap": float
                                }
                            }
                        },
                        ...
                    ]
                }

        Note:
            Если json_data не содержит ожидаемой структуры, метод завершится без ошибок,
            но не добавит никаких данных в репозиторий.
        """
        if json_data and "data" in json_data:
            for item in json_data["data"]:
                crypto = CryptoCurrency(
                    name=item.get("name"),
                    symbol=item.get("symbol"),
                    price=item.get("quote", {}).get("USD", {}).get("price", 0),
                    market_cap=item.get("quote", {}).get("USD", {}).get("market_cap", 0),
                    circulating_supply=item.get("circulating_supply", 0)
                )
                self.data.append(crypto)

    def search(self, query: str):
        """Выполняет поиск криптовалют по названию или символу (без учёта регистра).

        Args:
            query (str): Строка для поиска (может быть названием криптовалюты или её символом).

        Returns:
            list[CryptoCurrency]: Список найденных криптовалют, где:
                - Название (name) точно совпадает с запросом (без учёта регистра), ИЛИ
                - Символ (symbol) точно совпадает с запросом (без учёта регистра)

        Example:
            >>> repo = CryptoRepository()
            >>> repo.load_data(some_json_data)
            >>> repo.search("btc")
            [<CryptoCurrency: Bitcoin (BTC)>]
        """
        query_lower = query.lower()
        result = [
            crypto for crypto in self.data
                  if crypto.name.lower() == query_lower or crypto.symbol.lower() == query_lower
        ]
        return result
