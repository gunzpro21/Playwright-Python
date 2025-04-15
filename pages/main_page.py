from playwright.sync_api import Locator

from pages.base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.welcomelabel = page.locator("li:has(a i.fa-user)") # .shop-menu.pull-right .nav.navbar-nav>li:last-child >a


    # def get_welcomelabel_text(self) -> str:
    #     self.welcomelabel.wait_for(state="visible", timeout=10000)
    #     return self.welcomelabel.text_content().strip()

    def get_welcomelabel_locator(self) -> Locator: # return locator
        self.welcomelabel.wait_for(state="visible", timeout=5000)
        return self.welcomelabel # Return the locator.