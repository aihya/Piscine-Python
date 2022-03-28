#!/bin/sh

#  Upgrade pip and setuptools. Install (if not installed) or upgrade wheel.
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install --upgrade wheel

#  Create .whl and .tar.gz
python setup.py bdist_wheel bdist