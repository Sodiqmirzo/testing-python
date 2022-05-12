import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):
        response = requests.get('https://playground.learnqa.ru/api/user/34956')
        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_key(response, 'email')
        Assertions.assert_json_has_not_key(response, 'firstName')
        Assertions.assert_json_has_not_key(response, 'lastName')
