# Django settings for earthvibration project.
import os.path

PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(PROJECT_DIR), 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Stockholm'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = False

USE_TZ = True

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(PROJECT_DIR)),
                          "media." + os.path.basename(PROJECT_DIR))
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(PROJECT_DIR)),
                           "static." + os.path.basename(PROJECT_DIR))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'earthvibration.urls'

WSGI_APPLICATION = 'earthvibration.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    # Optional commenting support
    'fluent_comments',
    'crispy_forms',
    'django.contrib.comments',
    # Some customizations
    #'comments',

    # External apps
    'taggit',
    #'taggit_autocomplete_modified',
    'sorl.thumbnail',


    # My apps:
    'polls',
    'home',
    'events',
    'blog',
    'djplayer',
    'discography',
    'gallery',
)

COMMENTS_APP = 'fluent_comments'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
DATETIME_FORMAT = 'N j, Y, H:i'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

try:
    from settings_secret import *
except ImportError, e:
    pass
