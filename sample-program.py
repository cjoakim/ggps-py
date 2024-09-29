import ggps

# Use:
# $ python sample-program.py > tmp/sample-program.txt


def parse_file(infile, handler_type):
    print("parsing file: {} type: {}".format(infile, handler_type))
    handler = None
    if handler_type == "tcx":
        handler = ggps.TcxHandler()
    elif handler_type == "gpx":
        handler = ggps.GpxHandler()
    else:
        handler = ggps.PathHandler()

    handler.parse(infile)
    #print(repr(handler))
    handler.write_json_file()


if __name__ == "__main__":

    print("ggps version {}".format(ggps.VERSION))

    # Latest files produced in 2024 with Forerunner 265S
    parse_file("data/activity_17075053124_lorimer_avinger.tcx", "tcx")
    parse_file("data/activity_17075053124_lorimer_avinger.tcx", "path")
    parse_file("data/activity_17075053124_lorimer_avinger.gpx", "gpx")
    parse_file("data/activity_17075053124_lorimer_avinger.gpx", "path")

    # Twin Cities Marathon files
    parse_file("data/twin_cities_marathon.tcx", "tcx")
    parse_file("data/twin_cities_marathon.tcx", "path")
    parse_file("data/twin_cities_marathon.gpx", "gpx")
    parse_file("data/twin_cities_marathon.gpx", "path")

    # New River 50K files
    parse_file("data/new_river_50k.tcx", "tcx")
    parse_file("data/new_river_50k.tcx", "path")
    parse_file("data/new_river_50k.gpx", "gpx")
    parse_file("data/new_river_50k.gpx", "path")

    # Davidson Track 5K files
    parse_file("data/dav_track_5k.tcx", "tcx")
    parse_file("data/dav_track_5k.tcx", "path")
    parse_file("data/dav_track_5k.gpx", "gpx")
    parse_file("data/dav_track_5k.gpx", "path")

    # activity_4564516081 files
    parse_file("data/activity_4564516081.tcx", "tcx")
    parse_file("data/activity_4564516081.tcx", "path")
    parse_file("data/activity_4564516081.gpx", "gpx")
    parse_file("data/activity_4564516081.gpx", "path")

    # activity_4564516081 files
    parse_file("data/activity_607442311.tcx", "tcx")
    parse_file("data/activity_607442311.tcx", "path")
    parse_file("data/activity_607442311.gpx", "gpx")
    parse_file("data/activity_607442311.gpx", "path")
