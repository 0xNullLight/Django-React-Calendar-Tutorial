set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# A variable with a dollar sign ($) in front is typically used to reference
# an environment variable or shell variable, especially in scripts or CI/CD pipelines.
# It can also act as a placeholder in documentation or templates where users are expected to substitute their own values.

# useful for Render when creating a superuser
# if [[$CREATE_SUPERUSER]];
# then
#     python manage.py createsuperuser --no-input
# fi

# Envrionment Variables that would be useful on Render:
#
# DATABASE_URL (This is the "Internal Database URL" after creating it on Render)
# SECRET_KEY
# CREATE_SUPERUSER (TRUE)
# DJANGO_SUPERUSER_USERNAME
# DJANGO_SUPERUSER_PASSWORD
# DJANGO_SUPERUSER_EMAIL