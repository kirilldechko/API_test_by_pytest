import requests
import allure

from endpoints.parent_endpoint import ParentEndpoint


class DeleteMeme(ParentEndpoint):
    obj_json = None
    response = None

    @allure.step('Delete meme.')
    def delete_meme(self, meme_id, token):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers={
                'Authorization': token
            }
        )
        self.check_status_200()
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}")
        # self.check_status_200()
