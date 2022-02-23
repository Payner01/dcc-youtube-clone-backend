# DONt share
SECRET_KEY = 'django-insecure-$-*c5gei%cikbqw&1eqj$7_%c3npk^^7xp#_x(8oc$zy(j3wus'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME':'drf_jwt_database',
        'USER': 'root',
        'PASSWORD': 'StickyBacon2000',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
