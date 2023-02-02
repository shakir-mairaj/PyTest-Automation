import pytest
from selenium import webdriver


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome("executable_path=C://chromedriver.exe")
#     if request.param == "firefox":
#         driver = webdriver.Firefox()
#     request.cls.driver = driver
#     yield
#     driver.close()

# the above fixture is commented because it is in conftest file

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class Test_Google(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com")
        assert self.driver.title == "Google"
