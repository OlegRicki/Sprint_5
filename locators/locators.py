from selenium.webdriver.common.by import By


class LocatorsAuthorizationPage:
    """Локаторы страницы авторизации"""
    PASSWORD_FIELD = (By.XPATH, '//label[text()="Пароль"]/../input')
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/../input')
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, '//button[contains(@class, "button_button")]')
    LINK_REGISTER = (By.XPATH, '(//a[contains(@class, "Auth_link")])[1]')


class RegistrationPage:
    """Локаторы страницы регистрации"""
    NAME_FIELD = (By.NAME, 'name')
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/../input')
    PASSWORD_FIELD = (By.NAME, 'Пароль')
    BUTTON_REGISTER = (By.XPATH, '//button[contains(@class, "button_button__")]')

    AUTHORIZATION_FORM = (By.XPATH, '//h2[text()="Вход"]')
    LINK_TO_COME_IN = (By.XPATH, '//a[contains(@class, "Auth_link")]')


class MainPage:
    """Локаторы главного меню"""
    BUTTON_PRIVATE_OFFICE = (By.XPATH, '//p[text()="Личный Кабинет"]')
    BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, '//button[contains(@class, "button_button")]')
    TEXT_BURGER = (By.XPATH, '//h1[text()="Соберите бургер"]')
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')
    LOGO = (By.XPATH, '//div[contains(@class, "AppHeader_header__logo_")]')

    BUNS_BUTTON = (By.XPATH, '//span[text()="Булки"]/..')
    SAUCES_BUTTON = (By.XPATH, '//span[text()="Соусы"]/..')
    FILLING_BUTTON = (By.XPATH, '//span[text()="Начинки"]/..')
    BUTTON_CHECKOUT = (By.XPATH, '//button[text()="Оформить заказ"]')


class SettingsProfilePage:
    """Локаторы страницы профиля"""
    LIST_SETTINGS_PROFILE = (By.XPATH, '//nav[contains(@class, "Account_nav")]')
    NAME_FIELD = (By.XPATH, '//input[@name="Name"]')
    EMAIL_FIELD = (By.XPATH, '(//input[@name="name"])[1]')
    BUTTON_LOGOUT = (By.XPATH, '//button[text()="Выход"]')


class Message:
    """Локаторы сообщений"""
    MESSAGE_ERROR_PASSWORD = (By.XPATH, '//p[contains(@class, "input__error")]')
