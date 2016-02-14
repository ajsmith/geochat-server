#!/bin/sh
set -e

cd $(dirname $0)

# Remove old test database, if exists.
docker stop geochat-test-db && docker rm geochat-test-db || true

# Launch a new test database.
docker run -d -p 5432:5432 --name geochat-test-db mdillon/postgis

# Build fresh images for testing.
docker build -t ajsmith/geochat-server:testing -f docker/Dockerfile .
docker build -t ajsmith/geochat-test:latest -f docker/Dockerfile.test .

# Run the tests.
docker run -i --link geochat-test-db:db --rm ajsmith/geochat-test

# Remove test images.
docker rmi ajsmith/geochat-test:latest
docker rmi ajsmith/geochat-server:testing
