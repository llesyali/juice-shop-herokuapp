from pathlib import Path

from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import os

load_dotenv()
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
dotenv_path=PROJECT_ROOT / ".env"

def test_right_search(page: Page):
    base_page = BasePage(page)
    page.goto(os.getenv("BASE_URL"))

    base_page.header.search_product("Lemon Juice")
    base_page.add_product_to_basket("Lemon Juice (500ml)", count=2)
    expect(base_page.header.basket_counter).to_have_text("2")
