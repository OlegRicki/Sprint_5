from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver, authorization
from constants import TestDataUser
from tests.test_base import TestBase
from locators.locators import (
    MainPage, SettingsProfilePage,
)


class TestTransitions(TestBase):
    def check_private_office_page(self, wait: WebDriverWait):
        wait.until(ec.visibility_of_element_located(SettingsProfilePage.LIST_SETTINGS_PROFILE))
        name = wait.until(ec.presence_of_element_located(SettingsProfilePage.NAME_FIELD)).get_attribute('value')
        email = wait.until(ec.presence_of_element_located(SettingsProfilePage.EMAIL_FIELD)).get_attribute('value')
        assert name == TestDataUser.NAME
        assert email == TestDataUser.EMAIL

    def check_constructor_page(self, wait: WebDriverWait):
        text = wait.until(ec.visibility_of_element_located(MainPage.TEXT_BURGER)).text
        assert text == 'Соберите бургер'

    def test_go_to_private_office_page(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.click_to_element(wait, MainPage.BUTTON_PRIVATE_OFFICE)
        self.check_private_office_page(wait)

    def test_go_to_constructor_page(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.click_to_element(wait, MainPage.BUTTON_PRIVATE_OFFICE)
        self.check_private_office_page(wait)
        self.click_to_element(wait, MainPage.BUTTON_CONSTRUCTOR)
        self.check_constructor_page(wait)

    def test_go_to_registration_page_by_using_logo(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.click_to_element(wait, MainPage.BUTTON_PRIVATE_OFFICE)
        self.check_private_office_page(wait)
        self.click_to_element(wait, MainPage.BUTTON_CONSTRUCTOR)
        self.check_constructor_page(wait)

