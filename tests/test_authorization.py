from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from tests.test_base import TestBase
from constants import Constants
from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage, RegistrationPage,
)


class TestAuthorization(TestBase):
    def authorization(self, wait: WebDriverWait, login, password):
        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.send_keys(login)

        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.send_keys(password)

        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        text_burger = wait.until(ec.element_to_be_clickable(MainPage.TEXT_BURGER)).text
        assert text_burger == 'Соберите бургер'

    def test_authorization_the_login_button(self, driver):
        wait = WebDriverWait(driver, 10)

        self.click_to_element(wait, locator=MainPage.BUTTON_LOGIN_TO_ACCOUNT)

        self.authorization(wait, login=Constants.EMAIL, password=Constants.PASSWORD)

    def test_authorization_the_private_office_button(self, driver):
        wait = WebDriverWait(driver, 10)

        self.click_to_element(wait, locator=MainPage.BUTTON_PRIVATE_OFFICE)

        self.authorization(wait, login=Constants.EMAIL, password=Constants.PASSWORD)

    def test_authorization_the_registration_button(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url=f'{Constants.URL}register')

        self.click_to_element(wait, locator=RegistrationPage.LINK_TO_COME_IN)
        self.authorization(wait, login=Constants.EMAIL, password=Constants.PASSWORD)

    def test_authorization_the_forgot_password_page(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(url=f'{Constants.URL}forgot-password')

        self.click_to_element(wait, locator=RegistrationPage.LINK_TO_COME_IN)
        self.authorization(wait, login=Constants.EMAIL, password=Constants.PASSWORD)
