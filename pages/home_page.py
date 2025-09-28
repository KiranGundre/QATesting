from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo = (By.CLASS_NAME, "app_logo")
        self.menu_btn = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def get_logo_text(self):
        return self.driver.find_element(*self.logo).text

    def logout(self):
        self.driver.find_element(*self.menu_btn).click()
        self.driver.find_element(*self.logout_link).click()
