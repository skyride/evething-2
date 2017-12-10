FROM python:2.7.14

RUN apt-get -q update && apt-get install -y -q \
  sqlite3 wget bzip2 libpq-dev python-dev \
  --no-install-recommends \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8

RUN pip install --upgrade pip virtualenv

RUN virtualenv /venv
ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install gunicorn

ADD . /app
RUN wget --directory-prefix=/app https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2
RUN bzip2 -d /app/sqlite-latest.sqlite.bz2

RUN rm /app/evething/settings.py
RUN cp /app/evething/settings.kube.py /app/evething/settings.py

CMD gunicorn -b :8000 evething.wsgi:application
