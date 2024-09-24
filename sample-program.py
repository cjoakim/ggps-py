import ggps

# Use:
# $ python sample-program.py > tmp/sample-program.txt


def parse_file(infile, handler_type):
    print("processing file: {} type: {}".format(infile, handler_type))
    handler = None
    if handler_type == "tcx":
        handler = ggps.TcxHandler()
    elif handler_type == "gpx":
        handler = ggps.GpxHandler()
    else:
        handler = ggps.PathHandler()

    handler.parse(infile)
    print(repr(handler))
    handler.write_json_file()


if __name__ == "__main__":

    print("ggps version {}".format(ggps.VERSION))

    # Twin Cities Marathon files
    parse_file("data/twin_cities_marathon.tcx", "tcx")
    parse_file("data/twin_cities_marathon.tcx", "path")
    parse_file("data/twin_cities_marathon.gpx", "gpx")
    parse_file("data/twin_cities_marathon.gpx", "path")

    # Latest files produced in 2024 with Forerunner 265S
    parse_file("data/activity_17075053124_lorimer_avinger.tcx", "tcx")
    parse_file("data/activity_17075053124_lorimer_avinger.tcx", "path")
    parse_file("data/activity_17075053124_lorimer_avinger.gpx", "gpx")
    parse_file("data/activity_17075053124_lorimer_avinger.gpx", "path")
