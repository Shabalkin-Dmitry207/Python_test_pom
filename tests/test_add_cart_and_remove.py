from page.add_cart_and_remove import AddCartPage
from playwright.sync_api import expect



def test_add_cart (login_standard_user):
    cart_page = AddCartPage(login_standard_user)
    cart_page.add_backpack_to_cart()
    expect(cart_page.shopping_cart_badge).to_have_text("1")

def test_add_cart_and_remove(login_standard_user):
    cart_page = AddCartPage(login_standard_user)
    cart_page.add_backpack_to_cart()
    cart_page.remove_backpack_to_cat()
    expect(cart_page.shopping_cart_badge).to_be_hidden()

