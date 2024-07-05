from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from conftest import driver, authorization
from tests.test_base import TestBase
from locators.locators import (MainPage)


class TestConstruction(TestBase):

    def test_open_buns_sections(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(MainPage.SAUCES_BUTTON)).click()
        wait.until(ec.element_to_be_clickable(MainPage.BUNS_BUTTON)).click()
        text = wait.until(ec.visibility_of_element_located(MainPage.BUNS_BUTTON)).get_attribute('class')
        assert 'tab_tab_type_current' in text

    def test_open_sauces_sections(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(MainPage.SAUCES_BUTTON)).click()
        text = wait.until(ec.visibility_of_element_located(MainPage.SAUCES_BUTTON)).get_attribute('class')
        assert 'tab_tab_type_current' in text

    def test_open_fillings_sections(self, driver, authorization):
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(MainPage.FILLING_BUTTON)).click()
        text = wait.until(ec.visibility_of_element_located(MainPage.FILLING_BUTTON)).get_attribute('class')
        assert 'tab_tab_type_current' in text
