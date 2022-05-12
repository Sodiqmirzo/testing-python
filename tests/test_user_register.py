import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserRegister(BaseCase):
    def test_create_user_with_existing_email(self):
        email = 'sodikmirzo@gmail.com'
        data = {
            'password': '12345',
            'username': 'test_user',
            'firstName': 'test',
            'lastName': 'user',
            'email': email
        }

        response = requests.post('https://playground.learnqa.ru/api/user/', data=data)

        print(f"{response.status_code=}")
        print(f"{response.content=}")

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode(
            "utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"
