import allure
import json
from playwright.sync_api import expect
from tests.apis.base_api_test import BaseAPITest
from tests.data_test.api_user_data import Person

@allure.title("Verify User Retrieval (GET)")
@allure.description("Tests the GET /users/2 endpoint.")
def test_get_user(user_client):
    with allure.step("Send GET request to User API"):
        response = user_client.get_user()

    response_body = BaseAPITest().validate_and_attach_response(response,200)

    with allure.step("Verify user data"):
        user_data = response_body["data"]
        assert user_data["email"] == "janet.weaver@reqres.in", "Email mismatch"
        assert user_data["first_name"] == "Janet", "First name mismatch"
        assert user_data["last_name"] == "Weaver", "Last name mismatch"

@allure.title("Verify User Creation (POST)")
@allure.description("Tests the POST /users endpoint to create a new user.")
def test_create_user(user_client, fake):
    person = Person(name=fake.name(), job=fake.job())

    with allure.step("Send CREATE request to ReqRes API"):
        response = user_client.create_user(person.name, person.job)
    response_body = BaseAPITest().validate_and_attach_response(response, 201)

    with allure.step("Verify created user data"):
        assert response_body["name"] == person.name, "Name mismatch" #user_name = response_body.get("name")
        assert response_body["job"] == person.job, "Job mismatch"
        assert "id" in response_body, "ID not returned"
        assert "createdAt" in response_body, "Creation timestamp missing"

    # pytest tests/apis/test_users.py tests/apis/test_login.py -v --alluredir=reports/allure-results
    # allure generate reports/allure-results -o reports/allure-report --clean
    # allure open reports/allure-report
