import allure
from playwright.sync_api import Page


@allure.title("Verify Successful Login")
@allure.description("Tests the login functionality on automationexercise.com")
def test_login(page: Page, ui_base_url: str):
    # Navigate to the base URL
    with allure.step("Go to URL"):
        page.goto(ui_base_url)

    with allure.step("Click on 'Signup / Login' link"):
        page.click("a[href='/login']")

    with allure.step("Enter login credentials"):
        page.fill("input[data-qa='login-email']", "testuser@example.com")
        page.fill("input[data-qa='login-password']", "password123")

    with allure.step("Click 'Login' button"):
        page.click("button[data-qa='login-button']")

    with allure.step("Verify login success"):
        # Check for a logged-in user element (e.g., username in navbar)
        assert page.is_visible("a[href='/logout']"), "Logout link not visible, login failed"

        #pytest tests/ui/test_login_automation.py -v --alluredir=reports/allure-results