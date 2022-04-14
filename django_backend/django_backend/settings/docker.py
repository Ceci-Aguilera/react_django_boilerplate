import environ
from .base import *

DEBUG = True

env = environ.Env()
# reading env file
environ.Env.read_env()

SECRET_KEY= env("SECRET_KEY")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:80",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_DOCKER_NAME'),
        'USER': env('DB_DOCKER_USER'),
        'PASSWORD': env('DB_DOCKER_PASSWORD'),
        'HOST': env('DB_DOCKER_HOST'),
        'PORT': env('DB_DOCKER_PORT'),
    }
}
