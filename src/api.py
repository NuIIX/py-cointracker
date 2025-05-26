import requests
from config.config import API_KEY, API_URL, DEFAULT_PARAMS


class CoinMarketCapAPI:
    def __init__(self):
        """Инициализирует экземпляр класса CoinMarketCapAPI.
        
        Настраивает HTTP-сессию с заголовками для работы с API CoinMarketCap,
        включая API ключ для аутентификации.
        """
        self.session = requests.Session()
        self.session.headers.update({
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': API_KEY,
        })

    def get_listings(self):
        """Получает список криптовалют с их текущими данными.

        Отправляет GET-запрос к API CoinMarketCap с параметрами по умолчанию
        и возвращает ответ в формате JSON.

        Returns:
            dict: Ответ API в формате JSON с данными о криптовалютах, или None в случае ошибки.

        Raises:
            requests.exceptions.RequestException: Если произошла ошибка при выполнении запроса.
        """
        try:
            response = self.session.get(API_URL, params=DEFAULT_PARAMS)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при получении данных: {e}")
            return None
