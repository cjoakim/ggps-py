import json
import xml.sax

from collections import defaultdict
from datetime import datetime

import m26

from ggps.trackpoint import Trackpoint
from ggps import VERSION


class BaseHandler(xml.sax.ContentHandler):

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.filename = None
        self.handler_type = None
        self.heirarchy = list()
        self.trackpoints = list()
        self.curr_tkpt = Trackpoint()
        self.curr_text = ""
        self.end_reached = False
        self.first_time = None
        self.first_etime = None
        self.first_time_secs_to_midnight = 0
        self.path_counter = defaultdict(int)
        self.version = VERSION

    def __str__(self):
        return "<ggps.BaseHandler type :{} filename: {}>".format(
            self.handler_type, self.filename
        )

    def __repr__(self):
        return json.dumps(self.get_data(), sort_keys=False, indent=2)

    def get_data(self) -> dict:
        """Return a JSON serializable dictionary of the data in this handler."""
        data = dict()
        data["filename"] = self.filename
        data["ggps_version"] = self.version
        data["ggps_parsed_at"] = str(datetime.now())

        if self.handler_type == "path":
            data["path_counter"] = self.path_counter
        else:
            data["trackpoint_count"] = self.trackpoint_count()
            data["trackpoints"] = list()
            for t in self.trackpoints:
                data["trackpoints"].append(t.values)
        return data

    def endDocument(self):
        self.completed = True

    def characters(self, chars):
        if self.curr_text:
            self.curr_text = self.curr_text + chars
        else:
            self.curr_text = chars

    def reset_curr_text(self):
        self.curr_text = ""

    def curr_depth(self):
        return len(self.heirarchy)

    def curr_path(self):
        return "|".join(self.heirarchy)

    def trackpoint_count(self):
        return len(self.trackpoints)

    def set_first_trackpoint(self, t):
        self.first_time = t.get("time")
        self.first_hhmmss = self.parse_hhmmss(self.first_time)
        self.first_etime = m26.ElapsedTime(self.first_hhmmss)
        self.first_time_secs = self.first_etime.secs

        # deal with the possibility that the Activity spans two calendar days.
        secs = int(m26.Constants.seconds_per_hour() * 24)
        self.first_time_secs_to_midnight = secs - self.first_time_secs

    def meters_to_feet(self, t, meters_key, new_key):
        m = t.get(meters_key)
        km = float(m) / 1000.0
        d_km = m26.Distance(km, m26.Constants.uom_kilometers())
        yds = d_km.as_yards()
        t.set(new_key, str(yds * 3.000000))

    def meters_to_km(self, t, meters_key, new_key):
        m = t.get(meters_key)
        km = float(m) / 1000.0
        t.set(new_key, str(km))

    def meters_to_miles(self, t, meters_key, new_key):
        m = t.get(meters_key)
        km = float(m) / 1000.0
        d_km = m26.Distance(km, m26.Constants.uom_kilometers())
        t.set(new_key, str(d_km.as_miles()))

    def cadence_x2(self, t):
        c = t.get("cadence", 0)
        i = int(c)
        if i > 0:
            t.set("cadencex2", str(i * 2))

    def calculate_elapsed_time(self, t):
        time_str = t.get("time")
        new_key = "elapsedtime"
        if time_str:
            if time_str == self.first_time:
                t.set(new_key, "00:00:00")
            else:
                curr_time = self.parse_hhmmss(time_str)
                curr_etime = m26.ElapsedTime(curr_time.strip())
                secs_diff = curr_etime.secs - self.first_time_secs
                if secs_diff < 0:
                    secs_diff = secs_diff + self.first_time_secs_to_midnight
                elapsed = m26.ElapsedTime(secs_diff)
                t.set(new_key, elapsed.as_hhmmss())

    def parse_hhmmss(self, time_str):
        """
        For a given datetime value like '2014-10-05T17:22:17.000Z' return the
        hhmmss value '17:22:17'.
        """
        if len(time_str) > 0:
            if "T" in time_str:
                return str(time_str.split("T")[1][:8])
            else:
                return ""
        else:
            return ""

    def write_json_file(self, pretty=True, verbose=True) -> None:
        """Write the parsed handler data to a file in the same directory, with a .json filetype."""
        outfile = "{}.{}.json".format(self.filename.strip(), self.handler_type)
        jstr = None
        if pretty is True:
            jstr = json.dumps(self.get_data(), sort_keys=False, indent=2)
        else:
            jstr = json.dumps(self.get_data())

        with open(file=outfile, encoding="utf-8", mode="w") as file:
            file.write(jstr)
            if verbose is True:
                print(f"file written: {outfile}")
