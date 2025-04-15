import allure
import pytest
from playwright.sync_api import expect, APIRequestContext
import json


@pytest.fixture
def api_request(playwright):
    # Create a new API request context
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@allure.title("Verify ReqRes API User Data")
@allure.description("Tests the GET /api/users/2 endpoint and attaches the response.")
def test_api_get_user(api_request: APIRequestContext):  # Use custom fixture
    # Debug: Print the type to confirm
    print(f"Request type: {type(api_request)}")

    # Define the real API endpoint
    api_url = "https://reqres.in/api/users/2"

    with allure.step("Send GET request to ReqRes API"):
        response = api_request.get(api_url)

    with allure.step("Validate API response"):
        assert response.ok, f"API request failed with status {response.status}"
        # Use expect if to_have_status is supported; otherwise, use assert
        try:
            expect(response).to_have_status(200)  # Preferred if available
        except AttributeError:
            assert response.status == 200, "Expected status 200"  # Fallback

        status_code = response.status
        response_body = response.json()
        combined_response = {
            "status_code": status_code,
            "response_body": response_body
        }
        response_text = json.dumps(combined_response, indent=2)
        allure.attach(
            response_text,
            name="API Response with Status",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Verify response data"):
        user_data = response_body["data"]
        assert user_data["email"] == "janet.weaver@reqres.in", "Email mismatch"
        assert user_data["first_name"] == "Janet", "First name mismatch"
        assert user_data["last_name"] == "Weaver", "Last name mismatch"
        # pytest tests/test_api.py -v --alluredir=reports/allure-results
        # pytest tests/test_main_page.py tests/test_api.py -v --alluredir=reports/allure-results
        # tomorrow try grob api


@allure.title("Verify Create API User Data")
@allure.description("Tests the create /api/users endpoint and attaches the response.")
def test_api_create_user(api_request: APIRequestContext):  # Use custom fixture
    # Debug: Print the type to confirm
    print(f"Request type: {type(api_request)}")

    # Define the real API endpoint
    api_url = "https://reqres.in/api/users"

    data = {
        "name": "Dwayne",
        "job": "Johnson",
    }

    with allure.step("Send CREATE request to ReqRes API"):
        response = api_request.post(api_url, data=data)

    with allure.step("Validate API response"):
        assert response.ok, f"API request failed with status {response.status}"
        # Use expect if to_have_status is supported; otherwise, use assert
        try:
            expect(response).to_have_status(201)  # Preferred if available
        except AttributeError:
            assert response.status == 201, "Expected status 201"  # Fallback

        status_code = response.status
        response_body = response.json()
        combined_response = {
            "status_code": status_code,
            "response_body": response_body
        }
        response_text = json.dumps(combined_response, indent=2)
        allure.attach(
            response_text,
            name="API Response with Status",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Verify response data"):
        user_name = response_body.get("name")
        user_job = response_body.get("job")

        assert user_name == "Dwayne", "First name mismatch"
        assert user_job == "Johnson", "Job mismatch"
    #improve the product structure and run again