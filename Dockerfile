FROM python:2.7-alpine3.7

MAINTAINER Adam Findlay "skylinerspeeder@gmail.com"


# Set up environment
WORKDIR /app
RUN apk add --no-cache build-base python-dev mariadb-dev postgresql-dev libffi-dev
RUN pip install --no-cache-dir psycopg2 gunicorn wget

# Download and extract sde
RUN wget https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
RUN bzip2 -v -d sqlite-latest.sqlite.bz2

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

RUN cp evething/local_settings.docker.py evething/local_settings.py

# Environment variables
ENV DB_ENGINE=mysql
ENV DB_NAME=evething2
ENV DB_USER=evething2
ENV DB_PASSWORD=potato
ENV DB_HOST=127.0.0.1
ENV DB_PORT=3306

ENV ESI_URL=https://esi.tech.ccp.is
ENV ESI_CLIENT_ID=0
ENV ESI_SECRET_KEY=a
ENV ESI_CALLBACK_URL=https://<your_host>/account/sso/callback/

ENV REDIS_URL=redis://127.0.0.1/0
ENV REDIS_KEY_PREFIX=evething2_


EXPOSE 8000

CMD "gunicorn" "-b 0.0.0.0:8000" "evething.wsgi:application"