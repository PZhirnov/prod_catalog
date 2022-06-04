from .debug import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catalog',
        'USER': 'django',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '54325',
    }
}
