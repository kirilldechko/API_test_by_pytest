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
        self.check_status_200()
        self.obj_json = self.response.json()
        assert self.obj_json is not None, "Response have no memes"
        return self.obj_json

    @allure.step('Get meme by id.')
    def get_meme_by_id(self, obj_id, token):
        self.response = requests.get(
            f'{self.url}/meme/{obj_id}',
            headers={
                'Authorization': token
            }
        )
        self.check_status_200()
        self.obj_json = self.response.json()
        assert self.obj_json['id'] == obj_id, f"No meme with id {obj_id}"
        return self.obj_json

    @allure.step('Get meme by incorrect data.')
    def get_meme_by_incorrect_data(self, obj_id=None, token=None):
        self.response = requests.get(
            f'{self.url}/meme/{obj_id}',
            headers={
                'Authorization': token
            }
        )
        self.check_status_non_200()
        return self.response
