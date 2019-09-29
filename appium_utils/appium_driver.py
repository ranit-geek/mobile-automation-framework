from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
from ptest.plogger import preporter


class AppiumDriver(webdriver.Remote):
    def __init__(self):
        self.appium_url = "http://{0}:{1}/wd/hub".format(config.APPIUM_HOST, config.APPIUM_PORT)
        super().__init__(self.appium_url, config.DESIRED_CAPS)
        preporter.info("Initializing appium driver for URL: " + self.appium_url)
        preporter.info("Desired Caps" + str(config.DESIRED_CAPS))
        self.explicit_wait_time = 0

    def set_explicit(self, explicit_wait_time):
        self.explicit_wait_time = explicit_wait_time

    def find_element_present(self, find_by, wait_until=None):
        wait_until = self.explicit_wait_time if wait_until is None else wait_until
        return WebDriverWait(self, wait_until).until(EC.presence_of_element_located(find_by))

    def find_elements_present(self, find_by, wait_until=None):
        wait_until = self.explicit_wait_time if wait_until is None else wait_until
        return WebDriverWait(self, wait_until).until(EC.presence_of_all_elements_located(find_by))

    def find_element_visible(self, find_by, wait_until=None):
        wait_until = self.explicit_wait_time if wait_until is None else wait_until
        return WebDriverWait(self, wait_until).until(EC.visibility_of_element_located(find_by))

    def is_element_present_until(self, find_by, wait_until=None):
        wait_until = self.explicit_wait_time if wait_until is None else wait_until
        return not WebDriverWait(self, wait_until).until(EC.invisibility_of_element_located(find_by))

    def uninstall_app(self):
        preporter.info("Removing package :" + self.current_package)
        self.remove_app(self.current_package)

