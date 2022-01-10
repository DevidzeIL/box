import random
import requests
import json

def get_customer_token(url, phone):
    token_params = {
        'phone': phone
    }

    token_path = 'api/v2/seller/...'
    token_response = json.loads(requests.post(url+token_path, params=token_params).text)
    token = token_response['data']['token']
    return token


def get_customer_cart_token(url, headers):
    cart_token_path = 'api/v2/seller/userCart'
    cart_token_response = json.loads(requests.post(url+cart_token_path, headers=headers).text)
    cart_token = cart_token_response['data']['token']
    return cart_token


def choose_language():
    return


def get_list_airports(url, headers):
    airports_dict = {}

    airports_path = 'api/v1/seller/airports'
    airports_response = json.loads(requests.get(url+airports_path, headers=headers).text)
    for airports in airports_response['data']['airports']:
        airports_dict.setdefault(airports['id'], []).append(airports['code_iata'])
    return airports_dict

# !!!-!!!-!!! Как выглядит response?
def choose_airport(airports_dict):
    airport_id = random.choice(list(airports_dict))
    airport_code = random.choice(airports_dict[airport_id])
    return airport_id, airport_code


# !!!-!!!-!!! А где вообще категории в points?
def get_list_categories(url, headers, airport_code, language_code):
    categories_dict = {}
    categories_params = {
        'airport_code': airport_code,
        'language_code': language_code
    }

    categories_path = 'api/v1/seller/serviceCategories'
    categories_response = json.loads(requests.get(url+categories_path, params=categories_params, headers=headers).text)
    # !!!-!!!-!!! Записать список категорий в словарь
    return categories_dict


# !!!-!!!-!!! А где вообще категории в points?
def get_list_points_by_category(url, headers, airport_code, category_id):
    points_dict = {}
    points_params = {
        'airport_code': airport_code,
        'products_category': category_id
    }

    points_path = 'api/v1/seller/points'
    points_response = json.loads(requests.get(url+points_path, params=points_params, headers=headers).text)
    # !!!-!!!-!!! Записать список точек по категории в словарь
    return points_dict


def choose_point(points_dict):
    return


def add_to_cart(url, headers, airport_id, cart_token):
    body_request = {
        "items": [
        ],

        'airport_id': airport_id,

        'token': cart_token
    }

    item_group_path = 'api/v2/seller/userCart/itemGroup'
    item_group_response = json.loads(requests.post(url+item_group_path, json=body_request, headers=headers).text)
    return


def open_cart(url, headers, cart_token):
    cart_path = 'api/v2/seller/userCart?token=' + cart_token
    cart_response = json.loads(requests.get(url+cart_path, headers=headers).text)
    return cart_response


def confirm_order():
    return


def register_customer():
    return


def confirm_customer():
    return


def login_customer():
    return


def get_customer_profile():
    return


def get_customer_orders():
    return



def main():
    # phone = '+79777751713'
    # token = get_customer_token(url, phone)

    token = '7afd5bb7a750f431b2d10ccb4c347b741c0cea18d7b65b3a85d7739f7e2657ea'
    url = 'https://dev.api.maocloud.ru/'

    headers={'Authorization': f'Bearer {token}'}

    language_code = choose_language()

    cart_token = get_customer_cart_token(url, headers)

    airports_dict = get_list_airports(url, headers)

    airport_id, airport_code = choose_airport(airports_dict)
    print(airport_id, '->', airport_code)

    categories_dict = get_list_categories(url, headers, airport_code, language_code)

    for id in categories_dict:
        category_id = id
        points_dict = get_list_points_by_category(url, headers, airport_code, category_id)
        choose_point(points_dict)
        add_to_cart(url, headers, airport_id, cart_token)

    open_cart(url, headers, cart_token)
    confirm_order()
    register_customer()
    confirm_customer()
    login_customer()
    get_customer_profile()
    get_customer_orders()



    print('--- end ---')


if __name__ == '__main__':
    main()
