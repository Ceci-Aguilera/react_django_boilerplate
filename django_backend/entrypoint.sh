#!/usr/bin/env bash
set -e

echo "Waiting for postgres to connect ..."

while ! nc -z database 5432; do
  sleep 0.1
done

echo "PostgreSQL is active"

python manage.py collectstatic --noinput
python manage.py migrate
python manage.py makemigrations

gunicorn django_backend.wsgi:application --bind 0.0.0.0:8000



echo "Postgresql migrations finished"

python manage.py runserver