#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requeriments.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --noinput
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('324', 'admin@example.com', '1')"