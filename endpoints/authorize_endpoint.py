import requests
import allure
from endpoints.parent_endpoint import ParentEndpoint


class AuthorizePost(ParentEndpoint):
    obj_json = None
    response = None
    token = None
    user = None

    @allure.step('User authorize.')
    def authorize_post(self, name):
        self.response = requests.post(f"{self.url}/authorize", json=name)
        self.check_status_200()
        self.obj_json = self.response.json()
        assert self.obj_json['user'] == name['name']
        return self.obj_json['token']

    @allure.step('User authorize with incorrect name.')
    def authorize_incorrect_name(self, name):
        self.response = requests.post(f"{self.url}/authorize", json=name)
        self.check_status_400()

    @allure.step('Check correct token.')
    def check_token_by_token(self, token):
        self.response = requests.get(
            f"{self.url}/authorize/{token}"
        )
        self.check_status_200()

    @allure.step('Check token, used incorrect token.')
    def check_unexpected_token_by_token(self, token):
        self.response = requests.get(
            f"{self.url}/authorize/{token}"
        )
        print(self.response)
        self.check_status_400()
