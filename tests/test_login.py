import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.smoke
def test_valid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    home = HomePage(driver)
    assert home.get_logo_text() == "Swag Labs"

@pytest.mark.negative
def test_invalid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("locked_out_user", "secret_sauce")

    assert "Epic sadface" in login.get_error_message()
