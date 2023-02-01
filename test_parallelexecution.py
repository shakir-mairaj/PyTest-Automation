# to run tests in parallel mode, first install-- pip install pytest-xdist
# command py.test filename -n 2   --- 2 browsers will run parallely

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


def test_google():
    driver = webdriver.Chrome("executable_path= C://chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    driver.quit()


def test_yahoo():
    driver = webdriver.Chrome("executable_path= C://chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.yahoo.com")
    assert driver.title == "Yahoo Search - Web Search"
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome("executable_path= C://chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get("https://www.gmail.com")
    assert driver.title == "Sign in - Google Accounts"
    driver.quit()

