from .base import * 

DEBUG = False 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'codetutor',
        'USER': 'sitemaker',
        'PASSWORD': 'sitepass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}