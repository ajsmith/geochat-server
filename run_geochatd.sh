#!/bin/bash

cd $(readlink -f $(dirname $0))
source env/bin/activate
env/bin/geochatd
