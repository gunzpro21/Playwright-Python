from abc import ABC
from playwright.sync_api import APIRequestContext, APIResponse
from config.settings import Settings
import allure
import json
from utils.reporting import attach_response
from playwright.sync_api import expect

class BaseAPIClient:
    def __init__(self, request_context: APIRequestContext):
        self.request = request_context
        self.base_url = Settings.API_BASE_URL

    def validate_response(self, response: APIResponse, expected_status: int = 200, name: str = "API Response") -> dict:
        with allure.step(f"Validate {name} response"):
            assert response.ok, f"API request failed with status {response.status}"
            try:
                expect(response).to_have_status(expected_status)
            except AttributeError:
                assert response.status == expected_status, f"Expected status {expected_status}"
            status_code = response.status
            response_body = response.json
            attach_response(status_code, response_body, name)
            return response_body