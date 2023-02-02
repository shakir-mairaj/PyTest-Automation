# conftest file is used to store global fixtures which can be used for every test cases
# the below fixture is used in test_fixtures_parameters file

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome("executable_path=C://chromedriver.exe")
    if request.param == "firefox":
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.close()
