#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requeriments.txt

python manage.py makemigrations
python manage.py collectstatic --no-input
python manage.py migrate auth
python manage.py migrate --run-syncdb
python manage.py migrate --fake-initial
#create superusers. Primer despliegue 
#python manage.py createsuperuser --noinput #take enviroment variables
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('324', 'admin@example.com', '1')"