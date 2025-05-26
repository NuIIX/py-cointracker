class CryptoCurrency:
    """Класс, представляющий криптовалюту с основными финансовыми показателями.

    Attributes:
        name (str): Полное название криптовалюты (например, "Bitcoin").
        symbol (str): Тикер криптовалюты (например, "BTC").
        price (float): Текущая цена в USD.
        market_cap (float): Рыночная капитализация в USD.
        circulating_supply (float): Количество монет в обращении.
    """

    def __init__(self, name: str, symbol: str, price: float, market_cap: float, circulating_supply: float):
        """Инициализирует объект криптовалюты с заданными параметрами.

        Args:
            name: Полное название криптовалюты.
            symbol: Биржевой тикер криптовалюты.
            price: Текущая цена в долларах США.
            market_cap: Рыночная капитализация в долларах США.
            circulating_supply: Количество монет в обращении.
        """
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        self.circulating_supply = circulating_supply

    def __str__(self):
        """Возвращает строковое представление объекта криптовалюты.

        Returns:
            str: Форматированная строка с основными данными о криптовалюте.
                Пример: "Bitcoin (BTC) - Price: $42000.00, Market Cap: $8000.00, 
                Circulating Supply: 1870"
        """
        return (f"{self.name} ({self.symbol}) - Price: ${self.price:.2f}, "
                f"Market Cap: ${self.market_cap:.2f}, Circulating Supply: {self.circulating_supply}")
