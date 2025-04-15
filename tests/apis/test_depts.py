import allure
from .base_api_test import BaseAPITest

#TODO test file, it can not test anything
@allure.title("Verify Department API Data")
@allure.description("Tests the GET /unknown endpoint.")
def test_get_departments(dept_client):
    with allure.step("Send GET request to Department API"):
        response = dept_client.get_departments()

    response_body = BaseAPITest().validate_and_attach_response(response)

    with allure.step("Verify department data"):
        assert len(response_body["data"]) > 0, "No department data returned"
        assert response_body["data"][0]["id"] == 1, "First department ID mismatch"

        #pytest tests/api/test_users.py tests/api/test_depts.py
        # allure generate reports/allure-results -o reports/allure-report --clean
        # allure open reports/allure-report