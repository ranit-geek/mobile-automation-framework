import os
import glob
from ptest import config

USER_DIR = os.path.dirname(os.path.abspath('_file_'))
APP_PATH_PROJECT_LEVEL = glob.glob('resources/app/*.apk')
APP_PATH = USER_DIR + "/" + APP_PATH_PROJECT_LEVEL.pop()           # Path of the application
APPIUM_HOST = "0.0.0.0"
APPIUM_PORT = "4723"
APPIUM_URL = "http://{}:{}/wd/hub".format(APPIUM_HOST, APPIUM_PORT)
DESIRED_CAPS = {
    "app": APP_PATH,
    "platformName": "Android",
    "deviceName": "testDevice",
    "autoGrantPermissions": "true",
    "newCommandTimeout": 0
}
# Uncomment the following desired capabilities if you don't want to give apk instead want to use app installed in device

# DESIRED_CAPS = {
#   "platformName": "Android",
#   "deviceName": "MotoG",
#   "appPackage": "de.motain.iliga",
#   "appActivity": "de.motain.iliga.activity.FastLaunchSplashScreenActivity",
#   "autoGrantPermissions": "true"
# }
APPIUM_SERVER_LOG = config.get_option("output_dir") + "/appium_server_log.log"