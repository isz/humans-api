#!/bin/sh

docker run --rm -p 5432:5432 -d -v humans_volume:/var/lib/postgresql/data postgres