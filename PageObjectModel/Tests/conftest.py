import pytest
from selenium import webdriver
from PageObjectModel.Config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome("executable_path=TestData.CHROME_EXECUTABLE_PATH")
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.close()
