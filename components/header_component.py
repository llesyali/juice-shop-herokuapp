from playwright.sync_api import Locator, Page
from components.base_component import BaseComponent

class HeaderComponent(BaseComponent):
    def __init__(self, page: Page, root_locator: Locator):
        super().__init__(page, root_locator)

        self.menu_button = self.root_locator.get_by_role("button", name="Open Sidenav")
        self.search_button=self.root_locator.get_by_role("button", name="Open search")
        self.search_container = self.root_locator.locator(".search-container")
        self.account_button=self.root_locator.get_by_role("button", name="Show/hide account menu")
        self.basket_button=self.root_locator.get_by_role("button", name="Show the shopping cart")
        self.language_button=self.root_locator.get_by_role("button", name="Language selection menu")

    def search_product(self, name: str):
        self.search_button.click()
        self.search_container.fill(name)
        self.search_container.press("Enter")

    def click_menu(self):
        self.menu_button.click()

    def click_account(self):
        self.account_button.click()

    def click_basket(self):
        self.basket_button.click()

    def change_language(self):
        self.language_button.click()
