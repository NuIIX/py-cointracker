class CryptoCurrency:
    def __init__(self, name: str, symbol: str, price: float, market_cap: float, circulating_supply: float):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        self.circulating_supply = circulating_supply

    def __str__(self):
        return (f"{self.name} ({self.symbol}) - Price: ${self.price:.2f}, "
                f"Market Cap: ${self.market_cap:.2f}, Circulating Supply: {self.circulating_supply}")
