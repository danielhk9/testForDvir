import pytest

from e2e_tests.e2e_test_data import EXPECTED_NUMBER_OF_INVENTORY_ITEMS, EXPECTED_CART_COUNT_AFTER_ADDING_ONE_ITEM


def test_get_inventory_number_of_items(driver, login, inventory_setup):
    items = inventory_setup.get_inventory_items()
    assert len(items) == EXPECTED_NUMBER_OF_INVENTORY_ITEMS, f"Expected {EXPECTED_NUMBER_OF_INVENTORY_ITEMS} inventory items, but got different number {len(items)}."


@pytest.mark.parametrize('item_number_by_index', [0])
def test_add_single_item_to_cart(driver, login, inventory_setup, item_number_by_index):
    items = inventory_setup.get_inventory_items()
    first_item = items[item_number_by_index]
    inventory_setup.add_inventory_item_to_cart_by_index(first_item)
    cart_badge = inventory_setup.get_cart_item()
    assert cart_badge.text == EXPECTED_CART_COUNT_AFTER_ADDING_ONE_ITEM, (f"Cart badge should show {EXPECTED_CART_COUNT_AFTER_ADDING_ONE_ITEM} "
                                                                          f"instead of {cart_badge.text}, after adding one item to cart.")
    # Clean up: remove item so test is repeatable
    inventory_setup.remove_item_from_cart(first_item)
