#!/bin/bash

# Recreate the python virtual environment and reinstall libs on mac/linux.
# Chris Joakim

# delete previous venv directory
mkdir -p venv 
rm -rf venv 

echo 'upgrading pip ...'
python3 -m pip install --upgrade pip

echo 'creating new python3 virtual environment in the venv directory ...'
python3 -m venv venv

echo 'activating new venv ...'
source venv/bin/activate

echo 'upgrading pip ...'
python -m pip install --upgrade pip 

echo 'install pip-tools ...'
pip install --upgrade pip-tools

echo 'displaying python location and version'
which python
python --version

echo 'displaying pip location and version'
which pip
pip --version

echo 'pip-compile requirements.in ...'
pip-compile --output-file requirements.txt requirements.in

echo 'pip install requirements.txt ...'
pip install -q -r requirements.txt

echo 'activating venv ...'
source venv/bin/activate

echo 'upgrading pip setuptools wheel ...'
pip install --upgrade pip setuptools wheel

echo 'pip list ...'
pip list > pip_list.txt
pip list

echo 'done'
