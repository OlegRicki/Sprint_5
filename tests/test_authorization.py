from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from constants import TestUrl, TestDataUser
from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage, RegistrationPage,
)
from tests.test_base import TestBase


class TestAuthorization(TestBase):

    def test_authorization_the_login_button(self, driver):
        wait = WebDriverWait(driver, 10)

        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.send_keys(TestDataUser.EMAIL)

        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.send_keys(TestDataUser.PASSWORD)

        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        button_checkout = wait.until(ec.visibility_of_element_located(MainPage.BUTTON_CHECKOUT))
        assert button_checkout.is_displayed()

    def test_authorization_the_private_office_button(self, driver):
        wait = WebDriverWait(driver, 10)

        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_PRIVATE_OFFICE)).click()

        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.send_keys(TestDataUser.EMAIL)

        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.send_keys(TestDataUser.PASSWORD)

        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        button_checkout = wait.until(ec.visibility_of_element_located(MainPage.BUTTON_CHECKOUT))
        assert button_checkout.is_displayed()

    def test_authorization_the_registration_button(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url=f'{TestUrl.URL}register')

        wait.until(ec.element_to_be_clickable(RegistrationPage.LINK_TO_COME_IN)).click()

        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.send_keys(TestDataUser.EMAIL)

        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.send_keys(TestDataUser.PASSWORD)

        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        button_checkout = wait.until(ec.visibility_of_element_located(MainPage.BUTTON_CHECKOUT))
        assert button_checkout.is_displayed()

    def test_authorization_the_forgot_password_page(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url=f'{TestUrl.URL}forgot-password')

        wait.until(ec.element_to_be_clickable(RegistrationPage.LINK_TO_COME_IN)).click()

        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.send_keys(TestDataUser.EMAIL)

        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.send_keys(TestDataUser.PASSWORD)

        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        button_checkout = wait.until(ec.visibility_of_element_located(MainPage.BUTTON_CHECKOUT))
        assert button_checkout.is_displayed()
