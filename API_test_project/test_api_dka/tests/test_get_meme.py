import allure
from faker import Faker
from bodies_for_tests import body_meme, incorrect_token, incorrect_id

fake = Faker()
name = fake.name()
test_name = {"name": 'TEST_API_DKA3'}


@allure.feature("Get meme")
@allure.story("Get meme by id")
@allure.title("Get meme")
def test_get_meme(check_token, create_new_meme, get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_id(create_new_meme, check_token)


@allure.feature("Get meme")
@allure.story("Get meme by by incorrect token")
@allure.title("Get meme")
def test_get_meme_by_incorrect_token(check_token, create_new_meme, get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_id(create_new_meme, incorrect_token)


@allure.feature("Get meme")
@allure.story("Get meme by by incorrect id")
@allure.title("Get meme")
def test_get_meme_by_incorrect_id(check_token, get_all_meme_endpoint):
    get_all_meme_endpoint.get_meme_by_id(incorrect_id, check_token)


@allure.feature("Get meme")
@allure.story("Get all memes")
@allure.title("Get all memes")
def test_get_all_meme(check_token, get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme(check_token)


@allure.feature("Get meme")
@allure.story("Get meme by by incorrect token")
@allure.title("Get all memes")
def test_get_all_meme_by_incorrect_token(get_all_meme_endpoint):
    get_all_meme_endpoint.get_all_meme(incorrect_token)
