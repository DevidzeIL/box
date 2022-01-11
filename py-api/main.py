import random
import requests
import json
import datetime


token = '7afd5bb7a750f431b2d10ccb4c347b741c0cea18d7b65b3a85d7739f7e2657ea'
url_partnership = 'https://dev.api.maocloud.ru/'
url_mileonair = 'https://developer.mileonair.com/'

headers={'Authorization': f'Bearer {token}'}
language_code = ['ru','en']
phone = '+79777751713'

def get_customer_token(phone):
    token_params = {
        'phone': phone
    }

    token_path = 'api/v2/seller/...'
    token_response = json.loads(requests.post(url_partnership+token_path, params=token_params).text)
    token = token_response['data']['token']
    return token


def get_customer_cart_token():
    cart_token_path = 'api/v2/seller/userCart'
    cart_token_response = json.loads(requests.post(url_partnership+cart_token_path, headers=headers).text)
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
    airports_response = json.loads(requests.get(url_partnership+airports_path, headers=headers).text)
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
    categories_response = json.loads(requests.get(url_partnership+categories_path, params=categories_params, headers=headers).text)
    for categories in categories_response['data']['categories']:
        categories_dict.setdefault(categories['id'], []).append(categories['name'])
    return categories_dict


# !!!-!!!-!!! А где вообще категории в points?
def get_list_points_by_category(airport_code, category_id, language_code):
    products_dict = {}
    # points_params = {
    #     'airport_code': airport_code,
    #     'products_category': category_id,
    #     'language_code': language_code
    # }

    points_params = {
        'airport_code': 'SVO',
        'products_category': '3',
        'language_code': 'ru'
    }

    points_path = 'api/v2/seller/points'
    points_response = json.loads(requests.get(url_partnership+points_path, params=points_params, headers=headers).text)

    if points_response['data']['points'] != []:
        for point in points_response['data']['points']:
            for act_type in point['act_types']:
                for group in act_type['groups']:
                    for product in group['products']:
                        products_dict.setdefault(product['id'], []).append(0)

            # if 'max_products_quantity' in point['custom_info']:
            #     # products_dict.setdefault(product['id'], []).append(random.randint(1, point['custom_info']['max_products_quantity']))
            #     print('40')


    else:
        print('Нет точек ')

    print('\n', products_dict, '\n')

    return products_dict


def choose_point(products_dict):
    product_id = random.choice(list(products_dict))
    product_quantity = random.choice(products_dict[product_id])

    return product_id, product_quantity


def add_to_cart(airport_id, cart_token, product_id, product_quantity, estimated_date):
    print(airport_id)
    print(cart_token)
    print(product_id)
    print(product_quantity)
    print(estimated_date)

    body_request = {
        "items": [
            {
                "id": product_id,
                "quantity": product_quantity
            }
        ],
        "airport_id": airport_id,
        "estimated_date": estimated_date,

        "token": cart_token
    }

    item_group_path = 'api/v2/seller/userCart/itemGroup'
    item_group_response = json.loads(requests.post(url_partnership+item_group_path, json=body_request, headers=headers).text)

    print('\n111\n')
    print(item_group_response)
    print('\n111\n')

    return item_group_response



def open_cart(cart_token):
    cart_path = 'api/v2/seller/userCart?token=' + cart_token
    cart_response = json.loads(requests.get(url_partnership+cart_path, headers=headers).text)
    return cart_response


def confirm_cart(cart_token):
    confirm_cart_params = {
        'token': cart_token,
    }

    confirm_cart_path = 'api/v1/seller/UserCartRegisterOrder'
    confirm_cart_response = json.loads(requests.post(url_partnership+confirm_cart_path, params=confirm_cart_params, headers=headers).text)

    return confirm_cart_response


def register_customer(phone):
    body_request = {
        "phone": phone,
        "deviceInfo": {
            "geoAccuracyPermission": "",
            "ip_address": "",
            "geoAccuracyPermission": "",
            "instance_id": "",
            "ip_address": "",
            "os": "",
            "fcm_token": "",
            "os_version": "",
            "locale": "",
            "device_model": "",
            "geo_permission": "",
            "push_permission": "",
            "app_version": ""
        }
    }

    register_customer_path = 'api/v1/register'
    register_customer_response = json.loads(requests.post(url_mileonair+register_customer_path, json=body_request, headers=headers).text)
    return register_customer_response


def confirm_customer():
    body_request = {
        "code": "22222"
    }

    confirm_customer_path = 'api/v1/confirm'
    confirm_customer_response = json.loads(requests.post(url_mileonair+confirm_customer_path, json=body_request, headers=headers).text)
    customer_profile_token = confirm_customer_response['data']['token']
    return customer_profile_token


def login_customer(language_code, customer_profile_token):
    body_request = {
        {
            "token": customer_profile_token,
            "deviceInfo": {
                "geoAccuracyPermission": "",
                "ip_address": "",
                "geoAccuracyPermission": "",
                "instance_id": "",
                "ip_address": "",
                "os": "",
                "fcm_token": "",
                "os_version": "",
                "locale": "",
                "device_model": "",
                "geo_permission": "",
                "push_permission": "",
                "app_version": ""
            }
            # "locale": language_code
        }
    }

    login_customer_path = 'api/v1/login'
    login_customer_response = json.loads(requests.post(url_mileonair+login_customer_path, json=body_request, headers=headers).text)
    return login_customer_response


def get_customer_profile():
    customer_profile_path = 'api/v1/login'
    customer_profile_response = json.loads(requests.get(url_mileonair+customer_profile_path, headers=headers).text)
    return customer_profile_response


def get_customer_cart(cart_token):
    customer_cart_params = {
        'token': cart_token,
        'phone': phone
    }

    customer_cart_path = 'api/v1/seller/userCart'
    customer_cart_response = json.loads(requests.get(url_partnership+customer_cart_path, params=customer_cart_params, headers=headers).text)

    return customer_cart_response



def main():
    date_from, date_to = choose_dates()

    dates_dict={}
    dates_dict['date_from'] = date_from
    dates_dict['date_to'] = date_to

    print('\nFrom ->', dates_dict['date_from'], '\nTo ->', dates_dict['date_to'], '\n')

    cart_token = get_customer_cart_token()

    airports_dict = get_list_airports()

    airports_chooses = generate_flight(airports_dict)
    print (airports_chooses)

    for lang in language_code:
        print('\n\nLanguage ->', lang)

        for airport_id, estimated_date in zip(airports_chooses, dates_dict):
            print('\nAirport Code ->', airports_chooses[airport_id])

            categories_dict = get_list_categories(airports_chooses[airport_id], lang)
            print(categories_dict)

            for category_id in categories_dict:
                print('Category ID ->', category_id)

                products_dict = get_list_points_by_category(airports_chooses[airport_id], category_id, lang)

                if products_dict != {}:
                    product_id, product_quantity = choose_point(products_dict)

                    add_to_cart(airport_id, cart_token, product_id, product_quantity, dates_dict[estimated_date])

            cart_info = open_cart(cart_token)
            print(cart_info)
            # confirm_cart(cart_token)

            # register_customer()
            # customer_profile_token = confirm_customer()
            # login_customer(lang, customer_profile_token)

            # get_customer_profile()
            # get_customer_cart(cart_token)




    print('--- end ---')


if __name__ == '__main__':
    main()
