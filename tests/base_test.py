from ptest.decorator import BeforeSuite, AfterSuite, AfterMethod, BeforeMethod
from ptest.plogger import preporter, pconsole
from screens.onboarding_screen import OnBoardingScreen

from appium_utils.appium_driver import AppiumDriver


class PTestBase:

    @BeforeSuite()
    def before_suite(self):
        self.driver = AppiumDriver()  # Starting Driver here
        pconsole.write_line("Start Driver")
        self.on_boarding_screen = OnBoardingScreen(self.driver)

    @AfterSuite(always_run=True)
    def after_suite(self):
            # self.driver.quit()
            # self.driver.uninstall_app()
            pconsole.write_line("Stop Driver")
