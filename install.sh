#!/bin/bash

virtualenv --system-site-packages env
source env/bin/activate
python setup.py install
