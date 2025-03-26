import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CMC_PRO_API_KEY")
API_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
DEFAULT_PARAMS = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
