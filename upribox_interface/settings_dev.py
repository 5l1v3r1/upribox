"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '12$&#v9$a8*%s$rjag665ydimo*av3cax=i9q93pp=_1v5-#=j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rq',
    'widget_tweaks',
    'www',
    'wlan',
    'vpn',
    'statistics',
    'devices',
    'more'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'www/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'de'

LANGUAGES = (
  ('de', 'Deutsch'),
  ('en', 'English'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "www/static"),
)

STATIC_ROOT = '/usr/local/static/upribox_interface/'

# Login config

LOGIN_URL = 'upri_login'

LOGIN_REDIRECT_URL = 'upri_index'

# Fixtures
FIXTURE_DIRS = (
    os.path.join(BASE_DIR, "www/dev_fixtures"),
    os.path.join(BASE_DIR, "www/prod_fixtures"),
)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s]%(message)s',
            'datefmt' : '%d/%b/%Y %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'err':{
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'out': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
        }
    },
    'loggers': {
        'uprilogger': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        "rq.worker": {
            "handlers": ['err', 'out'],
            "level": "DEBUG"
        },
    },
}

ANSIBLE_FACTS_DIR = '/etc/ansible/facts.d'
DEFAULT_SETTINGS = 'lib/default_settings.json'

# if this is set to true, lib.utils.exec_upri_config will always return 0 if
# /usr/local/bin/upri-config.py is missing
# this is meant for local debugging where things like SSID changes cannot
# be tested. In Production, this variable should be set to False
IGNORE_MISSING_UPRICONFIG = False

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'DEFAULT_TIMEOUT': 600,
    }
}

# Set the duration vpn profile download links are valid (in seconds)
VPN_LINK_TIMEOUT = 30

# Path to api.upribox.org certificate
SSL_PINNING_PATH = '/usr/local/etc/upri-filter-update/update-server.pem'

# Path to logfiles
PRIVOXY_LOGFILE = 'privoxy_testlog' #'/var/log/privoxy/privoxy.log'
OPENVPN_LOGFILE = '/var/log/log/openvpn.log'
DNS_FILE = '/etc/dnsmasq-resolv.conf'
