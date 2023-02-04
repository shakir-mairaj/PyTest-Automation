from selenium.webdriver.common.by import By

from PageObjectModel.Pages.Basepage import Basepage


class HomePage(Basepage):

    HEADER = (By.XPATH, "//i18n-string[contains(text(),'User Guide')]")
    ACCOUNT_NAME = (By.XPATH, "//span[contains(text(),'Brandoza')]")
    SETTINGS_ICON = (By.ID, "navSetting")

    def __init__(self,driver):
        super().__init__(driver)

    def get_homepage_title(self, title):
        return self.get_title(title)

    def settings_icon(self):
        return self.is_visible(self.SETTINGS_ICON)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)


