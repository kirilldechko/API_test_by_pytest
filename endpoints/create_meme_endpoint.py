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
        if self.check_status_200():
            self.obj_json = self.response.json()
            self.obj_id = self.obj_json['id']
            return self.obj_id
        else:
            print(f"Incorrect request, {self.response}")

    @allure.step('Create a new meme with no required fields.')
    def create_meme_req_field(self, body, token):
        random_key = random.choice(list(body.keys()))  # Получаем случайный ключ
        body.pop(random_key)  # Удаляем ключ из словаря
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={
                'Authorization': token
            }
        )
        print(f"Test body is: {body}")
        print(f"Can't create a meme, no '{random_key}' key in test body'.")
        self.check_status_200()

    @allure.step('Create a new meme with no required fields.')
    def create_meme_incorrect_data(self, body, token):
        random_key = random.choice(list(body.keys()))  # Получаем случайный ключ
        body.pop(random_key)  # Удаляем ключ из словаря
        self.response = requests.post(
            f'{self.url}/meme',
            json=body,
            headers={
                'Authorization': token
            }
        )
        self.check_status_200()
