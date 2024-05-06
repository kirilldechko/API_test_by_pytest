import requests
import allure
from endpoints.parent_endpoint import ParentEndpoint


class AuthorizePost(ParentEndpoint):
    obj_json = None
    response = None
    token = None
    user = None

    @allure.step('Авторизация пользователя и получение токена.')
    def authorize_post(self, name):
        self.response = requests.post(
            f"{self.url}/authorize",
            json=name
        )
        if self.response.status_code == 400:
            print(f"Incorrect data: {name}")
        else:
            self.obj_json = self.response.json()
            self.token = self.obj_json['token']
            self.user = self.obj_json['user']
            assert self.response.status_code == 200
            assert self.user == name['name']
            return self.token

    @allure.step('Проверка токена.')
    def check_token_by_token(self, token):
        self.response = requests.get(
            f"{self.url}/authorize/{token}"
        )
        if self.response.status_code != 200:
            print("Your token wasn't created, you used incorrect data.")
        else:
            assert self.response.status_code == 200
