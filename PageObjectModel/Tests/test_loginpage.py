import pytest

from PageObjectModel.Config.config import TestData
from PageObjectModel.Tests.test_base import BaseTest
from PageObjectModel.Pages.Loginpage import LoginPage


class Test_Login(BaseTest):

    def test_signup_link(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.signup_link_exist()
        assert flag

    def test_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.USER_NAME, TestData.PASSWORD )






