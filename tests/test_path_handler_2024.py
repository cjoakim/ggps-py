import json

import ggps

import pytest

from tests.helpers.unit_test_helper import UnitTestHelper

# pytest -v tests/test_path_handler_2024.py


def test_twin_cities_marathon_gpx():
    expected_trackpoint_count = 2256
    filename = "data/twin_cities_marathon.gpx"
    handler = ggps.PathHandler()
    handler.parse(filename)

    helper = UnitTestHelper(handler)
    helper.assert_filename(filename)
    helper.assert_ggps_version()
    helper.assert_ggps_parsed_at()

    counter = handler.get_data()["path_counter"]
    assert counter["gpx|trk|trkseg|trkpt@lat"] == expected_trackpoint_count
    assert counter["gpx|metadata|time"] == 1
    helper.assert_str()
