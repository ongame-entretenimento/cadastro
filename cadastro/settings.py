import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'r38!cjs^=jcr)5r%pw#-_^n#viy!%vlwlvay#ezi8lc$iir3ap'
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cadastro',
    'usuario',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'cadastro.urls'
WSGI_APPLICATION = 'cadastro.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cadastro',
        'USER': 'root'
    }
}
LANGUAGE_CODE = 'pt-BR'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ti/ogenv/src/cadastro/cadastro/static/'
TEMPLATE_DIRS = {
    '/home/ti/ogenv/src/cadastro/cadastro/templates/'
}
