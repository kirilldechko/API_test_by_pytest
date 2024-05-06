import requests
import allure
from endpoints.parent_endpoint import ParentEndpoint


class GetAllMeme(ParentEndpoint):
    response = None
    obj_json = None
    obj_list = None

    @allure.step('Get all memes.')
    def get_all_meme(self, token):
        self.response = requests.get(
            f'{self.url}/meme',
            headers={
                'Authorization': token
            }
        )
        if self.response.status_code == 401:
            print("Incorrect token")
        else:
            assert self.response.status_code == 200
            self.obj_json = self.response.json()
            return self.obj_json

    @allure.step('Get meme by id.')
    def get_meme_by_id(self, obj_id, token):
        self.response = requests.get(
            f'{self.url}/meme/{obj_id}',
            headers={
                'Authorization': token
            }
        )
        if self.response.status_code == 401:
            print("Incorrect token")
        elif self.response.status_code == 200:
            self.obj_json = self.response.json()
        else:
            print("Incorrect id")
        return self.obj_json
