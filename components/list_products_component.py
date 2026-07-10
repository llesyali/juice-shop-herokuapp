from typing import List

from playwright.sync_api import Locator, Page
from components.base_component import BaseComponent
from components.product_component import ProductComponent

class ListProductsComponent(BaseComponent):
    def __init__(self, page: Page, root_locator: Locator):
        super().__init__(page, root_locator)

        self._product_card = "app-product"

    def get_product_list(self) -> List[ProductComponent]:

        cards_locator=self.root_locator.locator(self._product_card)
        cards_locator.first.wait_for(state="visible")

        products = []
        count=cards_locator.count()
        for i in range(count):
            product_locator = cards_locator.nth(i)
            product_comp = ProductComponent(self.page, product_locator)
            products.append(product_comp)

        return products



