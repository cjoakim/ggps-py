#!/bin/bash

# Execute the unit tests with code coverage.
# Chris Joakim, 2026

source .venv/bin/activate

echo 'reformatting source code with ruff ...'
ruff format *.py
ruff format ggps 
ruff format tests

echo 'executing unit tests with code coverage ...'
pytest -v --cov=ggps/ --cov-report html tests/
