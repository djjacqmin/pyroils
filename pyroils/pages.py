from pyroils.elements import UsernameTextElement, PasswordTextElement
from pyroils.locators import LoginPageLocators, MainPageLocators, SelectFormPageLocators


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Methods for interacting with the RO-ILS login page"""

    username_text_element = UsernameTextElement()
    password_text_element = PasswordTextElement()

    def has_correct_title(self):
        """Verifies that the hardcoded text "Login" appears in page title"""
        return "Login" in self.driver.title

    def click_sign_in_button(self):
        """Clicks "Sign in" to login to the website"""

        element = self.driver.find_element(*LoginPageLocators.SIGN_IN_BUTTON)
        element.click()

    @staticmethod
    def is_login_page(driver):
        """ Checks page title of driver to see if it is on the login page """
        return "Login" in driver.title


class MainPage(BasePage):
    """Methods for interacting with the RO-ILS main page"""

    def has_correct_title(self):
        """Verifies that the hardcoded text "Healthcare SafetyZone Portal – Home" appears in page title"""
        return "Healthcare SafetyZone Portal – Home" in self.driver.title

    def click_submit_event_button(self):
        """Clicks "Submit Event" to move to the "Select Form" page """

        element = self.driver.find_element(*MainPageLocators.SUBMIT_EVENT_BUTTON)
        element.click()

    @staticmethod
    def is_main_page(driver):
        """Verifies that the hardcoded text "Healthcare SafetyZone Portal – Home" appears in page title"""
        return "Healthcare SafetyZone Portal – Home" in driver.title


class SelectFormPage(BasePage):
    """Methods for interacting with the RO-ILS Select Form page"""

    def click_event_form_button(self):
        """Clicks "Event Form" to login to the website"""

        element = self.driver.find_element(*SelectFormPageLocators.EVENT_FORM_BUTTON)
        element.click()


class SubmitEventPage(BasePage):
    """Methods for interacting with the RO-ILS Submit Event page"""

    def has_correct_title(self):
        """Verifies that the hardcoded text "Submit Event" appears in page title"""
        return "Submit Event" in self.driver.title

    def click_save_button(self):
        pass

    @staticmethod
    def is_submit_event_page(driver):
        """Verifies that the hardcoded text "Submit Event" appears in page title"""
        return "Submit" in driver.title
