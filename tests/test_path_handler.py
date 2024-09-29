import json

import ggps

from tests.helpers.unit_test_helper import UnitTestHelper

# pytest -v tests/test_path_handler.py


def test_str():
    handler = ggps.PathHandler()
    actual = str(handler)
    expected = "{}"
    assert actual == expected

    filename = "data/twin_cities_marathon.gpx"
    expected_trackpoint_count = 2256
    handler = ggps.PathHandler()
    handler.parse(filename)
    obj = json.loads(str(handler))
    assert obj["gpx|trk|trkseg|trkpt@lat"] == expected_trackpoint_count

    helper = UnitTestHelper(handler)
    # helper.assert_str()


def test_counts():
    filename = "data/twin_cities_marathon.gpx"
    expected_trackpoint_count = 2256
    handler = ggps.PathHandler()
    handler.parse(filename)
    counter = handler.path_counter
    assert counter["gpx|trk|trkseg|trkpt@lat"] == expected_trackpoint_count
    assert counter["gpx|metadata|time"] == 1
    assert handler.curr_depth() == 0


def test_base_parse_hhmmss():
    filename = "data/twin_cities_marathon.gpx"
    handler = ggps.PathHandler()
    handler.parse(filename)
    hhmmss = handler.parse_hhmmss("")
    assert hhmmss == ""
    hhmmss = handler.parse_hhmmss("xxx")
    assert hhmmss == ""
