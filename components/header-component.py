from playwright.sync_api import Playwright

class HeaderComponent(BaseComponent):
    def __init__(self, page: Playwright):
        self.page = page
