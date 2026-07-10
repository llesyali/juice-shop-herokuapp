from playwright.sync_api import Locator, Page
from components.base_component import BaseComponent

class ProductComponent(BaseComponent):
    def __init__(self, page: Page, root_locator: Locator):
        super().__init__(page, root_locator)

        self.product_image = self.root_locator.locator(".image-container")
        self.product_name = self.root_locator.locator(".name")
        self.product_price = self.root_locator.locator(".price")
        self.add_to_basket_button=self.root_locator.get_by_role("button", name="Add to Basket")

    def add_to_basket(self, count: int):
        for i in range(count):
            self.add_to_basket_button.click()

    def open_product(self):
        self.product_image.click()

    def get_product_name(self):
        return self.product_name.inner_text()

    def get_product_price(self):
        text=self.product_price.inner_text()
        return float(text.replace("¤", "").strip())