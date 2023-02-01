import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = None


def setup_module(module):  # will execute before test cases
    global driver
    driver = webdriver.Chrome("executable_path= C://chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")


def teardown_module(module):  # will execute after all the test cases
    driver.quit()


def test_google_title():
    assert driver.title == "Google"


def test_google_url():
    assert driver.current_url == "https://www.google.com/"

# to view html report first install  pip install pytest-html
# and then run py.test filename -v -s --html=reportname.html
