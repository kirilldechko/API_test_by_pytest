import allure
from test_data.bodies_for_tests import test_body, body_meme, incorrect_boby, incorrect_body_meme
import pytest


@allure.feature("Create memes")
@allure.story("Positive tests")
@allure.title("Create meme with valid data")
@pytest.mark.parametrize("test_body", test_body)
@pytest.mark.regression
def test_create_new_meme(test_body, check_token, create_meme_endpoint, delete_meme_endpoint):
    new_meme = create_meme_endpoint.create_meme(test_body, check_token)
    create_meme_endpoint.check_obj_text(test_body["text"])
    delete_meme_endpoint.delete_meme(new_meme, check_token)

@pytest.mark.regression
@allure.feature("Create memes")
@allure.story("Negative tests")
@allure.title("Create meme without required fields")
@pytest.mark.parametrize("test_body", incorrect_boby)
def test_create_new_meme_without_req_fild(test_body, check_token, create_meme_endpoint):
    create_meme_endpoint.create_meme_invalid_data(test_body, check_token)

@pytest.mark.regression
@allure.feature("Create memes")
@allure.story("Negative tests")
@allure.title("Create meme with incorrect data (no key)")
def test_create_new_meme_with_incorrect_data(check_token, create_meme_endpoint):
    create_meme_endpoint.create_meme_invalid_data(body_meme, check_token)
