# -*- coding: utf-8; mode: python -*-
from milieu import Environment
import sys

env = Environment()

SELF = sys.modules[__name__]

from os.path import join, abspath


##########
# 3rd party stuff

GOOGLE_ANALYTICS_CODE = 'UA-46592615-1'


##########

LOCAL_PORT = 8000
PORT = env.get_int('PORT', LOCAL_PORT)
SCHEMA = PORT == 443 and 'https://' or "http://"
# Identifying environment
LOCAL = env.get('CONAUDIO_LOCAL_MODE') or (PORT is LOCAL_PORT)
SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')

# HTTP
HOST = env.get("HOST")
DOMAIN = env.get("DOMAIN")
absurl = lambda *path: "{0}{1}/{2}".format(
    SCHEMA, DOMAIN, "/".join(path).lstrip('/'))

sslabsurl = lambda *path: "{0}{1}/{2}".format(
    "https://", DOMAIN, "/".join(path).lstrip('/'))

BASE_URL = absurl("/")
STATIC_BASE_URL = absurl('/static/build/')

# setting up environment variables after all
if LOCAL:
    print "using custom localhost-specific settings"
    from .local import setup_localhost
    setup_localhost(SELF)

# Detecting environment
PRODUCTION = not LOCAL
DEBUG = not PRODUCTION
TESTING = env.get_bool('TESTING', False)
UNIT_TESTING = env.get_bool('UNIT_TESTING', False)


# Database-related
REDIS_URI = env.get_uri("REDIS_URI")


# Filesystem
LOCAL_FILE = lambda *path: abspath(join(__file__, '..', '..', *path))

# Security
SECRET_KEY = env.get("SESSION_SECRET_KEY")

# Logging
LOGGER_NAMES = [
    'conaudio',
    'conaudio.api.models',
    'conaudio.api.resources',
    'conaudio.framework.http',
    'conaudio.framework.db',
    'conaudio.web.models',
    'conaudio.web.controllers',
]

SALT = 'SGP#n>*3XJ)E9oubtmf"? bK'
GEO_IP_FILE_LOCATION = LOCAL_FILE('data', 'GeoIPCity.dat')

conaudio_path = abspath(join(__file__, '..', '..'))
FONT_AWESOME_PATH = '//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/'
