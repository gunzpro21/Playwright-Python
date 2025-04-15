from .base_client import BaseAPIClient
from playwright.sync_api import APIResponse
import allure

class UserClient(BaseAPIClient):
    USER_ENDPOINT = "/users/2"      # For GET specific user
    CREATE_USER_ENDPOINT = "/users" # For POST

    def get_user(self) -> APIResponse:
        with allure.step("Send GET request to fetch user"):
            return self.request.get(f"{self.base_url}{self.USER_ENDPOINT}")

    # def get_validated_user(self) -> dict:
    #     response = self.get_user()
    #     return self.validate_response(response, name="User API Response")

    def create_user(self, name: str, job: str) -> APIResponse:
        with allure.step("Send POST request to create a new user"):
            payload = {"name": name, "job": job}
            return self.request.post(
                f"{self.base_url}{self.CREATE_USER_ENDPOINT}",
                data=payload
            )

    # def create_validated_user(self, name: str, job: str) -> dict:
    #     response = self.create_user(name, job)
    #     return self.validate_response(response, expected_status=201, name="User Creation Response")