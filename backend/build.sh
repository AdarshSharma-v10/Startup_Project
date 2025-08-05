#!/usr/bin/env bash
set -e

apt-get update
apt-get install -y build-essential libjpeg-dev zlib1g-dev libfreetype6-dev

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --no-input
