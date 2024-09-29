import ggps


def expected_first_trackpoint():
    return {
    }


def expected_middle_trackpoint() {
    return {
    }
}

def expected_last_trackpoint():
    return {
    }


def test_twin_cities_marathon_tcx_file():
    filename = "data/twin_cities_marathon.tcx"
    options = dict()
    handler = ggps.TcxHandler(options)
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
