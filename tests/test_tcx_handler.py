import ggps

from tests.helpers.unit_test_helper import UnitTestHelper

# pytest -v tests/test_tcx_handler.py


def expected_first_trackpoint():
    return {
        "type": "Trackpoint",
        "time": "2014-10-05T13:07:53.000Z",
        "latitudedegrees": 44.97431952506304,
        "longitudedegrees": -93.26310088858008,
        "altitudemeters": 259.20001220703125,
        "distancemeters": 0.0,
        "heartratebpm": 85,
        "speed": 0.0,
        "cadence": 89,
        "altitudefeet": 850.3937408367167,
        "distancemiles": 0.0,
        "distancekilometers": 0.0,
        "cadencex2": 178,
        "elapsedtime": "00:00:00",
        "seq": 1,
        "elapsedseconds": 0.0,
    }


def expected_trackpoint_1200():
    return {
        "type": "Trackpoint",
        "time": "2014-10-05T15:15:47.000Z",
        "latitudedegrees": 44.91043584421277,
        "longitudedegrees": -93.2357053924352,
        "altitudemeters": 270.79998779296875,
        "distancemeters": 21266.9296875,
        "heartratebpm": 140,
        "speed": 2.818000078201294,
        "cadence": 86,
        "altitudefeet": 888.4514035202387,
        "distancemiles": 13.214657455149426,
        "distancekilometers": 21.2669296875,
        "cadencex2": 172,
        "elapsedtime": "02:07:54",
        "seq": 1200,
        "elapsedseconds": 7674.0,
    }


def expected_last_trackpoint():
    return {
        "type": "Trackpoint",
        "time": "2014-10-05T17:22:17.000Z",
        "latitudedegrees": 44.95180849917233,
        "longitudedegrees": -93.10493202880025,
        "altitudemeters": 263.6000061035156,
        "distancemeters": 42635.44921875,
        "heartratebpm": 161,
        "speed": 3.5460000038146977,
        "cadence": 77,
        "altitudefeet": 864.8294163501167,
        "distancemiles": 26.492439912628992,
        "distancekilometers": 42.63544921875,
        "cadencex2": 154,
        "elapsedtime": "04:14:24",
        "seq": 2256,
        "elapsedseconds": 15264.0,
    }


def test_twin_cities_marathon_tcx_file():
    expected_trackpoint_count = 2256
    filename = "data/twin_cities_marathon.tcx"
    options = dict()
    handler = ggps.TcxHandler(options)
    handler.parse(filename)

    helper = UnitTestHelper(handler)
    helper.assert_filename(filename)
    helper.assert_ggps_version()
    helper.assert_ggps_parsed_at()

    helper.assert_trackpoint_count(expected_trackpoint_count)
    helper.assert_first_trackpoint(expected_first_trackpoint())
    helper.assert_last_trackpoint(expected_last_trackpoint())
    helper.assert_trackpoint_at_index(expected_trackpoint_1200(), 1199)
    helper.assert_str()
