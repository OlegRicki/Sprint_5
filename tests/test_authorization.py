from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from constants import TestUrl, TestDataUser
from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage, RegistrationPage,
    SettingsProfilePage
)
from tests.test_base import TestBase


class TestAuthorization(TestBase):
    def authorization(self, wait: WebDriverWait, login, password):
        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.send_keys(login)

        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.send_keys(password)

        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        button_checkout = wait.until(ec.visibility_of_element_located(MainPage.BUTTON_CHECKOUT))
        assert button_checkout.is_displayed()

    def check_user_data(self, wait: WebDriverWait, name, login):

        self.click_to_element(wait, locator=MainPage.BUTTON_PRIVATE_OFFICE)

        name_in_profile = wait.until(
            ec.visibility_of_element_located(SettingsProfilePage.NAME_FIELD)).get_attribute('value')
        login_in_profile = wait.until(
            ec.visibility_of_element_located(SettingsProfilePage.EMAIL_FIELD)).get_attribute('value')
        assert name_in_profile == name
        assert login_in_profile == login

    def test_authorization_the_login_button(self, driver):
        wait = WebDriverWait(driver, 10)

        self.click_to_element(wait, locator=MainPage.BUTTON_LOGIN_TO_ACCOUNT)
        self.authorization(wait, login=TestDataUser.EMAIL, password=TestDataUser.PASSWORD)
        self.check_user_data(wait, name=TestDataUser.NAME, login=TestDataUser.EMAIL)

    def test_authorization_the_private_office_button(self, driver):
        wait = WebDriverWait(driver, 10)

        self.click_to_element(wait, locator=MainPage.BUTTON_PRIVATE_OFFICE)

        self.authorization(wait, login=TestDataUser.EMAIL, password=TestDataUser.PASSWORD)
        self.check_user_data(wait, name=TestDataUser.NAME, login=TestDataUser.EMAIL)

    def test_authorization_the_registration_button(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url=f'{TestUrl.URL}register')

        self.click_to_element(wait, locator=RegistrationPage.LINK_TO_COME_IN)
        self.authorization(wait, login=TestDataUser.EMAIL, password=TestDataUser.PASSWORD)
        self.check_user_data(wait, name=TestDataUser.NAME, login=TestDataUser.EMAIL)

    def test_authorization_the_forgot_password_page(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url=f'{TestUrl.URL}forgot-password')

        self.click_to_element(wait, locator=RegistrationPage.LINK_TO_COME_IN)
        self.authorization(wait, login=TestDataUser.EMAIL, password=TestDataUser.PASSWORD)
        self.check_user_data(wait, name=TestDataUser.NAME, login=TestDataUser.EMAIL)
