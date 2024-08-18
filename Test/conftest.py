import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IEService

driver = None
url = "https://www.linkedin.com/"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Browser to run tests on: chrome, firefox, IE"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = ChromeService()
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = FirefoxService()
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        service_obj = IEService()
        driver = webdriver.Ie(service=service_obj)
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver.maximize_window()
    driver.get(url)
    request.cls.driver = driver
    print("Browser:", browser_name)
    yield driver
    print("Close Driver")
    driver.quit()
