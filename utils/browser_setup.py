from playwright.sync_api import sync_playwright
from config.config_reader import ConfigReader

class BrowserSetup:
    # new
    def __init__(self):
        self.browser = None
        self.config = ConfigReader()
        self.playwright = sync_playwright().start()

    def launch(self):
        browser= self.config.get("browser", "chromium")
        headless = self.config.get("headless", True)

        if browser == "chromium":
            return self.playwright.chromium.launch(headless=headless)
        elif browser == "firefox":
            return self.playwright.firefox.launch(headless=headless)
        elif browser == "webkit":
            return self.playwright.webkit.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
    # new end

    # def __new__(cls):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #         cls._instance.playwright = sync_playwright().start()
    #         cls._instance.browser = cls._instance.playwright.chromium.launch(headless=False)
    #     return cls._instance

    def get_browser(self):
        return self.browser

    def close(self):
        self.browser.close()
        self.playwright.stop()