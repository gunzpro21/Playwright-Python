import allure
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.main_page import MainPage

@allure.title("Verify Successful Login")
@allure.description("Tests login functionality and verifies welcome text.")
def test_valid_login(page: Page, ui_base_url: str, user_name: str, password : str):
    login_page = LoginPage(page)
    main_page = MainPage(page)

    with allure.step("Navigate to login page"):
        login_page.navigate(ui_base_url+"/login")

    with allure.step("Perform login with credentials"):
        login_page.login(user_name, password)

    with allure.step("Verify welcome label text"): #Issue can not print report !!!
        expect(main_page.get_welcomelabel_locator()).to_have_text("Logged 1in as Steward")

    # pytest tests/ui/test_complete_guide.py -v --alluredir=reports/allure-results