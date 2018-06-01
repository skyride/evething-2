#!/bin/sh
sleep 5

# Run migrations
./manage.py migrate

# Collect static
echo yes | ./manage.py collectstatic

gunicorn -b 0.0.0.0:8000 evething.wsgi:application