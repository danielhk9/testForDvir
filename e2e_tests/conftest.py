import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from e2e_tests.config import BASE_URL
from e2e_tests.pages.home_page import HomePage
from e2e_tests.pages.item_page import ItemPage
from e2e_tests.pages.cart_page import CartPage
from e2e_tests.pages.filter_panel import FilterPanel

import pytest

@pytest.fixture(scope="session")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False
        })
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def open_ebay_page(driver):
    landing_page = HomePage(driver)
    search_bar = landing_page.verify_ebay_page_ready()
    assert search_bar, f"page failed to load! search bar was not found. Received: {search_bar}"



@pytest.fixture
def landing_page(driver):
    landing_page = HomePage(driver)
    return landing_page

@pytest.fixture
def item_page(driver):
    item_page = ItemPage(driver)
    yield item_page
    item_page.remove_item()

@pytest.fixture
def filter_panel(driver):
    filter_page = FilterPanel(driver)
    return filter_page

@pytest.fixture
def cart_page(driver):
    cart_page = CartPage(driver)
    return cart_page

@pytest.fixture()
def perform_search(item, landing_page):
    landing_page.search_for_item(item)

def search_results(landing_page):
    items = landing_page.get_items()
    assert items, f"No items were found for search term: {items}"
    return items.find_elements(By.TAG_NAME, "li")