FROM python:2.7-alpine3.7

MAINTAINER Adam Findlay "skylinerspeeder@gmail.com"

# Set up environment
WORKDIR /app
RUN apk add --no-cache build-base python-dev mariadb-dev libffi-dev wget curl
RUN pip install --no-cache-dir gunicorn

# Download and extract sde
#RUN wget https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
#RUN wget https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2.md5
#RUN bzip2 -v -d sqlite-latest.sqlite.bz2

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

RUN cp evething/local_settings.docker.py evething/local_settings.py
RUN chmod 777 evething/local_settings.py

ENV C_FORCE_ROOT=1

EXPOSE 8000

ENTRYPOINT "./init.sh"