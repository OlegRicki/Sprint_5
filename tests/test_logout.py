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
        self.click_to_element(wait, MainPage.BUTTON_PRIVATE_OFFICE)
        self.click_to_element(wait, SettingsProfilePage.BUTTON_LOGOUT)

    def check_logout(self, wait: WebDriverWait):
        self.click_to_element(wait, MainPage.BUTTON_PRIVATE_OFFICE)
        wait.until(ec.invisibility_of_element_located(MainPage.TEXT_BURGER))
        text = wait.until(ec.visibility_of_element_located(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).text
        assert text == 'Войти'

    def test_go_to_private_office_page(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.click_to_element(wait, MainPage.BUTTON_PRIVATE_OFFICE)
        self.logout(wait)
        self.check_logout(wait)
