import requests
from json.decoder import JSONDecodeError


def create_user(payload):
    print("Creating user...")
    print(payload)
    url = 'https://playground.learnqa.ru/api/user/'
    response = requests.post(url, data=payload)
    return response.json()


print(create_user({
    'username': 'sodikmirzo',
    'firstName': 'sodikmirzo',
    'lastName': 'sodikmirzo',
    'email': 'sodikmirzo1@gmail.com',
    'password': '12345'
}))

# payload = {'name': 'John', 'age': '27'}
# response = requests.get('https://playground.learnqa.ru/api/hello', params=payload)
# print(response.url)
# print(response.json())
# print(response.text)


# response = requests.get('https://playground.learnqa.ru/api/get_text')
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print('Не удалось получить данные в виде JSON')
