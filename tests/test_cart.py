from pages.login_page import LoginPage
from pages.cart_page import CartPage

def test_add_remove_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.add_to_cart()
    cart.open_cart()

    # Verify item added
    assert "Remove" in driver.page_source

    cart.remove_from_cart()
    assert "Remove" not in driver.page_source
