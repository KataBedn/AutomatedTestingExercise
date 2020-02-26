import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from pages import Pages
from utilities.environments.common import CommonEnvironment


def take_screenshot(context):
    now = datetime.now().strftime('%Y-%m-%d-%H-%M-')
    scenario = context.scenario.name.replace(' ', '-')
    step = context.step.name.replace(' ', '-')
    filename = f'{os.getcwd()}/screenshots/{now}-{scenario}:{step}.png'
    context.driver.save_screenshot(filename)


def create_webdriver():
    driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                              desired_capabilities=DesiredCapabilities.CHROME)
    driver.set_window_size(os.getenv('SCREEN_WIDTH'), os.getenv('SCREEN_HEIGHT'))
    return driver


class WebEnvironment(CommonEnvironment):
    def before_scenario(self, context, scenario):
        super().before_scenario(context, scenario)
        context.base_e2e_url = os.getenv('E2E_URL')
        context.logger.info(f'Base E2E URL is: {context.base_e2e_url}')
        context.logger.info('Starting browser')
        context.driver = create_webdriver()
        context.pages = Pages(context)

    def after_scenario(self, context, scenario):
        super().after_scenario(context, scenario)
        context.logger.info('Closing browser')
        context.driver.quit()

    def after_step(self, context, step):
        super().after_step(context, step)
        if step.status == 'failed':
            take_screenshot(context)
