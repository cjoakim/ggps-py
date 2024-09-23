# ggps-py

ggps - gps file parsing utilities for garmin connect and garmin devices


## Urls

- GitHub: https://github.com/cjoakim/ggps-py
- PyPi: https://pypi.org/project/ggps/

## Features

- Create Distances in either miles, kilometers, or yards.
- Translates Distances to the other units of measure.
- Specify ElapsedTime either in 'hh:mm:ss' strings, or int second values.
- Calculates Speed from a given Distance and ElapsedTime - per mile, per kilometer, and per yard.
- Calculates pace_per_mile and seconds_per_mile for a given Speed.
- Projects one Speed to another Distance with either a simple or algorithmic formula.
- RunWalkCalculator calculates pace and mph from given time intervals and paces.
- Calculates the Age of person, and age_graded times.
- Calculates five standard heart-rate training zones based on Age.


## Quick start


### Installation

```
$ pip install ggps
```

### Use


#### Sample Program

See sample-program.py in the GitHub repo.

```

```

#### Sample Program Output

```

```

---

## Changelog

Current version: 0.4.0

-  2024/09/23, version 0.4.0,  Upgraded to python 3.12, pyproject.toml build mechanism, latest m26 >=0.3.1
-  2020/02/22, version 0.3.0,  Parsing improvements, normalize 'cadence' and 'heartratebpm' attribute names
-  2020/02/19, version 0.2.1,  Upgraded the m26 and Jinga2 libraries
-  2017/09/27, version 0.2.0,  Converted to the pytest testing framework
-  2017/09/26, version 0.1.13, packagin.
-  2016/11/07, version 0.1.12, updated packaging
-  2016/11/07, version 0.1.11, updated packaging
-  2016/11/07, version 0.1.10, updated packaging
-  2016/11/07, version 0.1.9,  updated packaging
-  2016/11/07, version 0.1.8,  updated packaging
-  2016/11/06, version 0.1.7,  updated description
-  2016/11/06, version 0.1.6,  republished
-  2016/11/06, version 0.1.5,  refactored ggps/ dir
-  2016/11/06, version 0.1.4,  refactored ggps/ dir. nose2 for tests
-  2015/11/07, version 0.1.3,  Added README.rst
-  2015/11/07, version 0.1.1   Initial release
