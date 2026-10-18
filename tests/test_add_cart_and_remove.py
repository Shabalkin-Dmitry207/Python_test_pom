import allure
from page.add_cart_and_remove import AddCartPage
from playwright.sync_api import expect

@allure.epic("UI Тестирование")
@allure.feature("Проверки базовые удаления и добавления в корзину")
class TestCart:

    @allure.story("Добавление товара")
    @allure.title("Добавление рюкзака в корзину")
    def test_add_cart (self,login_standard_user):
        cart_page = AddCartPage(login_standard_user)
        cart_page.add_backpack_to_cart()
        expect(cart_page.shopping_cart_badge).to_have_text("1")

    @allure.story("Удаление товара")
    @allure.title("Добавление и удаление рюкзака из корзины")
    def test_add_cart_and_remove(self, login_standard_user):
        cart_page = AddCartPage(login_standard_user)
        cart_page.add_backpack_to_cart()
        cart_page.remove_backpack_to_cat()
        expect(cart_page.shopping_cart_badge).to_be_hidden()

