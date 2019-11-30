from .base import *


DEBUG = config('DEBUG',cast=bool)
ALLOWED_HOSTS = []


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':config('DB-NAME'),
        'USER': config('DB-USER'),
        'PASSWORD':config('DB-PASSWORD') ,
        'HOST': config('DB-HOST'),
        'PORT':''
    }
}

STRIPE_PUBLIC_KEY = 'your-live-public-key'

STRIPE_SECRET_KEY = 'your-live-secret-key'