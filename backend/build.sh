set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# useful for Render when creating a superuser
if [[$CREATE_SUPERUSER]];
then
    python manage.py createsuperuser --no-input
fi