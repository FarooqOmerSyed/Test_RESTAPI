import requests

endpoint = 'https://dummyjson.com/users/add'


def post_data():
    payload = {'username': 'loverboy', 'password': 'iluvu143'}
    response = requests.post(endpoint, json=payload)
    print(response.status_code)
    print(response.text)
    return response.status_code


def test_post_data():
    assert post_data() == 201

