# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from pyroils.elements import BasePageElement
from pyroils.locators import LoginPageLocators


class UsernameTextElement(BasePageElement):
    """This class gets the text from the specified locator"""

    # The locator for search box where search string is entered
    locator = LoginPageLocators.USERNAME_TEXT_BOX


class PasswordTextElement(BasePageElement):
    """This class gets the text from the specified locator"""

    # The locator for search box where search string is entered
    locator = LoginPageLocators.PASSWORD_TEXT_BOX


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Methods for interacting with the RO-ILS main page"""

    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Login" appears in page title"""
        return "Login" in self.driver.title

    def click_sign_in_button(self):
        """Clicks "Sign in" to login to the website"""

        element = self.driver.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        """Verifies that the hardcoded text "Healthcare SafetyZone Portal – Home" appears in page title"""

        return "Healthcare SafetyZone Portal – Home" in self.driver.title
