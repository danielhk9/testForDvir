from selenium.webdriver.common.by import By

from e2e_tests.pages.base_page import BasePage


class FilterPanel(BasePage):
    PRICE = (By.CLASS_NAME, "x-refine__price")
    MAX_PRICE = (By.XPATH, "//input[@aria-label='Maximum Value in ILS']")
    MIN_PRICE = (By.XPATH, "//input[@aria-label='Minimum Value in ILS']")
    NEW_ITEMS = (
        By.XPATH,
        "//input[@aria-label='New with box and papers']/ancestor::span[contains(@class,'x-refine__multi-select-checkbox')]"
    )

    def filter_by_price(self, min_price, max_price):
        self.type_text(self.MIN_PRICE, min_price)
        self.type_text(self.MAX_PRICE, max_price)
        self.submit()

    def filter_by_condition(self):
        self.click(self.NEW_ITEMS)