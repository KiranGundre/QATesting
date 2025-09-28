from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")
        self.error_msg = (By.XPATH, "//h3[@data-test='error']")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")
        self.cancel_alert()   # dismiss any alert if present

    def login(self, user, pwd):
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
        self.cancel_alert()   # handle alert after login attempt

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text
