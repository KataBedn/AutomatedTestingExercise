from pageObjects.basePage import BasePage


class AppView(BasePage):

#Using PIXEL 2 API 28 app

    def add_two_plus_two(self):
        button2 = self.context.driver.find_element_by_xpath("//*[@text='2']")
        plus_button = self.context.driver.find_element_by_xpath("//*[@text='+']")
        equal_button = self.context.driver.find_element_by_xpath("//*[@text='=']")

        button2.click()
        plus_button.click()
        button2.click()
        equal_button.click()

    def assert_result_of_two_plus_two(self):
        result = self.context.driver.find_element_by_id("com.android.calculator2:id/result").get_attribute("text")
        assert int(result) == 4

