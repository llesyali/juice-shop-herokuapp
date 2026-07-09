from playwright.sync_api import Playwright

class HeaderComponent:
    def __init__(self, page: Playwright):
        self.page = page
