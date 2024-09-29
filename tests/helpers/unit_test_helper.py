import pytest

import ggps

class UnitTestHelper(object):

    def __init__(self, parsed_data: dict):
        self.data = parsed_data

    def hey(self):
        print('hey!')

    def assert_filename(self, expected):
        actual = self.data["filename"]
        print("assert_filename; actual {}, expected: {}".format(actual, expected))
        assert actual == expected

    def assert_ggps_version(self):
        actual = self.data["ggps_version"]
        expected = ggps.VERSION
        print("assert_ggps_version; actual {}, expected: {}".format(actual, expected))
        assert actual == expected

    def assert_ggps_parsed_at(self):
        actual = self.data["ggps_parsed_at"]
        print("assert_ggps_parsed_at; actual {}".format(actual))
        assert actual.startswith("2024-")
        assert len(actual) == 26

    def assert_device_name(self, expected):
        actual = self.data["device_name"]
        print("assert_device_name; actual {}, expected: {}".format(actual, expected))
        assert actual == expected

    def assert_device_id(self, expected):
        actual = self.data["assert_device_id"]
        print("assert_device_id; actual {}, expected: {}".format(actual, expected))
        assert actual == expected

    def assert_trackpoint_count(self, expected):
        actual = len(self.data["trackpoints"])
        print("assert_trackpoint_count; actual {}, expected: {}".format(actual, expected))
        assert actual == expected

    def assert_first_trackpoint(self, expected:dict):
        actual = self.data["trackpoints"][0]
        print("assert_first_trackpoint; \n actual {}, \n expected: {}".format(actual, expected))
        assert actual == expected

    def assert_last_trackpoint(self, expected:dict):
        actual = self.data["trackpoints"][-1]
        print("assert_last_trackpoint; \n actual {}, \n expected: {}".format(actual, expected))
        assert actual == expected

    def assert_trackpoint_at_index(self, expected:dict, index:int):
        actual = self.data["trackpoints"][index]
        print("assert_trackpoint_at_index; \n actual {}, \n expected: {}".format(actual, expected))
        assert actual == expected
