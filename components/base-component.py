from playwright.sync_api import Page, Locator

class BaseComponent:
    def __init__(self, page: Page, root_locator: Locator):
        self.page = page
        self.root_locator = root_locator

    def wait_for_element(self):
        self.root_locator.wait_for(state="visible")

    def is_visible(self)->bool:
        return self.root_locator.is_visible()