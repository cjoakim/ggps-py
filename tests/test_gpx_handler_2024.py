import ggps

import pytest

# pytest -v tests/test_gpx_handler_2024.py


def expected_first_trackpoint():
    return {
        "cadence": "0",
        "elapsedtime": "00:00:00",
        "heartratebpm": "68",
        "latitudedegrees": "35.4942742176353931427001953125",
        "longitudedegrees": "-80.83952489309012889862060546875",
        "seq": "1",
        "time": "2024-09-19T11:05:15.000Z",
        "trackpointextension": "",
        "type": "Trackpoint",
    }


def expected_middle_trackpoint():
    return {
        "elapsedtime": "03:13:19",
        "heartratebpm": "140",
        "latitudedegrees": "44.959017438814044",
        "longitudedegrees": "-93.21290854364634",
        "seq": "1747",
        "time": "2014-10-05T16:21:12.000Z",
        "type": "Trackpoint",
    }


def expected_last_trackpoint():
    return {
        "cadence": "90",
        "cadencex2": "180",
        "elapsedtime": "00:46:17",
        "heartratebpm": "145",
        "latitudedegrees": "35.49437488429248332977294921875",
        "longitudedegrees": "-80.84005312062799930572509765625",
        "seq": "2778",
        "time": "2024-09-19T11:51:32.000Z",
        "trackpointextension": "",
        "type": "Trackpoint",
    }


# @pytest.mark.skip(reason="Temporarily disabled; refactoring to new/2024 data file")
def test_lorimer_avinger_gpx_file():
    filename = "data/activity_17075053124_lorimer_avinger.gpx"
    handler = ggps.GpxHandler()
    handler.parse(filename)

    tkpts = handler.trackpoints
    expected_attr_count = 7

    # check the number of trackpoints
    actual = len(tkpts)
    expected = 2256
    assert actual == expected

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
