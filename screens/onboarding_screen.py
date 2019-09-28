import time

from selenium.common.exceptions import TimeoutException
from .base_screen import Screen
from appium.webdriver.common.mobileby import MobileBy
from ptest.plogger import preporter


class OnBoardingScreen(Screen):
    search_onboarding = (MobileBy.ID, 'onboarding_search')
    search_first_result = (MobileBy.XPATH, '(//*[@resource-id="de.motain.iliga:id/following_item_name"])[1]')
    privacy_confirmation = (MobileBy.ID, 'confirmTxt')

    def is_search_bar_displayed(self):
        try:
            self.driver.find_element_visible(self.search_onboarding, wait_until=10)
            return True
        except TimeoutException:
            return False

    def is_privacy_confirmation_displayed(self):
        try:
            self.driver.find_element_visible(self.privacy_confirmation, wait_until=10)
            return True
        except TimeoutException:
            return False

    def search_and_select_content(self, content):
        search_element = self.driver.find_element_visible(self.search_onboarding, wait_until=10)
        search_element.send_keys(content)
        time.sleep(5)    # Had to use sleep because unique id is not provided in app code for search results
        first_search_element = self.driver.find_element_visible(self.search_first_result, wait_until=10)
        if first_search_element.text == content:
            self.tap(first_search_element)
        else:
            raise ValueError("Did't found proper search result for {}".format(content))

    def accept_privacy_confirmation(self):
        if self.is_privacy_confirmation_displayed():
            privacy_confirmation_element = self.driver.find_element_visible(self.privacy_confirmation, wait_until=10)
            self.tap(privacy_confirmation_element)








