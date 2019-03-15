from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    locator = None

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.locator))
        driver.find_element_by_id(self.locator[1]).clear()
        driver.find_element_by_id(self.locator[1]).send_keys(value)

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(EC.presence_of_element_located(self.locator))
        element = driver.find_element_by_id(self.locator[1])
        return element.get_attribute("value")
