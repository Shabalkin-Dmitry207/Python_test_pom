import allure
import pytest
from config.settings import settings
from page.login_page import LoginPage
from playwright.sync_api import expect

@allure.epic("UI Тестирование")
@allure.feature("Авторизация")
class TestLogin:

    @allure.story("Позитивный сценарий проверям доступен ли сервер по умолчанию")
    @allure.title("Успешный переход на страницу самого браузера")
    def test_open_saucedemo(self,page):
        page.goto(settings.BASE_URL, wait_until="domcontentloaded")
        assert "saucedemo" in page.url

    @allure.story("Негативный сценарий с разнцми форматми данных")
    @allure.title("Вход с неверными форматами данных: {key}")
    @pytest.mark.parametrize("key, value", settings.INVALID_LOGIN_PASSWORD.items())
    def test_login_click_with_incorrect_format(self, page, key, value):
        login_page = LoginPage(page).open()
        login_page.click_login_incorrect_format(key, value)

    @allure.story("Позитивный сценарий")
    @allure.title("Успешная регистрация обычного пользователя")
    @pytest.mark.parametrize("login, password", settings.USERS_PASSWORD.items())
    def test_click_login(self, page, login, password):
        login_page = LoginPage(page).open()
        login_page.click_login(login, password)
        assert "inventory" in page.url
        expect(page.locator(".app_logo")).to_have_text("Swag Labs", timeout=30000)

    @allure.story("Позитивный сценарий вход под разными ролями")
    @allure.title("Вход под разной ролью: {login}")
    @pytest.mark.parametrize("login, password", settings.USERS_PASSWORD.items())
    def test_all_users_roll(self, page, login, password):
        login_page = LoginPage(page).open()
        login_page.click_login_users_role(login, password)
