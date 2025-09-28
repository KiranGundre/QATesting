from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def cancel_alert(self, timeout=3):
        """Wait for an alert and dismiss it if present"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()   # cancel the alert
            print("[INFO] Alert dismissed successfully")
        except (NoAlertPresentException, TimeoutException):
            pass  # no alert found, safe to continue
