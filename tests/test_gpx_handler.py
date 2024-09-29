import ggps

# pytest -v tests/test_gpx_handler.py


def expected_first_trackpoint():
    return {
      "type": "Trackpoint",
      "latitudedegrees": 44.97431952506304,
      "longitudedegrees": -93.26310088858008,
      "time": "2014-10-05T13:07:53.000Z",
      "heartratebpm": 85,
      "seq": 1,
      "elapsedtime": "00:00:00",
      "elapsedseconds": 0.0
    }


def expected_middle_trackpoint():
    return {
      "type": "Trackpoint",
      "latitudedegrees": 44.959017438814044,
      "longitudedegrees": -93.21290854364634,
      "time": "2014-10-05T16:21:12.000Z",
      "heartratebpm": 140,
      "seq": 1747,
      "elapsedtime": "03:13:19",
      "elapsedseconds": 11599.0
    }


def expected_last_trackpoint():
    return {
      "type": "Trackpoint",
      "latitudedegrees": 44.95180849917233,
      "longitudedegrees": -93.10493202880025,
      "time": "2014-10-05T17:22:17.000Z",
      "heartratebpm": 161,
      "seq": 2256,
      "elapsedtime": "04:14:24",
      "elapsedseconds": 15264.0
    }

def test_twin_cities_marathon_gpx_file():
    filename = "data/twin_cities_marathon.gpx"
    options = dict()
    handler = ggps.GpxHandler(options)
    handler.parse(filename)

    data = handler.get_data()
    tkpts = data["trackpoints"]


    actual = len(tkpts)
    expected = 2256
    assert actual == expected

    expected_attr_count = 8

    # check the first trackpoint
    expected_tkpt = expected_first_trackpoint()
    actual_tkpt = handler.trackpoints[0]
    assert len(actual_tkpt.values) == expected_attr_count
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert expected == actual

    # check a trackpoint at ~mile 20
    expected_tkpt = expected_middle_trackpoint()
    actual_tkpt = handler.trackpoints[1746]
    assert len(actual_tkpt.values) == expected_attr_count
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert expected == actual

    # check the last trackpoint
    expected_tkpt = expected_last_trackpoint()
    actual_tkpt = handler.trackpoints[-1]
    assert len(actual_tkpt.values) == expected_attr_count
    for key in expected_tkpt.keys():
        expected, actual = expected_tkpt[key], actual_tkpt.values[key]
        assert expected == actual

    # check seconds_to_midnight
    secs = int(handler.first_time_secs_to_midnight)
    assert secs > 0
    assert secs < 86400
