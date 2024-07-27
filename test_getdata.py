
import requests

endpoint = 'https://dummyjson.com/users/1'


def get_data():
    response = requests.get(endpoint)
    response_data = response.json()
    print(response_data)
    print(f"status code: {response.status_code}")
    return response.status_code


def test_getdata():
    assert get_data() == 200
