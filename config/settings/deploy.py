from .base import*

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(
    env_file = os.path.join(BASE_DIR, '.env')
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.mysql',	#mariaDB가 mysql에서 나온거라
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'password123',
        'HOST': 'mariadb',
        'PORT': '3306',							#mysql이 사용하는 포트가 3306임
    }
}