
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY ='5wuzid$bhshhgd%lm332f5x%q^5xbx+#=o%q6554_w!3trn'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "rest_framework",
    "django_rq",
    "django_cleanup.apps.CleanupConfig",
    "mgw_back.apps.MgwBackConfig",
    "mgw_front.apps.MgwFrontConfig",
]

ROOT_URLCONF = "matchering_web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

WSGI_APPLICATION = "matchering_web.wsgi.application"

DATA_DIR = os.path.join(BASE_DIR, "data")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(DATA_DIR, "db.sqlite3"),
    },
}

REST_FRAMEWORK = {
    "UNAUTHENTICATED_USER": None,
}

RQ_QUEUES = {
    "default": {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
    },
}

TIME_ZONE = "UTC"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(DATA_DIR, "media")
MEDIA_URL = "/media/"

MGW_STORE_DATA_FOR_MINUTES = 60
