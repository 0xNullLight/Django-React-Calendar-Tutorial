# If we are on RENDER, we will be using these settings.
# If we are not and on a local computer, we will use the settings that isn't tied to this file.

import os
import dj_database_url
from .settings import *
from .settings import BASE_DIR

ALLOWED_HOSTS [os.environ.get['RENDER_EXTERNAL_HOSTNAME']]
CORS_ALLOWED_ORIGINS = ['https//'+os.environ.get['RENDER_EXTERNAL_HOSTNAME']]
                                                 
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    # WhiteNoise is required to host Static Files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ALLOWED_ORIGINS = ['']

STORAGES = {
    "default":
        "BACKEND" : "django.core.files.storage.FileSystemStorage",
        },
    "staticfiles": {
        "BACKEND" : "whitenoise.storage.CompressedStaticFilesStorage", 
    }
    
DATABASES = {
    'default': dj_database_url.config(
        default = os.environ['DATABASE_URL'],
        conn_max_age=600
    )
}