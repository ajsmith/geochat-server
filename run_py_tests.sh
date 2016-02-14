#!/bin/bash

cd $(readlink -f $(dirname $0))
source env/bin/activate
exec python setup.py test
