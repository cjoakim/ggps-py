# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working
with code in this repository.

## What this project is

**ggps** is a Python library (published to PyPI) that parses GPX and TCX
fitness activity files downloaded from Garmin Connect.  It exposes three 
handler classes as its public API: TcxHandler, GpxHandler, and PathHandler.

## Commands

### Setup

```bash
./venv.sh          # Create/recreate .venv and install dependencies via uv
source .venv/bin/activate
```

### Running tests

```bash
./tests.sh                              # ruff format + full test suite with coverage
pytest -v tests/test_tcx_handler.py    # single test file
pytest -v -k "test_twin_cities"        # single test by name
```

### Linting / formatting

```bash
ruff format *.py ggps tests    # auto-format (run by tests.sh)
```

### Run the sample program

```bash
uv run sample-program.py
```

### Build for PyPI

```bash
./build.sh         # builds dist/ artifacts
# then: python3 -m twine upload --repository pypi dist/*
```

## Architecture

All three public handler classes inherit from `BaseHandler` (`ggps/base_handler.py`), which itself extends `xml.sax.ContentHandler`. Parsing is SAX-based (streaming, event-driven), not DOM.

**Handler hierarchy:**

```
xml.sax.ContentHandler
  └── BaseHandler          # shared SAX state, unit conversion, elapsed-time math
        ├── TcxHandler     # parses TCX (TrainingCenterDatabase XML)
        ├── GpxHandler     # parses GPX (GPS Exchange Format XML)
        └── PathHandler    # structural discovery — counts every XML path/attribute
```

**Key data flow:**

1. Caller instantiates a handler with an `opts` dict and calls `handler.parse(filename)`.
2. During SAX parsing, each handler tracks the current XML path via a `heirarchy` list (joined with `|`). Element data is accumulated on `self.curr_tkpt` (a `Trackpoint` instance) and appended to `self.trackpoints` when a trackpoint element closes.
3. After parsing (`endDocument`), `TcxHandler` computes derived fields (altitude in feet, distance in miles/km, `cadencex2`). `GpxHandler` does the same during its `parse()` call after SAX completes.
4. `BaseHandler.get_data()` serializes everything to a JSON-compatible dict. For TCX, it also computes `stats` with `heartbeat_data` and `cadence_data` histograms using `Counter`. Pass `opts["no-stats"] = True` to skip stats computation.
5. `Trackpoint.post_parse()` converts all string values collected during SAX parsing to correct numeric types (int/float).

**`PathHandler`** is different from the other two — it does not collect Trackpoints. Instead it counts every unique XML path (and attribute path) encountered, returning a `path_counter` dict. This is the tool for discovering the structure of an unfamiliar GPX/TCX file.

**`m26` library** is the only non-dev runtime dependency; it provides distance/unit conversions and `ElapsedTime` arithmetic.

**`run_walk_separator_cadence`** (default 150, configurable via `opts`) is the cadence threshold used in `stats` to distinguish running vs. walking trackpoints. TCX cadence values are steps-per-minute for one foot; `cadencex2` doubles this to both feet.

## Public API surface

```python
import ggps

handler = ggps.TcxHandler(opts)   # or GpxHandler / PathHandler
handler.parse("file.tcx")
data = handler.get_data()         # returns JSON-serializable dict
```

The `__init__.py` re-exports `Counter`, `Trackpoint`, `BaseHandler`, `GpxHandler`, `PathHandler`, `TcxHandler`, `VERSION`, and `DEFAULT_RUN_WALK_SEPARATOR_CADENCE`.

## Tests

Tests live in `tests/`. `tests/helpers/unit_test_helper.py` provides `UnitTestHelper`,
which wraps assertion helpers (`assert_first_trackpoint`, `assert_last_trackpoint`, etc.)
used across test files.

Test data files are in `data/` and are checked into the repo.
