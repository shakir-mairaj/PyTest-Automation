from PageObjectModel.Config.config import TestData
from PageObjectModel.Pages.Loginpage import LoginPage
from PageObjectModel.Tests.test_base import BaseTest


class Test_Home(BaseTest):

    def test_homepage_title(self):
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        title = homepage.get_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_homepage_header(self):
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        header = homepage.get_header_value(TestData.HOME_PAGE_HEADER)
        assert header == TestData.HOME_PAGE_HEADER

    def test_account_name_value(self):
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homepage.get_header_value(TestData.ACCOUNT_NAME)
        assert account_name == TestData.ACCOUNT_NAME

    def test_settings_icon(self):
        self.loginPage = LoginPage(self.driver)
        homepage = self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD)
        assert homepage.settings_icon()






