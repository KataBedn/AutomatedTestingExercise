from pageObjects.basePage import BasePage


class HomePage(BasePage):
    URL = "www.google.pl"

    def __init__(self, context):
        super().__init__(context)
