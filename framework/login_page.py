from appium.webdriver.common.mobileby import MobileBy
from selenium.common import NoSuchElementException

from .page import Page


class LoginPage(Page):
    def find_hello_login(self):
        return self.find_element(
            MobileBy.ID, "com.ajaxsystems:id/authHelloLogin"
        )

    def find_email(self):
        return self.find_element(
            MobileBy.ID, "com.ajaxsystems:id/authLoginEmail"
        )

    def find_password(self):
        return self.find_element(
            MobileBy.ID, "com.ajaxsystems:id/authLoginPassword"
        )

    def find_login(self):
        return self.find_element(MobileBy.ID, "com.ajaxsystems:id/authLogin")

    def find_sidebar(self):
        return self.find_element(MobileBy.ID, "com.ajaxsystems:id/menuDrawer")

    def is_element(self, element):
        try:
            self.driver.find_element(MobileBy.ID, element)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def write_email(email_field, email):
        email_field.clear()
        email_field.send_keys(email)

    @staticmethod
    def write_password(password_field, password):
        password_field.clear()
        password_field.send_keys(password)
