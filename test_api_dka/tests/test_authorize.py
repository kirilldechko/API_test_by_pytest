import allure
import pytest
from test_data.bodies_for_tests import test_names


@allure.feature("Authorize")
@allure.story("Authorize")
@allure.title("Authorize with different names")
@pytest.mark.parametrize("name", test_names)
def test_authorization_with_random_name(name, authorize_endpoint):
    obj_id = authorize_endpoint.authorize_post(name)
    authorize_endpoint.check_token_by_token(obj_id)
