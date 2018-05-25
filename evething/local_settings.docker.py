# make a copy of this file as local_settings.py and edit that
import settings
import os

# switch this to True if you want to see crash information
# NEVER LEAVE THIS ON FOR A PUBLIC SITE
DEBUG = False

# If you keep DEBUG set to False you will need to set allowed hosts correctly.
# https://docs.djangoproject.com/en/1.5/ref/settings/#std%3asetting-ALLOWED_HOSTS
ALLOWED_HOSTS = []

# this is used for a few random things, it's a pretty good idea to change it
# http://www.miniwebtool.com/django-secret-key-generator/
# SECRET_KEY = ""

# these people will get e-mails with traceback information
ADMINS = (
    #('Freddie', 'freddie@wafflemonster.org'),
)

# database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' % os.environ.get("DB_ENGINE"),
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    },
    # this database should contain a current version of the Static Data Export
    'import': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite-latest.sqlite',
    },
}

# change this to the public facing directory for static files, needed for
# './manage.py collectstatic' to work
STATIC_ROOT = '/static'
# override the default '/static/' for static files
#STATIC_URL = 'http://static.evething.home'

# API host to use, change this if you have an API proxy handy
API_HOST = ''
# Number of _permanent_ API key failures per 7 days to trigger punishment,
# 0 to disable
API_FAILURE_LIMIT = 3

# ESI Details
# When you create the ESI application at developers.eveonline.com you should
# fill in this section
ESI_URL = os.environ.get("ESI_URL")
ESI_UPDATE_INTERVAL = 60  # How often to update in minutes
ESI_RETRIES = 15
ESI_DATASOURCE = "tranquility"
ESI_CLIENT_ID = ''
ESI_SECRET_KEY = ''
ESI_CALLBACK_URL = os.environ.get("ESI_CALLBACK_URL")

# IP addresses that will see some extra DEBUG info
INTERNAL_IPS = (
    '127.0.0.1',
)

# Disable the password tab if you are using external auth
DISABLE_ACCOUNT_PASSWORD = False

# Reject new API keys where keyid < MAX(keyid) added at least half an hour ago.
ONLY_NEW_APIKEYS = True

# Allow new users to register
ALLOW_REGISTRATION = True

# Default stagger APITask calls on startup
STAGGER_APITASK_STARTUP = True

# Market Data URL for prices
# - works on both eve-central or goonmetrics.
# PRICE_URL = 'http://api.eve-central.com/api/marketstat/?station_id=60003760&typeid=%s'
PRICE_URL = 'http://goonmetrics.com/api/price_data/?station_id=60003760&type_id=%s'

# Celery broker URL - http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker
BROKER_URL = 'amqp://guest:guest@localhost:5672/'

# Cache for various things. You really want to use memcache if at all
# possible, other caches do not guarantee atomic increments.
#
# https://docs.djangoproject.com/en/dev/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get("REDIS_URL"),
        'KEY_PREFIX': 'evething2_',
    }
}


# Use redis as the session handler
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'