import logging

import allure

from api_tests.api_test_data import expected_airports, airports_distance, EXPECTED_DISTANCE, EXPECTED_NUMBER_OF_AIRPORTS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@allure.feature("Login")
@allure.story("Valid credentials")
def test_verify_airport_count(get_airports_data):
    logger.info("Starting validate airport count")
    assert len(get_airports_data) == EXPECTED_NUMBER_OF_AIRPORTS, f"Expected {EXPECTED_NUMBER_OF_AIRPORTS} airports but got {len(get_airports_data)}"


def test_verify_specific_airports(get_airports_data):
    logger.info("Starting specific airport validation test")
    airports = get_airports_data
    airport_names = [airport["attributes"]["name"] for airport in airports]
    for expected in expected_airports:
        assert expected in airport_names, f"Expected airport '{expected}' not found."


def test_distance_between_two_airports(post_distance_between_airports):
    logger.info("Starting validate distance between two airport")
    response_json = post_distance_between_airports(airports_distance)
    kilometers = response_json["attributes"]["kilometers"]
    assert kilometers > EXPECTED_DISTANCE, f"Distance should be greater than 400 km, but got {kilometers} km"
