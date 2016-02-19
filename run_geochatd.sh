#!/bin/bash

cd $(readlink -f $(dirname $0))
source env/bin/activate
exec env/bin/geochatd --db-host db
