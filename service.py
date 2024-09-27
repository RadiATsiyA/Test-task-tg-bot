import requests

from config import CURRENCY_API_URL


def get_currency():
    url = CURRENCY_API_URL
    response = requests.get(url)
    data = response.json()

    if not data:
        raise 'Something went wrong..'
    return data['data']['RUB']['value']

# check = get_crypto_price()
# print(check)
