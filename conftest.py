import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage)

from constants import TestDataUser, TestUrl


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestUrl.URL)
    yield driver
    driver.quit()


@pytest.fixture
def authorization(driver):
    driver.get(f'{TestUrl.URL}login')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable(MainPage.BUTTON_LOGIN_TO_ACCOUNT)).click()

    field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
    field_email.send_keys(TestDataUser.EMAIL)

    field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
    field_password.send_keys(TestDataUser.PASSWORD)
    wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()


