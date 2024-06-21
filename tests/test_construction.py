from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from conftest import driver, authorization
from tests.test_base import TestBase
from locators.locators import (MainPage)


class TestConstruction(TestBase):
    def select_sections(self, wait: WebDriverWait, locator):
        try:
            text = wait.until(ec.visibility_of_element_located(locator)).get_attribute('class')
            assert 'tab_tab_type_current' in text
        except AssertionError:
            self.click_to_element(wait, locator=locator)

    def check_select_section(self, wait: WebDriverWait, locator):
        try:
            text = wait.until(ec.visibility_of_element_located(locator)).get_attribute('class')
            assert 'tab_tab_type_current' in text

        except Exception:
            raise Exception('раздел булки не выбран')

    def test_open_buns_sections(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.select_sections(
            wait, locator=MainPage.BUNS_BUTTON)
        self.check_select_section(wait, locator=MainPage.BUNS_BUTTON)

    def test_open_sauces_sections(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.select_sections(
            wait, locator=MainPage.SAUCES_BUTTON)
        self.check_select_section(wait, locator=MainPage.SAUCES_BUTTON)

    def test_open_fillings_sections(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        self.select_sections(
            wait, locator=MainPage.FILLING_BUTTON)
        self.check_select_section(wait, locator=MainPage.FILLING_BUTTON)
