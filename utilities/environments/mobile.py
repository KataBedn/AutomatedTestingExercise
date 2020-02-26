import os

from appium import webdriver

from pages import Pages
from utilities.environments.common import CommonEnvironment


class MobileEnvironment(CommonEnvironment):
    def before_scenario(self, context, scenario):
        super().before_scenario(context, scenario)
        desired_caps = {
            'deviceName': os.getenv('DEVICE_NAME'),
            'fullReset': os.getenv('FULL_RESET'),
            'app': os.getenv('APP_PATH'),
            'platformName': os.getenv('PLATFORM_NAME'),
            'appPackage': os.getenv('APP_PACKAGE'),
            'appActivity': os.getenv('APP_ACTIVITY'),
            'automationName': os.getenv('AUTOMATION_NAME')
        }
        context.driver = webdriver.Remote(os.getenv('MOBILE_ADDRESS'), desired_caps)
        context.driver.implicitly_wait(5)
        context.pages = Pages(context)

    def after_scenario(self, context, scenario):
        super().after_scenario(context, scenario)
        context.driver.quit()
