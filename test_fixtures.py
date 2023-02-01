import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = None


@pytest.fixture(scope='module')  # will be executed before the test case like setup method
def init_driver():
    global driver
    print("setup")
    driver = webdriver.Chrome("executable_path= C://chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")

    yield  # will be excecuted after the test cases like teardown
    print("teardown")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_google():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/"


