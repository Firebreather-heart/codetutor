from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['localhost', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sql8721138',
#         'USER': 'sql8721138',
#         'PASSWORD': 'KhDTVQgTk2',
#         'HOST': 'sql8.freesqldatabase.com',
#         'PORT': '3306', 
#     }
# }
