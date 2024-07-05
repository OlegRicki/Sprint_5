from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver, authorization
from tests.test_base import TestBase

from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage,
    SettingsProfilePage
)


class TestPageTransitions(TestBase):
    def logout(self, wait: WebDriverWait):
        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_PRIVATE_OFFICE)).click()
        wait.until(ec.element_to_be_clickable(SettingsProfilePage.BUTTON_LOGOUT)).click()

    def check_logout(self, wait: WebDriverWait):
        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_PRIVATE_OFFICE)).click()
        wait.until(ec.invisibility_of_element_located(MainPage.TEXT_BURGER))
        button = wait.until(ec.visibility_of_element_located(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT))
        assert button.is_displayed()

    def test_go_to_private_office_page(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_PRIVATE_OFFICE)).click()
        self.logout(wait)
        self.check_logout(wait)
