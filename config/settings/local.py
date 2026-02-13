
from decouple import config #noqa
from .base import *  # noqa


#---------------------------------------#
# Secret Key and Debug Configuration
#---------------------------------------#

SECRET_KEY = config("SECRET_KEY", default="unsafe-dev-key")

DEBUG = config("DEBUG", cast=bool, default=True)



#--------------------------------------- #
# Hosts
#---------------------------------------#

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


#--------------------------------------- #
# Admin URL Configuration
#---------------------------------------#
ADMIN_URL = config("ADMIN_URL", default="admin/")


SITE_NAME = config("SITE_NAME", default="Standard Bank API")


#--------------------------------------- #
# Celery Email Configuration
#---------------------------------------#
EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
CELERY_EMAIL_BACKEND = config(
    "CELERY_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)


#--------------------------------------- #
# Email Settings
#---------------------------------------#
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_PORT = config("EMAIL_PORT", default=25, cast=int)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="jobbee <noreply@jobbee.com>")


#--------------------------------------- #
# Domain Configuration
#---------------------------------------#
# Domain Configuration
#---------------------------------------#
DOMAIN = config("DOMAIN", default="localhost:8000")


#--------------------------------------- #
# Image Configuration
#---------------------------------------#

MAX_UPLOAD_SIZE = 1 * 1024 * 1024  # 1 MB