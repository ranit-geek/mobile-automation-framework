from appium.webdriver.common.touch_action import TouchAction
from ptest.plogger import preporter, pconsole


class Screen:
    """The base page for all other pages."""

    EXPLICIT_WAIT_TIME = 10

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_explicit(self.EXPLICIT_WAIT_TIME)
        self.action = TouchAction(self.driver)

    def tap(self, element):
        try:
            self.action.tap(element).perform()
        except Exception as e:
            preporter.critical("Element Not found to tap on\n" + str(e))
            pconsole.write_line("Element Not found to tap on\n" + str(e))
