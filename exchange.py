import requests
import json

pair = ('btcusd', 'trxusd', 'ethusd', 'dogeusd')


def req_exchange_val(market, val):
    list_of_results = []
    for i in pair:
        c = requests.get(f'https://api.cryptowat.ch/markets/{market}/{i}/price')
        crypto_prices = c.json()
        wynik = float(val) / crypto_prices['result']['price']
        list_of_results.append(round(wynik, 8))
    return list_of_results


def crypto_list():
    c = requests.get(f'https://api.cryptowat.ch/markets')
    crypto_prices2 = c.json()
    show_me = json.dumps(crypto_prices2)
    print(show_me)


# crypto_list()
