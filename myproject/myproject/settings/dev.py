from .base import *
from os import environ

DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS += ('django_nose',)

SECRET_KEY = environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': environ['NAME'],
        'USER': environ['USER'],
        'PASSWORD': environ['PASSWORD'],
        'HOST': environ['DATABASE_HOST'],
        'PORT': environ['PORT'],
    }
}

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_URL = '/static/'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=insps',
]
