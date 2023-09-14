from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *args, **kwargs):
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located((MobileBy.ID, "android:id/content"))
        )
        return self.driver.find_element(*args, **kwargs)

    @staticmethod
    def click_element(element):
        element.click()
