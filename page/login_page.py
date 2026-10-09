# Page Object для страницы логина
# Здесь будут локаторы и методы: login, expect_error
from playwright.sync_api import Page,expect

from config.locators import Locators
from config.settings import settings
from page.base_page import BasePage

class LoginPage(BasePage):
    base_url = settings.BASE_URL

    def __init__(self, page: Page):
        super().__init__(page)
        self.textbox_login = page.locator(Locators.LOGIN)
        self.textbox_password = page.locator(Locators.PASSWORD)
        self.login_button = page.get_by_text("Login", exact=True)


    def open(self):
        self.page.goto(self.base_url, wait_until="domcontentloaded")
        return self

    def click_login(self, login: str, password: str):
        self.textbox_login.fill(login)
        self.textbox_password.fill(password)
        self.login_button.click()
        self.page.wait_for_url("**/inventory.html")
        return self

    def click_login_incorrect_format(self, key: str, value: str):
            login, password = value.split(":")
            self.textbox_login.fill(login.strip())
            self.textbox_password.fill(password.strip())
            self.login_button.click()
            assert "inventory" not in self.page.url, f"Unexpected login for: {key}"
            return self

    def click_login_users_role(self, login: str, password: str):
            self.page.context.clear_cookies()
            self.page.goto(self.base_url, wait_until="domcontentloaded")
            self.textbox_login.fill(login.strip())
            self.textbox_password.fill(password.strip())
            self.login_button.click()
            assert "inventory" in self.page.url, f"Unexpected login for: {login}"
            return self