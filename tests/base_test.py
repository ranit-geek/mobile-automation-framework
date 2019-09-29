from ptest.decorator import BeforeSuite, AfterSuite
from ptest.plogger import preporter
from screens.following_screen import FollowingScreen
from screens.onboarding_screen import OnBoardingScreen
from appium_utils.appium_driver import AppiumDriver


class PTestBase:

    @BeforeSuite()
    def before_suite(self):
        self.driver = AppiumDriver()
        preporter.info("Start Driver")
        self.on_boarding_screen = OnBoardingScreen(self.driver)
        self.following_screen = FollowingScreen(self.driver)

    @AfterSuite(always_run=True)
    def after_suite(self):
            self.driver.quit()
            preporter.info("Stop Driver")
            self.driver.uninstall_app()
            preporter.info("Uninstalled application")

