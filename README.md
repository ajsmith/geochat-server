# Geo Chat Server

A simple location centric chat server.

For the most part, this is a somewhat interesting pet project. This project
also serves as an example of Python web server development using web
microframeworks (bottle.py), database integration using SQL Alchemy, good
Python packaging and testing practices, and Docker based deployment.

If you happen to find a use for this project or have ideas for extending it, by
all means let me know, file an issue, or send me a pull request!

# Requirements

Under Docker the requirements are pretty simple: just have Docker installed and
running.

To perform builds or installations on a non-Docker enabled host, the
requirements are:

- Linux or similar operating system
- PostgreSQL
- PostGIS
- Python
- Python virtualenv
- Python psycopg2
- Python geos

# Compatibility

This software has been tested on Fedora Linux, but may also work on other
operating systems.

# Very Quick Start

The Very Quick Start uses the Docker based build.

Step 1: Run the tests:

```shell
$ ./test.sh
```

Step 2: Run the server:

```shell
$ docker run -d -p 8080:8080/tcp --link geochat-test-db:db ajsmith/geochat-server:testing
```

## What just happened?

The test script starts a PostgreSQL database container with PostGIS extensions
enabled, then builds the Geochat test images and runs the Python tests. The
test script leaves the DB running and the test images available for debugging,
and these can be used for typical testing and debugging purposes.
