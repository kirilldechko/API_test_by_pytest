import allure
import pytest

from test_data.bodies_for_tests import correct_names

@pytest.mark.regression
@allure.feature("Change meme")
@allure.story("Positive tests")
@allure.title("Change meme by id")
def test_change_meme_put(check_token, create_new_meme, change_meme_put_endpoint):
    change_meme_put_endpoint.change_meme(create_new_meme, check_token)


@pytest.mark.regression
@allure.feature("Change meme")
@allure.story("Negative tests")
@allure.title("Change meme with incorrect token")
def test_change_meme_incorrect_token(create_new_meme, change_meme_put_endpoint, authorize_endpoint):
    incorrect_token = authorize_endpoint.authorize_post(correct_names[4])
    change_meme_put_endpoint.change_meme_with_incorrect_data(create_new_meme, incorrect_token)
