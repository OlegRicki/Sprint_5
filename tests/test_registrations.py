from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from tests.test_base import TestBase
from locators.locators import (
    LocatorsAuthorizationPage,
    MainPage, RegistrationPage,
    SettingsProfilePage,
    Message
)

faker = Faker()


class TestRegistration(TestBase):
    def go_to_registration_page(self, wait: WebDriverWait):
        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.LINK_REGISTER)).click()

    def fill_field_registration(self, wait: WebDriverWait, name, email, password):
        wait.until(ec.element_to_be_clickable(RegistrationPage.NAME_FIELD)).send_keys(name)
        wait.until(ec.element_to_be_clickable(RegistrationPage.EMAIL_FIELD)).send_keys(email)
        wait.until(ec.element_to_be_clickable(RegistrationPage.PASSWORD_FIELD)).send_keys(password)

    def registration_new_user(self, wait: WebDriverWait, name, email, password):
        self.fill_field_registration(wait, name, email, password)
        self.click_to_element(wait, RegistrationPage.BUTTON_REGISTER)
        wait.until(ec.visibility_of_all_elements_located(RegistrationPage.AUTHORIZATION_FORM))

    def check_registration_new_user(self, wait: WebDriverWait, name, email, password):
        wait.until(ec.visibility_of_all_elements_located(RegistrationPage.AUTHORIZATION_FORM))

        field_email = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.EMAIL_FIELD))
        field_email.click()
        field_email.send_keys(email)

        wait.until(ec.visibility_of_element_located(LocatorsAuthorizationPage.PASSWORD_FIELD)).click()
        field_password = wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.PASSWORD_FIELD))
        field_password.click()
        field_password.send_keys(password)
        wait.until(ec.text_to_be_present_in_element_value(LocatorsAuthorizationPage.PASSWORD_FIELD, password))
        wait.until(ec.element_to_be_clickable(LocatorsAuthorizationPage.BUTTON_LOGIN_TO_ACCOUNT)).click()
        wait.until(ec.element_to_be_clickable(MainPage.BUTTON_PRIVATE_OFFICE)).click()

        wait.until(ec.visibility_of_element_located(SettingsProfilePage.LIST_SETTINGS_PROFILE))
        new_name = wait.until(ec.presence_of_element_located(SettingsProfilePage.NAME_FIELD)).get_attribute('value')
        new_email = wait.until(ec.presence_of_element_located(SettingsProfilePage.EMAIL_FIELD)).get_attribute('value')
        assert new_name == name
        assert new_email == email

    def check_error_message(self, wait: WebDriverWait, locator, message: str):
        error_message = wait.until(ec.visibility_of_element_located(locator)).text
        assert error_message == message

    def test_registration_new_user(self, driver):
        wait = WebDriverWait(driver, 10, 0.4)
        original_name = faker.name()
        original_email = faker.email()
        original_password = '12345678910'

        self.go_to_registration_page(wait)

        self.registration_new_user(wait, name=original_name, email=original_email, password=original_password)
        driver.refresh()
        self.check_registration_new_user(
            wait, name=original_name, email=original_email, password=original_password)

    def test_fail_password_during_registration(self, driver):
        wait = WebDriverWait(driver, 10, 0.4)
        original_name = faker.name()
        original_email = faker.email()
        original_password = '1'
        self.go_to_registration_page(wait)
        self.fill_field_registration(wait, name=original_name, email=original_email, password=original_password)
        self.click_to_element(wait, RegistrationPage.BUTTON_REGISTER)
        self.check_error_message(wait, Message.MESSAGE_ERROR_PASSWORD, message='Некорректный пароль')
