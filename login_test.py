import unittest
from selenium import webdriver
from pyroils import pages
import getpass


class RoilsLogin(unittest.TestCase):
    """A test class to verify the login function"""

    def setUp(self):
        with open("roils_url.txt") as url_txt:
            self.url = url_txt.readline()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(25)
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
        assert login_page.has_correct_title(), "Login"

        # Sets the text of the "Username" and "Password" boxes to user-defined input
        login_page.username_text_element = input("Username: ")
        login_page.password_text_element = getpass.getpass("Password: ")
        login_page.click_sign_in_button()

        main_page = pages.MainPage(self.driver)
        # Verifies that the results page is not empty
        assert main_page.has_correct_title(), "Healthcare SafetyZone Portal – Home"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
