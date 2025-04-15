import allure
import pytest
from playwright.sync_api import sync_playwright, Playwright, Page
from browser.browser import Browser
from browser.config_reader import ConfigReader


@pytest.fixture(scope="session")
def playwright() -> Playwright:
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright: Playwright) -> Browser:
    config = ConfigReader()
    browser_type = config.get_browser_type()
    headless = config.get_headless()
    browser = Browser(playwright, browser_type, headless)
    yield browser.start()
    browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    return browser.page()

@pytest.fixture(scope="function")
def ui_base_url() -> str:
    return ConfigReader.get_ui_base_url()

@pytest.fixture(scope="function")
def user_name() -> str:
    return ConfigReader.get_user_name()

@pytest.fixture(scope="function")
def password() -> str:
    return ConfigReader.get_password()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot = page.screenshot(full_page=True, type="png")
            allure.attach(
                screenshot,
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
