#!/bin/bash

# Execute the unit tests with code coverage.
# Chris Joakim, September 2024

source venv/bin/activate

echo 'reformatting source code with black ...'
black *.py
black ggps 
black tests

echo 'executing unit tests with code coverage ...'
pytest -v --cov=ggps/ --cov-report html tests/
