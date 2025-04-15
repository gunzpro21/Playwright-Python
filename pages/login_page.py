from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = page.locator("input[data-qa='login-email']")
        self.password_field = page.locator("input[data-qa='login-password']")
        self.login_button = page.locator("button[data-qa='login-button']")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()