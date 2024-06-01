import allure
import requests


class ParentEndpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    obj_json = None

    @allure.step('Check meme text')
    def check_obj_text(self, text):
        assert self.obj_json['text'] == text, f"Object with data: {text} wasn't created'"

    @allure.step('Check request status code 200.')
    def check_status_200(self):
        assert self.response.status_code == 200, "Incorrect status code, expect 200, check request data"

    @allure.step('Check request status code, 4__.')
    def check_status_400(self):
        assert self.response.status_code in [400, 401, 403, 404,], "ERROR! Unexpected status code"

