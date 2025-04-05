#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r BBM/requirements.txt

cd BBM
python manage.py collectstatic --no-input
python manage.py migrate
