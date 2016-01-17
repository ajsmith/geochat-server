#!/bin/bash

useradd geochat -d /var/lib/geochat
virtualenv --system-site-packages env
source env/bin/activate
python setup.py install
