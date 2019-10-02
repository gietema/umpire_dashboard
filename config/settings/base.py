from .defaults import *

# CONTEXT
PROJECT_NAME = env('PROJECT_NAME')
PROJECT_URL = "https://{}.nl".format(env('DOMAIN'))

# WSGI
WSGI_APPLICATION = 'core.wsgi.application'

# LOCAL APPS
INSTALLED_APPS += [
    'core',
    'users',
    'metrics',
    'stats',
]

# CRISPY FORMS
# ------------------------------------------------------------------------------
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs

INSTALLED_APPS = ['crispy_forms'] + INSTALLED_APPS
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_FAIL_SILENTLY = not DEBUG

# DJANGO WEBPACK LOADER
# ------------------------------------------------------------------------------
# https://github.com/owais/django-webpack-loader

INSTALLED_APPS += ['webpack_loader']
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'build/',
        'STATS_FILE': str(ROOT_DIR.path('webpack-stats.json')),
    }
}
STATICFILES_DIRS += [str(ROOT_DIR.path('frontend'))]
