import allure
import pytest
from test_data.bodies_for_tests import correct_names, incorrect_names


@allure.feature("Authorize")
@allure.story("Authorize")
@allure.title("Authorize with correct names")
@pytest.mark.parametrize("name", correct_names)
def test_authorization_with_correct_name(name, authorize_endpoint):
    authorize_endpoint.authorize_post(name)


@allure.feature("Authorize")
@allure.story("Authorize")
@allure.title("Authorize with incorrect names")
@pytest.mark.parametrize("name", incorrect_names)
def test_authorization_with_incorrect_name(name, authorize_endpoint):
    authorize_endpoint.authorize_incorrect_name(name)


@allure.feature("Authorize")
@allure.story("Authorize")
@allure.title("Authorize with correct token")
@pytest.mark.parametrize("name", correct_names)
def test_authorization_with_correct_token(name, authorize_endpoint):
    token = authorize_endpoint.authorize_post(name)
    authorize_endpoint.check_token_by_token(token)


@allure.feature("Authorize")
@allure.story("Authorize")
@allure.title("Authorize with incorrect token")
@pytest.mark.parametrize("name", incorrect_names)
def test_authorization_with_incorrect_token(name, authorize_endpoint):
    token = authorize_endpoint.authorize_incorrect_name(name)
    authorize_endpoint.check_unexpected_token_by_token(token)
