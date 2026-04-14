from e2e_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By



class LandingPage(BasePage):
    search_bar  = (By.ID, '<palcehodler>')
    search_button  = (By.ID, '<palcehodler>')
    all_items = (By.CLASS_NAME, "s-card s-card--vertical")
    item_price = (By.CSS_SELECTOR, ".s-card__price")
    cart_button = (By.CLASS_NAME, "gh-cart")

    def verify_ebay_page_ready(self):
        return self.get_element(search_bar)

    def search_for_item(self, item):
        self.type_text(self.search_bar, item)
        self.click(self.search_button)

    def select_item_by_index(self,min_price, max_price, items, how_many_items_to_select=1):
        items_selected = 0
        all_prices = []
        for item in range(len(items)):
            actual_price =  float(re.sub(r"[^\d.]", "", item.find_element(item_price).text))
            if min_price <= actual_price >= max_price:
                self.click(items[item])
                all_prices.append(actual_price)
                items_selected += 1
            else:
                continue
            if items_selected == how_many_items_to_select:
                return all_prices
        # add assert here to validate all prices is not none
        return None

    def get_items(self):
        return self.get_element(self.all_items)

    def click_on_cart(self):
        self.click(self.cart_button)
