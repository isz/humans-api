#!/bin/sh

RETRIES=5

docker-compose build

until docker-compose run --rm humans_api /bin/bash -c "./manage.py migrate" || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 1
done