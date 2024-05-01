import allure
from bodies_for_tests import test_names, body_meme


@allure.feature("Delete meme")
@allure.story("Delete meme by id")
@allure.title("Delete meme")
def test_delete_meme(check_token, delete_meme_endpoint, create_new_meme):
    delete_meme_endpoint.delete_meme(create_new_meme, check_token)


@allure.feature("Delete meme")
@allure.story("Delete meme with incorrect token")
@allure.title("Delete meme")
def test_delete_meme_incorrect_token(check_token, create_new_meme, authorize_endpoint, delete_meme_endpoint):
    incorrect_token = authorize_endpoint.authorize_post(test_names[4])
    delete_meme_endpoint.delete_meme(create_new_meme, incorrect_token)
