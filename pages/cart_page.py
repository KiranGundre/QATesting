from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_item = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_item = (By.ID, "remove-sauce-labs-backpack")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_btn = (By.CSS_SELECTOR, ".btn_action.checkout_button")

    def add_to_cart(self):
        self.driver.find_element(*self.add_item).click()

    def remove_from_cart(self):
        self.driver.find_element(*self.remove_item).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
