from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """A class for RO-ILS login page locators. All login page locators should come here"""

    USERNAME_TEXT_BOX = (By.ID, "ctl00_contentBody_txtUserName")
    PASSWORD_TEXT_BOX = (By.ID, "ctl00_contentBody_txtPassword")
    SIGN_IN_BUTTON = (By.ID, "ctl00_contentBody_cmdSubmit")


class MainPageLocators(object):
    """A class for RO-ILS main page locators. All main page locators should come here"""

    SUBMIT_EVENT_BUTTON = (By.ID, "ctl00_contentBody_btnSubmit")


class SelectFormPageLocators(object):
    """A class for RO-ILS Select Form page locators. All Select Form page locators should come here"""

    EVENT_FORM_BUTTON = (By.ID, "ctl00_contentBody_dlFormOne_ctl00_btnOne")
    DOCUMENT_UPLOAD_BUTTON = (By.ID, "ctl00_contentBody_dlFormTwo_ctl00_btnTwo")

