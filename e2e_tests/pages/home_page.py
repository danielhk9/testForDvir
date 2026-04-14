import re
import logging
from e2e_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


logger = logging.getLogger(__name__)

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

    def select_item_by_index(self, min_price, max_price, item):
        try:
            price_el = item.find_element(By.CSS_SELECTOR, ".s-card__price")
            actual_price = price_el.get_attribute("innerText").strip()
            logger.info(f"Raw price text: '{actual_price}'")
            actual_price = float(re.sub(r"[^\d.]", "", actual_price))

            logger.info(f"Parsed price: {actual_price} | Range: {min_price}-{max_price}")

            if int(min_price) <= int(actual_price) <= int(max_price):
                logger.info("✅ Item in range → clicking item")
                self.click(element=item)
                self.all_prices.append(actual_price)
                logger.info(f"Added price: {actual_price}")
                return self.all_prices
            else:
                logger.info("❌ Item NOT in range")

        except Exception as e:
            logger.error(f"Error processing item: {e}")

        return None

    def get_items(self):
        return self.get_element(self.all_items)

    def click_on_cart(self):
        self.click(self.cart_button)
