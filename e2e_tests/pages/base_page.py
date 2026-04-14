from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_element(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False

    def wait_for_elements(self, locator):
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            assert False

    def get_element(self, locator):
        return self.wait_for_element(locator)

    def get_element_inside_locator(self, main_locator, locator):
        return self.driver.find_element(main_locator, locator)

    def submit(self):
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def get_elements(self, locator):
        return self.wait_for_elements(locator)

    def click(self, locator=True, element=None):
        if element:
            element.click()
        else:
            self.get_element(locator).click()

    def type_text(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def change_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_tab(self):
        self.driver.close()


