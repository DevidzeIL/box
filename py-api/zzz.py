import random
import requests
import json


def test(url, headers):
    # Список аэропортов, терминалов и кодов
    airportsPath = 'api/v1/seller/airports'
    airportsResponse = json.loads(requests.get(url+airportsPath, headers=headers).text)
    airports_codeList = list()
    for airports in airportsResponse['data']['airports']:
        airports_codeList.append(airports['code_iata'])
        # print(airports['title'])
        # for terminal in airports['terminals']:
            # print(" -", terminal['title'])

    # Список брендов
    brandsList = set()
    for code in airports_codeList:
        brandsPath = 'api/v1/seller/partners?airport_code=' + code
        brandsResponse = json.loads(requests.get(url+brandsPath, headers=headers).text)
        # print("\n", code)
        for brands in brandsResponse['data']['partners']:
            brandsList.add(brands['brand_tag'])
            # print(" -", brands['brand_tag'])

    # Информация о бренде
    for brand in brandsList:
        brandPath = 'api/v1/seller/brand?brand_tag=' + brand
        brandResponse = json.loads(requests.get(url+brandPath, headers=headers).text)
        # print("\n", brandResponse)

    # Список предложений
    for code in airports_codeList:
        # print("\n -", code)
        stocksPath = 'api/v1/seller/stocks?airport_code=' + code
        stocksResponse = json.loads(requests.get(url+stocksPath, headers=headers).text)
        # for stocks in stocksResponse['data']['stocks']:
        #     print(stocks)

    # Подробности предложения
    for code in airports_codeList:
        print('\n', code)
        stockPath = 'api/v1/seller/stock?airport_code=' + code
        stockResponse = json.loads(requests.get(url+stockPath, headers=headers).text)
        # for stock in stockResponse['data']['stocks']:
        #     print('stock_id -', stock['stock_id'])
        #     print('title -', stock['title'])
