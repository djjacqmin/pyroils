from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for RO-ILS main page locators. All main page locators should come here"""

    USERNAME_TEXT_BOX = (By.ID, "ctl00_contentBody_txtUserName")
    PASSWORD_TEXT_BOX = (By.ID, "ctl00_contentBody_txtPassword")
    SIGN_IN_BUTTON = (By.ID, "ctl00_contentBody_cmdSubmit")

