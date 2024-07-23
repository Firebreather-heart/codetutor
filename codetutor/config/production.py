from .base import * 
import cloudinary


DEBUG = True 
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_SAMESITE = 'Lax'
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_DOMAIN = '.onrender.com'
# SECURE_SSL_REDIRECT = True
# CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com', 'http://*.onrender.com',
#                         'https://codetutor-asuq.onrender.com'
#                         ]

X_FRAME_OPTIONS = 'SAMEORIGIN'
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


cloudinary.config(
    cloud_name='doyyzz5fy',
    api_key='154137597569181',
    api_secret='bvi1QQT0eFtYzfqVhu9BMgwt3mc',
    api_proxy="http://proxy.server:3128"
)
import cloudinary.uploader
import cloudinary.api
CLOUDINARY_URL = 'CLOUDINARY_URL=cloudinary://154137597569181:bvi1QQT0eFtYzfqVhu9BMgwt3mc@doyyzz5fy'

DEFAULT_FILE_STORAGE = 'codetutor.cloudinary_backend.CustomCloudinaryStorage'
