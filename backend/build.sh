#!/usr/bin/env bash
set -e

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --no-input

