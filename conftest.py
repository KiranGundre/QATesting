import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser option: chrome, firefox, edge"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-notifications")
        options.add_experimental_option("prefs", {
           "credentials_enable_service": False,
            "profile.password_manager_enabled": False
})

        driver = webdriver.Chrome(service=ChromeService(), options=options)


    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.set_preference("dom.webnotifications.enabled", False)
            options.set_preference("signon.rememberSignons", False)

        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Edge(service=EdgeService(), options=options)

    else:
        raise ValueError(f"Browser '{browser}' is not supported. Use chrome, firefox, or edge.")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
