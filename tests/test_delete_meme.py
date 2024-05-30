import allure
from test_data.bodies_for_tests import correct_names


@allure.feature("Delete meme")
@allure.story("Positive tests")
@allure.title("Delete meme by id")
def test_delete_meme(check_token, delete_meme_endpoint, create_new_meme):
    delete_meme_endpoint.delete_meme(create_new_meme, check_token)


@allure.feature("Delete meme")
@allure.story("Negative tests")
@allure.title("Delete meme with incorrect token")
def test_delete_meme_incorrect_token(create_new_meme, authorize_endpoint, delete_meme_endpoint):
    incorrect_token = authorize_endpoint.authorize_post(correct_names[4])
    delete_meme_endpoint.delete_meme(create_new_meme, incorrect_token)
