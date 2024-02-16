"""
Django settings for footprime project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
# this module is used for using database on render website
import dj_database_url

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#tz&2r7z%iz-xjn(k113g1@n%2g1c0)wy%e097-oco%p^)b&m+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['footprime.shop', '13.233.143.94', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'paypal.standard.ipn',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'whitenoise.runserver_nostatic',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'adminpage',
    'cart_management',
    'user_profile',
    'wishlist',
    'coupon',
    'wallet',
    'payment.apps.PaymentConfig',
    'banner',
    'offer',
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

ROOT_URLCONF = 'footprime.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'footprime.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'footprime',
#         'USER': 'mysuperuser',
#         'PASSWORD': 'mysuperuser',
#         'HOST': 'footprime.c3coywe2eg5j.ap-southeast-2.rds.amazonaws.com',
#         'PORT': '5433',
#         # 'CONN_MAX_AGE': 6000,  # Increase the connection timeout to 600 seconds (10 minutes)
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

#database is created using render website
#https://dashboard.render.com/
DATABASES['default'] = dj_database_url.parse('postgres://mysuperuser:24ElI64pjrONjHsFdC00choJ3iZl3auv@dpg-cn6b9fmn7f5s73el5g10-a.singapore-postgres.render.com/footprime')





# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'  

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_USE_TLS = True
EMAIL_PORT = 587 
EMAIL_HOST_USER = 'prajun0604@gmail.com'  
EMAIL_HOST_PASSWORD = 'qqqt ayrz senq esqp'


#Paypal settings
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = 'sb-xytuh29127232@business.example.com'

#settings for s3 bucket in aws for static file storing in cloud
AWS_ACCESS_KEY_ID = 'AKIA5FTY7ZDAFA3HPYUM'
AWS_SECRET_ACCESS_KEY = 'COI+tVwS5PswrpKN3CPW4PFexnjRwiHf+CG6RR4Q'
AWS_STORAGE_BUCKET_NAME = 'footprime'
AWS_S3_SIGNATURE_NAME = 's3v4',
AWS_S3_REGION_NAME = 'ap-southeast-2'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

