from helper import wait_until

class BaseElement():

    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, value):
        try:
            type = wait_until.wait_until_presence_of_element_located(self.driver, locator)
            type.clear()
            type.send_keys(value)
        except:
            self.driver.quit()
            raise

    def click(self, locator):
        try:
            wait_until.wait_until_element_to_be_clickable(self.driver, locator ).click()
        except:
            self.driver.quit()
            raise

    def wait(self, locator):
        try:
            wait_until.wait_until_element_to_be_clickable(self.driver, locator )
        except:
            self.driver.quit()
            raise