#!/bin/sh

# Run migrations
./manage.py migrate

# Collect static
./manage.py collectstatic

# Update the SDE if necessary
curl https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2.md5 > latest
if diff latest sqlite-latest.sqlite.bz2.md5 >/dev/null ; then
    wget https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
    bzip2 -d -v sqlite-latest.sqlite.bz2
    ./import.py
    wget https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2.md5