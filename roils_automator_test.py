import unittest
from pyroils.pyroils import RoilsAutomator
from pyroils.pages import MainPage, SubmitEventPage


class RoilsAutomatorTests(unittest.TestCase):
    """A test class to verify that RoilsAutomator can login and reach the main page"""

    def setUp(self):
        with open("roils_url.txt") as url_txt:
            self.url = url_txt.readline()
        self.roils = RoilsAutomator(self.url)

        with open("roils_credentials.txt") as login_creds:
            self.r_username = login_creds.readline()
            self.r_password = login_creds.readline()

    def test_login_on_roils(self):
        """
        Tests RO-ILS login feature. 
            (1) Create a new RoilsAutomator, which includes a login
            (2) Verify that we reach the main screen after login
        """

        # Attempts to login
        self.roils.login(self.r_username, self.r_password)

        assert MainPage.is_main_page(self.roils.driver)

    def test_submit_event_nav(self):

        # Login, then go to the Submit Event page
        self.roils.login(self.r_username, self.r_password)
        self.roils._navigate_to_submission_form()

        assert SubmitEventPage.is_submit_event_page(self.roils.driver)

    def tearDown(self):
        self.roils.driver.close()


if __name__ == "__main__":
    unittest.main()
