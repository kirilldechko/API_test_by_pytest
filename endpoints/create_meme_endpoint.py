import random
import requests
import allure

from endpoints.parent_endpoint import ParentEndpoint


class CreateMeme(ParentEndpoint):
    response = None
    obj_json = None
    obj_id = None

    @allure.step('Create new meme.')
    def create_meme(self, body, token):
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={
                'Authorization': token
            }
        )
        self.check_status_200()
        self.obj_json = self.response.json()
        self.obj_id = self.obj_json['id']
        assert self.obj_json['text'] == body['text']
        print(self.obj_json['text'])
        return self.obj_id

    @allure.step('Create a new meme with invalid data.')
    def create_meme_invalid_data(self, body, token):
        random_key = random.choice(list(body.keys()))  # Получаем случайный ключ
        body.pop(random_key)  # Удаляем ключ из словаря
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={
                'Authorization': token
            }
        )
        print(self.response)
        self.check_status_400()
