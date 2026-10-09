from playwright.sync_api import Page,expect
from config.locators import Locators
from config.settings import settings, Settings
from page.base_page import BasePage




class AddCartPage(BasePage):
    base_url = settings.BASE_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.btn_add_backpack = page.locator(Locators.ADD_CART)
        self.btn_remove_backpack = page.locator(Locators.REMOVE_CART)
        self.shopping_cart_badge = page.locator(Locators.SHOPPING_CART_BADGE)

    def add_backpack_to_cart(self):
        """Метод кликает по кнопке добавления товара в корзину"""
        self.btn_add_backpack.click()
        return self

    def remove_backpack_to_cat(self):
        if self.btn_remove_backpack.is_visible():
            self.btn_remove_backpack.click()
        else:
            raise AssertionError("Кнопка 'Remove' не найдена на странице")

            return self