import requests
import pytest


class TestUserAuth:
    def test_user_auth(self):
        data = {
            'email': 'sodikmirzo@gmail.com',
            'password': '12345'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert "auth_sid" in response1.cookies, "Нет кукисов"
        assert "x-csrf-token" in response1.headers, "There is no x-csrf-token"
        assert "user_id" in response1.json(), "Нет поля user_id"

        auth_sid = response1.cookies.get('auth_sid')
        token = response1.headers.get('x-csrf-token')
        user_id_from_auth_method = response1.json().get('user_id')

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={
                'x-csrf-token': token,
                'cookie': 'auth_sid={}'.format(auth_sid)
            }
        )

        assert "user_id" in response2.json(), "Нет поля user_id"

        user_id_from_check_method = response2.json().get('user_id')

        assert user_id_from_auth_method == user_id_from_check_method, "Поля user_id не совпадают"

    exclude_params = [
        ("no_cookie"),
        ("no_token"),
    ]

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        data = {
            'email': 'sodikmirzo@gmail.com',
            'password': '12345'
        }

        response1 = requests.post('https://playground.learnqa.ru/api/user/login', data=data)

        assert "auth_sid" in response1.cookies, "Нет кукисов"
        assert "x-csrf-token" in response1.headers, "There is no x-csrf-token"
        assert "user_id" in response1.json(), "Нет поля user_id"

        auth_sid = response1.cookies.get('auth_sid')
        token = response1.headers.get('x-csrf-token')

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={
                    'x-csrf-token': token
                }
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={
                    "auth_sid": auth_sid
                }
            )

        assert "user_id" in response1.json(), "Нет поля user_id"

        user_id_from_check_method = response2.json().get('user_id')

        assert user_id_from_check_method == 0, f"User is authenticated, but should not be condition: {condition}"
