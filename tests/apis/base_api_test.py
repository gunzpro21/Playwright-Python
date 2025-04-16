import allure
from typing import Any, Dict, List, Union
from playwright.sync_api import expect, APIResponse
from utils.reporting import attach_response


class BaseAPITest:
    """Base class for API tests to handle common validation and reporting."""

    # tomorrow try new code on Copilot
    def validate_and_attach_response(
            self, response: APIResponse, expected_status: Union[int, List[int]]
    ) -> Dict[str, Any]:
        """
        Validates the API response and attaches it to an Allure report.
        Supports single or multiple expected status codes.
        """
        with allure.step(f"Validate API response for expected status {expected_status}"):
            self._validate_status_code(response, expected_status)
            return self._attach_response_to_report(response)

    def _validate_status_code(self, response: APIResponse, expected_status: Union[int, List[int]]) -> None:
        """
        Validates the response status code against one or more expected status codes.
        """
        status = response.status
        with allure.step(f"Response Status Code: {status}"):
            # Handle multiple expected status codes
            if isinstance(expected_status, list):
                assert status in expected_status, (
                    f"Expected one of {expected_status}, but got {status}"
                )
            else:
                assert status == expected_status, f"Expected {expected_status}, but got {status}"

    def _attach_response_to_report(self, response: APIResponse) -> Dict[str, Any]:
        try:
            status_code = response.status
            response_body = response.json()
            with allure.step(f"Attaching response to report: Status: {status_code}, Body: {response_body}"):
                attach_response(status_code, response_body, self.__class__.__name__)
                return response_body
        except Exception as e:
            with allure.step(f"Failed to attach response or parse JSON: {str(e)}"):
                raise ValueError("Invalid response or JSON parsing failed") from e