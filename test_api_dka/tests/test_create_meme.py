import allure
from tests.test_data.bodies_for_tests import test_body, body_meme
import pytest


@allure.feature("Create memes")
@allure.story("Create new meme")
@allure.title("Create meme with valid data")
@pytest.mark.parametrize("test_body", test_body)
def test_create_new_meme(test_body, check_token, create_meme_endpoint, delete_meme_endpoint):
    new_meme = create_meme_endpoint.create_meme(test_body, check_token)
    create_meme_endpoint.check_obj_text(test_body["text"])
    delete_meme_endpoint.delete_meme(new_meme, check_token)


@allure.feature("Create memes")
@allure.story("Create meme without required fields")
@allure.title("Create meme without required fields")
@pytest.mark.parametrize("test_body", test_body)
def test_create_new_meme_without_req_fild(test_body, check_token, create_meme_endpoint):
    create_meme_endpoint.create_meme_req_field(test_body, check_token)


@allure.feature("Create memes")
@allure.story("Create meme without the required fields")
@allure.title("Create meme without the required fields_2")
def test_create_new_meme_without_requirement_fild(check_token, create_meme_endpoint):
    create_meme_endpoint.create_meme_req_field(body_meme, check_token)
