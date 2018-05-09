FROM python:2.7-alpine3.7

MAINTAINER Adam Findlay "skylinerspeeder@gmail.com"


# Set up environment
ADD . /app
WORKDIR /app

RUN apk add --no-cache --virtual .build-deps build-base python-dev mariadb-dev postgresql-dev libffi-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir psycopg2 gunicorn
RUN apk del .build-deps