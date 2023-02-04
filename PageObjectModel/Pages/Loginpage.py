from selenium.webdriver.common.by import By

from PageObjectModel.Config.config import TestData
from PageObjectModel.Pages.Basepage import Basepage
from PageObjectModel.Pages.Homepage import HomePage


class LoginPage(Basepage):
    """Locators"""
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions for Login Page"""

    """to get page title"""
    def get_page_title(self, title):
        return self.get_title(title)

    """To check signup link exists"""
    def signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    """To login"""
    def login(self, username, password):
        self.enter_send_keys(self.EMAIL, username)
        self.enter_send_keys(self.PASSWORD, password)
        self.perform_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)







