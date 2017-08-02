from diary.settings.develop import *


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DIARY_DB_NAME'),
        'USER': os.getenv('DIARY_DB_USER'),
        'PASSWORD': os.getenv('DIARY_DB_PASSWORD'),
        'HOST': os.getenv('DIARY_DB_HOST'),
        'PORT': os.getenv('DIARY_DB_PORT'),
    }
}
