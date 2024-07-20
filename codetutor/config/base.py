import os
import secrets
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "1L9zMfswTc3bPKTc64CKitQ69Xf1Gr6hVdiq1t52N4if7LH-HUxclzGoTC61mkot8Yo"


# Allowed hosts
ALLOWED_HOSTS = ['codetutor-asuq.onrender.com',]

# Application definition
INSTALLED_APPS = [

    # 3rd party
    'jazzmin',

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',

    # local

    'accounts',
    'codebase',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ROOT_URLCONF = 'codetutor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'codetutor.wsgi.application'


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['accounts.authbackends.CustomUserModelBackend']
LOGIN_REDIRECT_URL = 'home'

# Jazzmin settings
JAZZMIN_SETTINGS = {
    "site_title": "CodeTutor Admin",
    "site_header": "CodeTutor Admin",
    "welcome_sign": "Welcome to Codetutor admin",
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    # "changeform_format_overrides": {
    #     "yourapp.yourmodel": "vertical_tabs",
    # },
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "show_sidebar": True,
    "navigation_expanded": True,
    "language_chooser": False,
}


CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_DOMAIN = '.onrender.com'
SECURE_SSL_REDIRECT = False
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com', 'http://*.onrender.com',                     
                        'https://codetutor-asuq.onrender.com'
                        ]
