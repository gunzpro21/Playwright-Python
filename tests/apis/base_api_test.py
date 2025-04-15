import allure
import json
from playwright.sync_api import expect, APIResponse
from utils.reporting import attach_response


class BaseAPITest:
    """Base class for API tests to handle common validation and reporting."""

    def validate_and_attach_response(self, response: APIResponse, expected_status: int = 200):
        """Validate response and attach it to Allure report."""
        with allure.step("Validate API response"):
            assert response.ok, f"API request failed with status {response.status}"
            try:
                expect(response).to_have_status(expected_status)
            except AttributeError:
                assert response.status == expected_status, f"Expected status {expected_status}"

            status_code = response.status
            response_body = response.json()
            attach_response(status_code, response_body, self.__class__.__name__)
            return response_body