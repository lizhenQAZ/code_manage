"""
Django settings for ttsx_part1 project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pozt6(65@rbf+*zw*6e^&*!5=!f$p+5%g2n7d_ae$3wmyrxq1n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', ]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 安装自定义应用
    'carts',
    'users',
    'goods',
    'order',
    # 按装富文本编辑器
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'users.middleware.RecordUrlMiddleware',  # 安装中间件记录跳转页面之前的url
)

ROOT_URLCONF = 'ttsx_part5.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'ttsx_part5.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ttsx_part5',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'mysql',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# 设置静态文件路径
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 设置图片路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images/goods')

# 配置tinymce
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    # 'theme': 'simple',
    'width': 600,
    'height': 400,
    'language': 'zh-CN',
    'theme_advanced_buttons1': 'bold, italic, underline, strikethrough, justifyleft, justifycenter, justifyright, '
                               'justifyfull, styleselect, bullist, numlist, outdent, indent, undo,redo, link, unlink, '
                               'image, cleanup, help, code, table, row_before, row_after, delete_row, separator, '
                               'rowseparator',
    'theme_advanced_buttons2': 'col_before, col_after, delete_col, hr, removeformat, sub, sup, formatselect, '
                               'fontselect, fontsizeselect, forecolor,charmap,visualaid,spacer,cut,copy,paste'
}

