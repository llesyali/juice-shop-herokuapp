from playwright.sync_api import Page
from components.header_component import HeaderComponent
from components.list_products_component import ListProductsComponent

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.header = HeaderComponent(page, page.locator("mat-toolbar"))
        self.list_products_component = ListProductsComponent(page, page.locator(".products-grid"))
        self.count_page_dropdown=self.page.locator(".mat-mdc-form-field-flex")
        self.prev_button=self.page.get_by_role("button", name="Previous page")
        self.next_button=self.page.get_by_role("button", name="Next page")

    def _find_product_in_list(self, name: str):
        all_products = self.list_products_component.get_product_list()
        for product in all_products:
            if name.lower() in product.get_product_name().lower():
                return product
        return None

    def add_product_to_basket(self, name:str, count:int):
        product = self._find_product_in_list(name)
        if product:
            product.add_to_basket(count)
        else:
            raise ValueError()


    def select_product_by_name(self, name:str):
        product = self._find_product_in_list(name)
        if product:
            product.open_product()
        else:
            raise ValueError(f"Продукт з назвою '{name}' не знайдено для вибору!")

