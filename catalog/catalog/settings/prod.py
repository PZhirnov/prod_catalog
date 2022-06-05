from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = 'django-insecure-x^1x6*yxebp5$dj2x=*0k=6^-5j0i3j5i4xnp+*(*1i9$y+tn+'
# MY_SECRET_KEY добавлен в переменную окружения ОС

# SECRET_KEY = dict(os.environ)['MY_SECRET_KEY']

DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalog',
        'USER': 'django',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}
