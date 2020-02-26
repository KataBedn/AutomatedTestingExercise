class BasePage(object):
    URL = ''

    def __init__(self, context):
        self.context = context

    def open(self):
        self.context.driver.get(self.context.base_e2e_url + self.URL)
