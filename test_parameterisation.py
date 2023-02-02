import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestWebsite(BaseTest):

    @pytest.mark.parametrize(
        "username, password",
        [
            ("admin@gmail.com", "admin123"),
            ("test123@gmail.com", "test123"),
        ]
    )
    def test_login(self, username, password):
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID, "username").send_keys(username)
        time.sleep(3)
        self.driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(3)
