import random
import requests
import json
import datetime


token = '7afd5bb7a750f431b2d10ccb4c347b741c0cea18d7b65b3a85d7739f7e2657ea'
url = 'https://dev.api.maocloud.ru/'

headers={'Authorization': f'Bearer {token}'}
language_code = ['ru','en']
phone = '+79777751713'

def get_customer_token(phone):
    token_params = {
        'phone': phone
    }

    token_path = 'api/v2/seller/...'
    token_response = json.loads(requests.post(url+token_path, params=token_params).text)
    token = token_response['data']['token']
    return token


def get_customer_cart_token():
    cart_token_path = 'api/v2/seller/userCart'
    cart_token_response = json.loads(requests.post(url+cart_token_path, headers=headers).text)
    cart_token = cart_token_response['data']['token']
    return cart_token


def choose_dates():
    numdays = 30
    base = datetime.date.today()
    date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]

    date_from = random.choice(date_list)
    date_to = random.choice(date_list)
    while date_to <= date_from:
        date_to = random.choice(date_list)

    return date_from, date_to


def get_list_airports():
    airports_dict = {}
    airports_path = 'api/v1/seller/airports'
    airports_response = json.loads(requests.get(url+airports_path, headers=headers).text)
    for airports in airports_response['data']['airports']:
        airports_dict.setdefault(airports['id'], []).append(airports['code_iata'])
    return airports_dict


def choose_airport(airports_dict):
    airport_id = random.choice(list(airports_dict))
    airport_code = random.choice(airports_dict[airport_id])
    return airport_id, airport_code


def generate_flight(airports_dict):
    airports_chooses = {}
    airport_id_from, airport_code_from = choose_airport(airports_dict)
    airport_id_to, airport_code_to = choose_airport(airports_dict)

    while airport_id_from == airport_id_to:
        airport_id_to, airport_code_to = choose_airport(airports_dict)

    airports_chooses = {}

    airports_chooses[airport_id_from] = airport_code_from
    airports_chooses[airport_id_to] = airport_code_to

    return airports_chooses


def get_list_categories(airport_code, language_code):
    categories_dict = {}
    categories_params = {
        'airport_code': airport_code,
        'language_code': language_code
    }

    categories_path = 'api/v1/seller/serviceCategories'
    categories_response = json.loads(requests.get(url+categories_path, params=categories_params, headers=headers).text)
    for categories in categories_response['data']['categories']:
        categories_dict.setdefault(categories['id'], []).append(categories['name'])
    return categories_dict


# !!!-!!!-!!! А где вообще категории в points?
def get_list_points_by_category(airport_code, category_id, language_code):
    points_dict = {}
    points_params = {
        'airport_code': airport_code,
        'products_category': category_id,
        'language_code': language_code
    }

    points_path = 'api/v1/seller/points'
    points_response = json.loads(requests.get(url+points_path, params=points_params, headers=headers).text)
    # !!!-!!!-!!! Записать список точек по категории в словарь
    return points_dict


def choose_point(points_dict):
    return


def add_to_cart(airport_id, cart_token):
    body_request = {
        "items": [
        ],

        'airport_id': airport_id,

        'token': cart_token
    }

    item_group_path = 'api/v2/seller/userCart/itemGroup'
    item_group_response = json.loads(requests.post(url+item_group_path, json=body_request, headers=headers).text)
    return


def open_cart(cart_token):
    cart_path = 'api/v2/seller/userCart?token=' + cart_token
    cart_response = json.loads(requests.get(url+cart_path, headers=headers).text)
    return cart_response


def confirm_cart(cart_token):
    confirm_cart_params = {
        'token': cart_token,
    }

    confirm_cart_path = 'api/v1/seller/UserCartRegisterOrder'
    confirm_cart_response = json.loads(requests.post(url+confirm_cart_path, params=confirm_cart_params, headers=headers).text)

    return confirm_cart_response


def register_customer():
    return


def confirm_customer():
    return


def login_customer():
    return


def get_customer_profile():
    return


def get_customer_cart(cart_token):
    customer_cart_params = {
        'token': cart_token,
        'phone': phone
    }

    customer_cart_path = 'api/v1/seller/userCart'
    customer_cart_response = json.loads(requests.get(url+customer_cart_path, params=customer_cart_params, headers=headers).text)

    return customer_cart_response



def main():
    date_from, date_to = choose_dates()
    print('\nFrom ->', date_from, '\nTo ->', date_to)

    cart_token = get_customer_cart_token()

    airports_dict = get_list_airports()

    airports_chooses = generate_flight(airports_dict)
    print ('\n', airports_chooses)

    for lang in language_code:
        print('\nLanguage ->', lang)

        for airport_id in airports_chooses:
            print('\nAirport ID ->', airport_id)

            categories_dict = get_list_categories(airports_chooses[airport_id], lang)
            print(categories_dict)

            for category_id in categories_dict:
                print('Category ID ->', category_id)

                points_dict = get_list_points_by_category(airports_chooses[airport_id], category_id, lang)
                choose_point(points_dict)
                add_to_cart(airport_id, cart_token)

            open_cart(cart_token)
            confirm_cart(cart_token)

            register_customer()
            confirm_customer()
            login_customer()

            get_customer_profile()
            get_customer_cart(cart_token)




    print('--- end ---')


if __name__ == '__main__':
    main()
