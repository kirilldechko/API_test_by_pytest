import requests
import allure
import random
from endpoints.parent_endpoint import ParentEndpoint
from faker import Faker

fake = Faker()
name = fake.name()


class ChangeMeme(ParentEndpoint):
    response = None
    obj_json = None
    obj_text = None

    @allure.step('Change meme.')
    def change_meme(self, obj_id, token):
        self.response = requests.put(
            f'{self.url}/meme/{obj_id}',
            json={
                "id": obj_id,
                "text": f"Вечер пятницы, утро субботы {random.randint(20, 30)}",
                "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
                       "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
                       "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
                "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
                "info": {"person": f"{name}"}
            },
            headers={
                'Authorization': token
            }
        )
        if self.check_status_200():
            self.obj_json = self.response.json()
            self.obj_text = self.obj_json["text"]
            return self.obj_text
        else:
            print(f"Incorrect request, {self.response}")
