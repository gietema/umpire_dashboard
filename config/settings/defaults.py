"""
Django settings for umpire_dashboard project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# PATHS & ENVIRONMENTAL VARIABLES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth

import environ
import os
import sys
from django.utils.translation import gettext_lazy as _

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("apps")
sys.path.append(str(APPS_DIR))

env = environ.Env(
    DEBUG=bool,
    DEBUG_TOOLBAR=bool,
)
env.read_env(str(ROOT_DIR.path(".env")))

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "users.User"

PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation."
             "UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation."
             "MinimumLengthValidator",
     "OPTIONS": {"min_length": 9}},
    {"NAME": "django.contrib.auth.password_validation."
             "CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation."
             "NumericPasswordValidator"},
]

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
PASSWORD_RESET_TIMEOUT_DAYS = 1

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#cache

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# DATABASE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#database

DATABASES = {
    "default": {
        "ENGINE": env("DATABASE_ENGINE"),
        "NAME": env("DATABASE_NAME", default='umpire'),
        "USER": env("DATABASE_USER", default='umpire'),
        "PASSWORD": env("DATABASE_PASSWORD", default=''),
        "HOST": 'localhost',
        "PORT": "",
        "ATOMIC_REQUESTS": True,
        # Lower CONN_MAX_AGE if postgres "too many connections" errors.
        "CONN_MAX_AGE": 60,
    }
}

# DEBUGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#debugging

DEBUG = env("DEBUG")

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#email
ADMINS = [
    ('Admin', env("ADMIN_EMAIL")),
]

# https://docs.djangoproject.com/en/2.2/ref/settings/#managers
MANAGERS = ADMINS 

if env("EMAIL_TYPE") == "mailhog":
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_PORT = 1025
    EMAIL_HOST = "localhost"
elif env("EMAIL_TYPE") == "smtp":
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env('EMAIL_HOST')
    EMAIL_PORT = env('EMAIL_PORT')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    EMAIL_USE_TLS = env('EMAIL_TLS', default=True)
else:
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = str(ROOT_DIR.path("tmp", "emails"))
    
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_FROM_EMAIL = '{} <info@{}>'.format(env('PROJECT_NAME'), env('EMAIL_DOMAIN'))
EMAIL_SUBJECT_PREFIX = "[{}]".format(env("PROJECT_SLUG"))
SERVER_EMAIL = "webmaster@{}".format(env("DOMAIN"))

# FILE UPLOADS & MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#file-uploads

FILE_UPLOAD_PERMISSIONS = 0o644
# TODO: What happens if you exceed FILE_UPLOAD_MAX_MEMORY_SIZE?
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760  # (10 MB)
MEDIA_ROOT = str(ROOT_DIR.path("media"))
MEDIA_URL = "/media/"

# GLOBALIZATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#globalization-i18n-l10n

USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR.path("locale"))]
TIME_ZONE = "Europe/Amsterdam"
LANGUAGE_CODE = "nl"
LANGUAGES = (
    ("en", _("English")),
)

# HTTP
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#http

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(',')

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
SECURE_HSTS_SECONDS = 63072000  # 2 years
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = False  # nginx
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# MODELS (INSTALLED APPS)
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#models

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django.contrib.sites",
    "django.contrib.staticfiles",
]

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#security

SECRET_KEY = env("DJANGO_SECRET_KEY")
X_FRAME_OPTIONS = "SAMEORIGIN"
CSRF_COOKIE_SECURE = env('CSRF_COOKIE_SECURE', default=True)
CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True


# SESSIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#sessions

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = env('CSRF_COOKIE_SECURE', default=True)


# SITES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#sites

SITE_ID = 1


# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#static-files

STATIC_ROOT = str(ROOT_DIR.path("frontend", "build"))
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR.path("static"))]
STATICFILES_FINDERS = [
    # FileSystemFinder looks in STATICFILES_DIRS
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#id12

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(APPS_DIR.path("templates")),
        ],
        "OPTIONS": {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.11/ref/settings/#urls

ROOT_URLCONF = "core.urls"
APPEND_SLASH = True

################################################################################
#                            THIRD PARTY SETTINGS                              #
################################################################################

# DJANGO EXTENSIONS
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/command_extensions.html

INSTALLED_APPS += ["django_extensions"]

