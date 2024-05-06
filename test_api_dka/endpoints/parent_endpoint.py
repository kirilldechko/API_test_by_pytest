import allure
import requests


class ParentEndpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    obj_json = None

    @allure.step('Check meme text')
    def check_obj_text(self, text):
        if self.response.status_code != 200:
            print(f"Object with data: {text} wasn't created.")
        else:
            assert self.obj_json['text'] == text, f"Object with data: {text} wasn't created'"
