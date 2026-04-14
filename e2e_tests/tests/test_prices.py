import pytest
from e2e_tests.e2e_test_data import WATCH, APPLE, SHIRT, min_price, max_price
from e2e_tests.conftest import perform_search, search_results


@pytest.mark.parametrize("item", [WATCH])
def test_add_single_item_to_cart(driver,item_page,cart_page,landing_page,perform_search,filter_panel, item):
    all_item_prices = 0
    filter_panel.filter_by_price(min_price,max_price)
    filter_panel.filter_by_condition()
    items = search_results(landing_page)
    for i, item in enumerate(items):
        all_item_prices = landing_page.select_item_by_index(min_price,max_price,item)
        item_page.add_to_cart()
        if len(all_item_prices) == 2:
            break
    landing_page.click_on_cart()
    total_price = cart_page.get_total_price()
    assert sum(all_item_prices) == total_price, (
        f"Cart total price should match the selected items. "
        f"Expected: {all_item_prices}, Actual: {total_price}."
    )