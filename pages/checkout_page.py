from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_btn = (By.ID, "continue")
        self.finish_btn = (By.ID, "finish")
        self.success_msg = (By.CLASS_NAME, "complete-header")
        self.error_msg = (By.XPATH, "//h3[@data-test='error']")

    def fill_details(self, fname, lname, pcode):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(pcode)
        self.cancel_alert()

    def continue_checkout(self):
        self.driver.find_element(*self.continue_btn).click()
        self.cancel_alert()

    def finish_checkout(self):
        self.driver.find_element(*self.finish_btn).click()
        self.cancel_alert()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
