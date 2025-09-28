from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_successful_checkout(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.add_to_cart()
    cart.open_cart()
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_details("John", "Doe", "12345")
    checkout.continue_checkout()
    checkout.finish_checkout()

    assert "Thank you for your order!" in checkout.get_success_message()

def test_checkout_missing_fields(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    cart = CartPage(driver)
    cart.add_to_cart()
    cart.open_cart()
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_details("", "Doe", "12345")  # Missing first name
    checkout.continue_checkout()

    assert "Error: First Name is required" in checkout.get_error_message()
