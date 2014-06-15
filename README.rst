===============
Geo Chat Server
===============

A simple location centric chat server.


Requirements
============

- Linux or similar operating system
- PostgreSQL
- PostGIS


Very Quick Start
================

To create a virtualenv::

    ./make_env.sh

To run the tests::

    ./test.sh

To use the virtualenv::

    . env/bin/activate

To install::

    python setup.py install

Alternatively, to install a development build::

    python setup.py develop

To initialize a database::

    geochat-initdb

To run the web server::

    geochatd
