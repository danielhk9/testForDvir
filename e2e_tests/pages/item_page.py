from time import sleep

from e2e_tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ItemPage(BasePage):
    add_to_cart_button  = (By.XPATH, "//span[text()='Add to cart']")
    checkout_button = (By.ID, '<palcehodler>')
    product_price = (By.ID, '<palcehodler>')
    REMOVE_BTN = (By.CSS_SELECTOR, "[data-test-id='cart-remove-item']")


    def click_on_checkout(self):
        self.click(self.checkout_button)

    def add_to_cart(self, number_of_open_items=1):
        for _ in range(number_of_open_items):
            self.change_tab()
            self.click(self.add_to_cart_button)
            sleep(5) # Temporary wait to handle CAPTCHA triggered by rapid actions
            self.close_current_tab()
        self.change_tab()

    def remove_item(self):
        elements = self.get_elements(self.REMOVE_BTN)
        for i, el in enumerate(elements):
            sleep(2)  # Temporary wait to handle CAPTCHA triggered by rapid actions
            if i == len(elements)-1:
                self.get_element(self.REMOVE_BTN).click()
                break
            self.click(element=el)

