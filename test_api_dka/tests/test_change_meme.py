import allure
from tests.test_data.bodies_for_tests import test_names


@allure.feature("Change meme")
@allure.story("Change meme by id")
@allure.title("Change meme")
def test_change_meme_put(check_token, create_new_meme, change_meme_put_endpoint):
    changed_meme = change_meme_put_endpoint.change_meme(create_new_meme, check_token)
    change_meme_put_endpoint.check_obj_text(changed_meme)


@allure.feature("Change meme")
@allure.story("Change meme with incorrect token")
@allure.title("Change meme")
def test_change_meme_incorrect_token(create_new_meme, change_meme_put_endpoint, authorize_endpoint):
    incorrect_token = authorize_endpoint.authorize_post(test_names[4])
    change_meme_put_endpoint.change_meme(create_new_meme, incorrect_token)
