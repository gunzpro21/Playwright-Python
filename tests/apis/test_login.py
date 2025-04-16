import allure
from tests.apis.base_api_test import BaseAPITest


@allure.title("Verify user login unsuccessfully")
@allure.description("Tests the GET /unknown endpoint.")
def test_login_api(login_client):
    with allure.step("Send POST request to login API"):
        response = login_client.login()
        response_body = BaseAPITest().validate_and_attach_response(response, 400)

    with allure.step("Verify login failed respond"):
        assert response_body["error"] == "Missing password", "Missing password"

        # pytest tests/apis/test_users.py tests/apis/test_login.py -v --alluredir=reports/allure-results
        # allure generate reports/allure-results -o reports/allure-report --clean
        # allure open reports/allure-report
