#!/bin/sh
set -e

cd $(dirname $0)

rm -rf var
mkdir -p var/{data,run}
initdb var/data
postgres -D var/data -k $(pwd)/var/run -p 10000 2>&1 > var/log &
sleep 1
bash --rcfile env/bin/activate -c 'python setup.py test'
kill %1
