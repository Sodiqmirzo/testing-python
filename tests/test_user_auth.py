import requests
import pytest
from lib.base_case import BaseCase


class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token"),
    ]

    def setup(self):
        data = {
            'email': 'sodikmirzo@gmail.com',
            'password': '12345'
        }
        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_from_auth_method = self.get_json_value(response1, 'user_id')

    def test_user_auth(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={
                'x-csrf-token': self.token,
                'cookie': 'auth_sid={}'.format(self.auth_sid)
            }
        )

        assert "user_id" in response2.json(), "Нет поля user_id"

        user_id_from_check_method = response2.json().get('user_id')

        assert self.user_id_from_auth_method == user_id_from_check_method, "Поля user_id не совпадают"

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={
                    'x-csrf-token': self.token
                }
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={
                    "auth_sid": self.auth_sid
                }
            )

        assert "user_id" in self.response1.json(), "Нет поля user_id"

        user_id_from_check_method = response2.json().get('user_id')

        assert user_id_from_check_method == 0, f"User is authenticated, but should not be condition: {condition}"
