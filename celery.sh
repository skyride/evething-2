#!/bin/sh
sleep 5

celery worker -A evething -B -c 8
