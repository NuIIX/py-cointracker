import requests
from config.config import API_KEY, API_URL, DEFAULT_PARAMS

class CoinMarketCapAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY,
        })

    def get_listings(self):
        try:
            response = self.session.get(API_URL, params=DEFAULT_PARAMS)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении данных: {e}")
            return None
