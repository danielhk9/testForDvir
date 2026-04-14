import pytest
import pytest
from e2e_tests.e2e_test_data import WATCH, APPLE, SHIRT, min_price, max_price
from e2e_tests.conftest import search_results


@pytest.mark.parametrize("search_term", [WATCH, APPLE, SHIRT])
def test_add_single_item_to_cart(driver,item_page,cart_page,landing_page,filter_panel, search_term):
    filter_panel.filter_by_price(min_price,max_price)
    items = search_results(search_term,landing_page)
    all_item_prices = landing_page.select_item_by_index(min_price,max_price,items,5)
    item_page.add_to_cart(5)
    landing_page.click_on_cart()
    total_price = cart_page.get_total_price()
    assert sum(all_item_prices) == total_price, (
        f"Cart total price should match the selected items. "
        f"Expected: {item_price}, Actual: {total_price}."
    )