import requests
import allure
from endpoints.parent_endpoint import ParentEndpoint


class CheckToken(ParentEndpoint):
    token = None
    obj_json = None
    response = None

    @allure.step('Проверка токена.')
    def check_token(self, token):
        self.response = requests.get(
            f"{self.url}/authorize/{token}"
        )
        self.check_status_200()