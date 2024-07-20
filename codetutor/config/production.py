from .base import * 

DEBUG = False 
ALLOWED_HOSTS = ['codetutor-asuq.onrender.com', 'www.codetutor-asuq.onrender.com']
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'codetutor',
#         'USER': 'sitemaker',
#         'PASSWORD': 'sitepass',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = '.onrender.com'
SECURE_SSL_REDIRECT = True
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com', 'http://*.onrender.com',
                        'https://codetutor-asuq.onrender.com'
                        ]

X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
