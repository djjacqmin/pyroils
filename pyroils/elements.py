from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyroils.locators import LoginPageLocators


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    locator = None

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.locator))
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")


# LOGIN PAGE ELEMENTS


class UsernameTextElement(BasePageElement):
    """This class gets the text from the specified locator"""

    # The locator for search box where search string is entered
    locator = LoginPageLocators.USERNAME_TEXT_BOX


class PasswordTextElement(BasePageElement):
    """This class gets the text from the specified locator"""

    # The locator for search box where search string is entered
    locator = LoginPageLocators.PASSWORD_TEXT_BOX


# MAIN PAGE ELEMENTS
