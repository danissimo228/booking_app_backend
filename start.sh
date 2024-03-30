python manage.py makemigrations --noinput || exit 1
python manage.py migrate --noinput || exit 1
python manage.py loaddata fixtures/admin.json
python manage.py runserver 0.0.0.0:8765