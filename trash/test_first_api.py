import pytest
import requests


class TestFirstAPI:
    names = [
        ("John"),
        ("Jane"),
        ("Jack"),
        (""),
    ]

    @pytest.mark.parametrize("name", names)
    def test_first_api(self, name):
        url = 'https://playground.learnqa.ru/api/hello'
        # name = 'Sodikmirzo'
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dick = response.json()
        assert "answer" in response_dick, "There is no field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"
        actual_response_text = response_dick['answer']
        assert actual_response_text == expected_response_text, "Actual response text is not equal to expected"
