from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyroils.pages import LoginPage, MainPage, SelectFormPage, SubmitEventPage
import getpass


class RoilsAutomator(object):
    """A RO-ILS data entry automator"""

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)

    def login(self, r_username, r_password):
        """Login to the RO-ILS"""

        if self._is_logged_in():
            print(f"You are already logged in.")
        else:
            self.driver.get(self.url)
            if LoginPage.is_login_page(self.driver):
                login_page = LoginPage(self.driver)

                # Set username and password
                login_page.username_text_element = r_username
                login_page.password_text_element = r_password

                # Click the login button
                login_page.click_sign_in_button()

    def _is_logged_in(self):
        """Returns True if the user is already logged in"""
        self.driver.get(self.url)
        return MainPage.is_main_page(self.driver)

    def _navigate_to_submission_form(self):
        """ This private method navigates to the RO-ILS submission form """

        # Go to Main Page
        self.driver.get(self.url)

        # Click the Submit Event button
        main_page = MainPage(self.driver)
        main_page.click_submit_event_button()

        # Click the Event Form button
        select_form_page = SelectFormPage(self.driver)
        select_form_page.click_event_form_button()

