import re

from e2e_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test-id='SUBTOTAL']")

    def get_total_price(self):
        total_text = self.get_element(self.TOTAL_PRICE).text
        numbers = re.findall(r"\d+(?:\.\d+)?", total_text)
        total_price = float(numbers[0])
        return total_price

