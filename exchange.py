import requests
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
from strings import PAIR, FIAT, url


headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'e4402d27-462c-4cb0-8197-91263de378e1',
}

session = Session()
session.headers.update(headers)


def req_exchange_val(val):
    list_of_results = []
    data = {}
    for i in PAIR:
        parameters = {
            'slug': FIAT[0],
            'convert': i
        }
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
        result = float(val) / data['data']['20317']['quote'][i]['price']
        list_of_results.append(round(result, 8))
    return list_of_results


def check_code_crypto():
    for i in PAIR:
        parameters = {
            'id': FIAT[1],
            'convert': i
        }
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            pprint.pprint(data)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


check_code_crypto()
