import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome("executable_path= C://chromedriver.exe")
    request.cls.driver = ch_driver
    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_firefox_driver(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("init_chrome_driver")
class BaseChromeTest:
    pass


class Test_Google_Chrome(BaseChromeTest):

    def test_title_chrome(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"


@pytest.mark.usefixtures("init_firefox_driver")
class BaseFirefoxTest:
    pass


class Test_Google_Firefox(BaseFirefoxTest):

    def test_title_firefox(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"