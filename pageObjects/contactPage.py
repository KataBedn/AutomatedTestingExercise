from pageObjects.basePage import BasePage


class ContactPage(BasePage):
    URL = "www.phptravels.net/contact-us"

    def __init__(self, context):
        super().__init__(context)
