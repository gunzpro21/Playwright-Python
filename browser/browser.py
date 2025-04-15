from playwright.sync_api import sync_playwright, Playwright, Browser as PlaywrightBrowser, Page
from typing import Optional

class Browser:
    def __init__(self, playwright: Playwright, browser_type: str, headless: bool = True):
        self.playwright = playwright
        self.browser_type = browser_type.lower()
        self.headless = headless
        self._browser: Optional[PlaywrightBrowser] = None
        self._page: Optional[Page] = None

    def start(self) -> 'Browser':
        if self._browser:
            return self
        if self.browser_type == "chromium":
            self._browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self._browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self._browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        self._page = self._browser.new_page()
        return self

    def page(self) -> Page:
        if not self._page:
            raise RuntimeError("Browser not started. Call start() first.")
        return self._page

    def close(self) -> None:
        if self._page:
            self._page.close()
            self._page = None
        if self._browser:
            self._browser.close()
            self._browser = None

    def __enter__(self) -> 'Browser':
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()