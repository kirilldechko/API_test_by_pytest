import pytest
from endpoints.authorize_endpoint import AuthorizePost
from endpoints.create_meme_endpoint import CreateMeme
from endpoints.delete_meme_endpoint import DeleteMeme
from endpoints.change_meme_put_endpoint import ChangeMeme
from endpoints.check_token_endpoint import CheckToken
from endpoints.get_meme_endpoint import GetAllMeme

from faker import Faker
import random

fake = Faker()
name = fake.name()
test_name = {"name": 'TEST_API_DKA3'}


@pytest.fixture()
def authorize_endpoint():
    return AuthorizePost()


@pytest.fixture()
def check_token_endpoint():
    return CheckToken()


@pytest.fixture()
def get_all_meme_endpoint():
    return GetAllMeme()


@pytest.fixture()
def create_meme_endpoint():
    return CreateMeme()


@pytest.fixture()
def change_meme_put_endpoint():
    return ChangeMeme()


@pytest.fixture()
def delete_meme_endpoint():
    return DeleteMeme()


@pytest.fixture()
def check_token(authorize_endpoint):
    token = authorize_endpoint.authorize_post(test_name)
    authorize_endpoint.check_token_by_token(token)
    return token


@pytest.fixture()
def create_new_meme(create_meme_endpoint, delete_meme_endpoint, check_token):
    body_meme = {"text": f"Вечер пятницы, утро субботы {random.randint(0, 10)}",
                 "url": "https://sun9-13.userapi.com/impg/7baXWqxpMPVvxz7rmJJnV8cFs6yiO1PFsGsXRQ/aZHzlt82_fU."
                        "jpg?size=929x905&quality=96&sign=5b9cf9b9b3e0f46cd9ace6b023249eef&c_uniq_tag=hnaqx8M"
                        "-kYqa_hhwuzvy8dcNsizvftoC_ET1PIvZH94&type=album",
                 "tags": ["friday", "relax", "Anthony Edward 'Tony' Stark"],
                 "info": {"person": f"{name}"}}
    new_meme = create_meme_endpoint.create_meme(body_meme, check_token)
    create_meme_endpoint.check_obj_text(body_meme["text"])
    yield new_meme
    delete_meme_endpoint.delete_meme(new_meme, check_token)



