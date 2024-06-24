from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestBase:
    def click_to_element(self, wait: WebDriverWait, locator):
        wait.until(ec.visibility_of_element_located(locator))
        wait.until(ec.element_to_be_clickable(locator)).click()
