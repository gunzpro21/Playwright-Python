import allure
from playwright.sync_api import sync_playwright

@allure.title("Example Test with Screenshot")
def test_google():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        with allure.step("Navigate to website"):
            page.goto("https://www.google.com")
        with allure.step("Verify title"):
            assert "Google failed test" in page.title()
        browser.close ()
        #thang qq html khong add screenshot duoc. choi voi allure thoi
        # pytest tests/ --alluredir=allure-results
        # allure serve allure-results