from appium.webdriver.common.appiumby import AppiumBy

from .page import Page


class LoginPage(Page):
    def find_hello_login(self):
        return self.find_element(AppiumBy.ACCESSIBILITY_ID, "authHelloLogin")

    def find_email(self):
        return self.find_element(AppiumBy.ACCESSIBILITY_ID, "authLoginEmail")

    def find_password(self):
        return self.find_element(AppiumBy.ACCESSIBILITY_ID, "authLoginPassword")

    def find_login(self):
        return self.find_element(AppiumBy.ACCESSIBILITY_ID, "authLogin")

    def find_sidebar(self):
        return self.find_element(AppiumBy.ACCESSIBILITY_ID, "menuDrawer")

    @staticmethod
    def write_email(email_field, email):
        email_field.send_keys(email)

    @staticmethod
    def write_password(password_field, password):
        password_field.send_keys(password)
