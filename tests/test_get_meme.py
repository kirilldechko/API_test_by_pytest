import allure
from faker import Faker
from tests.test_data.bodies_for_tests import incorrect_token, incorrect_id

fake = Faker()
name = fake.name()
test_name = {"name": 'TEST_API_DKA3'}


@allure.feature("Get meme")
@allure.story("Positive tests")
@allure.title("Get meme by id")
def test_get_meme(check_token, create_new_meme, get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_id(create_new_meme, check_token)


@allure.feature("Get meme")
@allure.story("Positive tests")
@allure.title("Get all memes")
def test_get_all_meme(check_token, get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme(check_token)


@allure.feature("Get meme")
@allure.story("Negative tests")
@allure.title("Get meme by id, with incorrect token")
def test_get_meme_by_incorrect_token(check_token, create_new_meme, get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_incorrect_data(create_new_meme, incorrect_token)


@allure.feature("Get meme")
@allure.story("Negative tests")
@allure.title("Get meme by incorrect id")
def test_get_meme_by_incorrect_id(check_token, get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_incorrect_data(incorrect_id, check_token)


@allure.feature("Get meme")
@allure.story("Negative tests")
@allure.title("Get all memes by incorrect token")
def test_get_all_meme_by_incorrect_token(get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_incorrect_data(incorrect_token)
