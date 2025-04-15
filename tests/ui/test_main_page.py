import allure
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import Config

#Error page - no need
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    # Attach screenshot after every test (pass or fail)
    screenshot = page.screenshot(path="screenshot.png", full_page=True)
    allure.attach(
        screenshot,
        name="Test End Screenshot",
        attachment_type=allure.attachment_type.PNG
    )
    page.close()

@allure.title("Verify Successful Login")
@allure.description("Tests login functionality and verifies welcome text.")
def test_valid_login(page: Page):
    login_page = LoginPage(page)
    main_page = MainPage(page)

    with allure.step("Navigate to login page"):
        login_page.navigate(Config.BASE_URL)

    with allure.step("Perform login with credentials"):
        login_page.login(Config.USERNAME, Config.PASSWORD)

    with allure.step("Verify welcome label text"):
        #welcome_text = main_page.get_welcomelabel_locator()
        try:
            expect(main_page.get_welcomelabel_locator()).to_have_text("Logged 1in as Steward")
        except AssertionError:
            allure.attach(
                page.screenshot(),
                name="Login Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            raise
        #pytest tests/ui/test_main_page.py -v --alluredir=reports/allure-results
        #allure generate reports/allure-results -o reports/allure-report --clean
        #allure open reports/allure-report
