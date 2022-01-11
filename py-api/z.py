import random
import requests
import json


# Получение списка аэропортов
def airports_list(url, headers):
    airports_dict = {}

    # Список аэропортов, терминалов и кодов
    airportsPath = 'api/v1/seller/airports'
    airportsResponse = json.loads(requests.get(url+airportsPath, headers=headers).text)
    for airports in airportsResponse['data']['airports']:
        airports_dict.setdefault(airports['id'], []).append(airports['code_iata'])

    return airports_dict;


# Проветка совместимости аэропортов
def test_airport(url, headers, airports_dict):
    # Получаем список точек по аэропорту
    airport_id = random.choice(list(airports_dict))
    airport_code = random.choice(airports_dict[airport_id])

    # Получаем точки продаж
    pointsParams = { "airport_code": airport_code }
    pointsPath = 'api/v1/seller/points'
    pointsResponse = json.loads(requests.get(url+pointsPath,params=pointsParams, headers=headers).text)

    # Проверяем аэропорот на пустое значение
    while pointsResponse['data']['points'] == []:
        airport_id = random.choice(list(airports_dict))
        airport_code = random.choice(airports_dict[airport_id])

        pointsParams = { "airport_code": airport_code }
        pointsPath = 'api/v1/seller/points'
        pointsResponse = json.loads(requests.get(url+pointsPath,params=pointsParams, headers=headers).text)

    return airport_id, airport_code, pointsResponse


# Выбор продукта
def choose_product(pointsResponse):
    product_dict = {}

    # Записываем продукты и количество в список
    for point in pointsResponse['data']['points']:
        for product in point['products']:
            if('max_products_quantity' in point['custom_info']):
                product_dict.setdefault(product['id'], []).append(random.randint(1, point['custom_info']['max_products_quantity']))
            else:
                product_dict.setdefault(product['id'], []).append(0)

    product_id = random.choice(list(product_dict))
    product_quantity = random.choice(product_dict[product_id])

    return product_id, product_quantity

# Генерация токена корзины
def get_cart_token(url, headers):
    # Получение токена корзины
    tokenPath = 'api/v2/seller/userCart'
    tokenResponse = json.loads(requests.post(url+tokenPath, headers=headers).text)
    cart_token = tokenResponse['data']['token']

    return cart_token;

# Добавление услуги в корзину
def add_to_cart(url, headers, airport_id, product_id, product_quantity, cart_token):
    bodyRequest ={
        "items": [
            {
                "id": product_id,
                "quantity": product_quantity
            },
        ],
        "airport_id": airport_id,

        "token": cart_token
    }

    item_groupPath = 'api/v2/seller/userCart/itemGroup'
    item_groupResponse = json.loads(requests.post(url+item_groupPath, json=bodyRequest, headers=headers).text)

    return item_groupResponse;

# Просмотр корзины
def open_cart(url, headers, cart_token):
    cartPath = 'api/v2/seller/userCart?token=' + cart_token
    cartResponse = json.loads(requests.get(url+cartPath, headers=headers).text)

    return cartResponse;


def main():
    token = '7afd5bb7a750f431b2d10ccb4c347b741c0cea18d7b65b3a85d7739f7e2657ea'
    url = 'https://dev.api.maocloud.ru/'

    headers={'Authorization': f'Bearer {token}'}

    # Получаем список аэропортов
    airports_dict = airports_list(url, headers)

    #Проверяем аэропорт
    airport_id, airport_code, pointsResponse = test_airport(url, headers, airports_dict)

    # Выбираем случайный продукт из возможных в выбранном аэропорту
    product_id, product_quantity = choose_product(pointsResponse)
    print('Airport_ID =', airport_id, '; Airport_CODE =', airport_code, '; Product_ID =', product_id, '; Product_Quantity =', product_quantity)


    # Генерируем токер корзины
    cart_token = get_cart_token(url, headers)

    # Добавляем продукт в корзину и проверяем значение корзины
    add_to_cart(url, headers, airport_id, product_id, product_quantity, cart_token)

    open_cart = open_cart(url, headers, cart_token)

    print(open_cart)

if __name__ == '__main__':
    main()
