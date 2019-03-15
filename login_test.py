import unittest
from selenium import webdriver
from pyroils import pages
import getpass


class RoilsLogin(unittest.TestCase):
    """A test class to verify the login function"""

    def setUp(self):
        self.url = "https://events.healthcaresafetyzone.com/EventsModuleWeb/default.aspx?cs=49ff4d9e-ece1-43ca-9a7c-5cd25901d84c&groupaccessId=cc2b44da-f619-4e8f-b159-f6518b893bde"
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def test_login_on_roils(self):
        """
        Tests RO-ILS login feature. 
        (0) Opens the Login page
        (1) Prompts the user to enter a username and password. 
        (2) Enters the username and password into the appropriate elemetns
        (3) Presses the "Sign in" buttton
        (4) Verifies the resulting page has the main page title.
        """

        # Load the login page.
        login_page = pages.LoginPage(self.driver)

        # Checks if the word "Login" is in title
        assert login_page.is_title_matches(), "Login"

        # Sets the text of search textbox to "pycon"
        login_page.username_text_element = input("Username: ")
        login_page.password_text_element = getpass.getpass("Password: ")
        login_page.click_sign_in_button()

        search_results_page = pages.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        assert (
            search_results_page.is_results_found()
        ), "Healthcare SafetyZone Portal – Home"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
