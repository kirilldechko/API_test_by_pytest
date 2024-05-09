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
        if self.check_status_200():
            self.obj_json = self.response.json()
            return self.obj_json['token']

    @allure.step('Check token.')
    def check_token_by_token(self, token):
        self.response = requests.get(
            f"{self.url}/authorize/{token}"
        )
        self.check_status_200()
