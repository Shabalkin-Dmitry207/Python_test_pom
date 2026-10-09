import pytest
from config.settings import settings
from page.login_page import LoginPage
from playwright.sync_api import expect


def test_open_saucedemo(page):
    "Просто открыть сайт"
    page.goto(settings.BASE_URL, wait_until="domcontentloaded")
    assert "saucedemo" in page.url

@pytest.mark.parametrize("key, value", settings.INVALID_LOGIN_PASSWORD.items())
def test_login_click_with_incorrect_format(page, key, value):
     "Авторизация негативный сценарий с обычным пользователям"
     login_page = LoginPage(page).open()
     login_page.click_login_incorrect_format(key, value)

@pytest.mark.parametrize("login, password", settings.USERS_PASSWORD.items())
def test_click_login(page, login, password):
    "Авторизация позитивный сценарий с обычным пользователям"
    login_page = LoginPage(page).open()
    login_page.click_login(login, password)
    assert "inventory" in page.url
    expect(page.locator(".app_logo")).to_have_text("Swag Labs", timeout=30000)

@pytest.mark.parametrize("login, password", settings.USERS_PASSWORD.items())
def test_all_users_roll(page, login, password):
    "Проверка всех ролей и доступ"
    login_page = LoginPage(page).open()
    login_page.click_login_users_role(login, password)
