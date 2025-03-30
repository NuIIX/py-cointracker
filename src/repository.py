from src.models import CryptoCurrency

class CryptoRepository:
    def __init__(self):
        self.data = []

    def load_data(self, json_data):
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
        """
        Возвращает список криптовалют, где query совпадает
        либо с name, либо с symbol (без учёта регистра).
        """
        query_lower = query.lower()
        result = [
            crypto for crypto in self.data
                  if crypto.name.lower() == query_lower or crypto.symbol.lower() == query_lower
        ]
        return result
