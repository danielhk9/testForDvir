from selenium.webdriver.common.by import By

from e2e_tests.pages.base_page import BasePage


class FilterPanel(BasePage):
    PRICE = (By.CLASS_NAME, "x-refine__price")
    MAX_PRICE = (By.XPATH, "//input[@aria-label='Maximum Value in $']")
    MIN_PRICE = (By.XPATH, "//input[@aria-label='Minimum Value in $']")

    def filter_by_price(self, min_price, max_price):
        self.type_text(self.PRICE, min_price)
        self.type_text(self.PRICE, max_price)
        self.submit(self.PRICE)