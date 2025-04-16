from .base_client import BaseAPIClient
from playwright.sync_api import APIResponse
import allure


class LoginClient(BaseAPIClient):
    LOGIN_ENDPOINT = "/login"

    def login(self):
        with allure.step("Send POST request to create a new user"):
            payload = {"email": "hello@gmail.com"}
        return self.request.post(f"{self.base_url}{self.LOGIN_ENDPOINT}", data=payload)
