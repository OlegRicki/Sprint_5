import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage)

from constants import Constants


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def authorization(driver):
    driver.get(f'{Constants.URL}login')
    wait = WebDriverWait(driver, 10)
    wait.until(ec.element_to_be_clickable(MainPage.BUTTON_LOGIN_TO_ACCOUNT)).click()

    field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
    field_email.send_keys(Constants.EMAIL)

    field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
    field_password.send_keys(Constants.PASSWORD)

    wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
    text_burger = wait.until(ec.element_to_be_clickable(MainPage.TEXT_BURGER)).text
    assert text_burger == 'Соберите бургер'
