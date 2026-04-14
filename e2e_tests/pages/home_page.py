import re
from time import sleep

from e2e_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class HomePage(BasePage):
    search_bar  = (By.CSS_SELECTOR, '.ui-autocomplete-input')
    search_button  = (By.ID, 'gh-search-btn')
    all_items = (By.CSS_SELECTOR, ".srp-results.srp-grid.clearfix")
    item_price = (By.CSS_SELECTOR, "span.s-card__price")
    cart_button = (By.CLASS_NAME, "gh-cart__icon")
    all_prices = []

    def verify_ebay_page_ready(self):
        return self.get_element(self.search_bar)

    def search_for_item(self, item):
        self.type_text(self.search_bar, item)
        self.click(self.search_button)

    def select_item_by_index(self,min_price, max_price, item):
        price_el = item.find_element(By.CSS_SELECTOR, ".s-card__price")
        actual_price = price_el.get_attribute("innerText").strip()
        actual_price =  float(re.sub(r"[^\d.]", "", actual_price))
        if int(min_price) <= int(actual_price) <= int(max_price):
            self.click(element=item)
            self.all_prices.append(actual_price)
            return self.all_prices
        return None

    def get_items(self):
        return self.get_element(self.all_items)

    def click_on_cart(self):
        self.click(self.cart_button)
