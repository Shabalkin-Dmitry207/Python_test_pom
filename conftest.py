import pytest
from page.login_page import LoginPage
from playwright.sync_api import sync_playwright, Page, Browser
from config.settings import settings

@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser) -> Page:
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        locale="ru-RU",
    )
    page = context.new_page()

    yield page
    context.close()

@pytest.fixture(scope="function")
def login_standard_user(page: Page) -> Page:
    """Фикстура для автоматического логина перед тестом"""
    login_page = LoginPage(page).open()
    login_page.click_login("standard_user", settings.USERS_PASSWORD["standard_user"])
    return page
