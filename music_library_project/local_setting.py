# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)9zqww*)ez+oh5w04&py0vv7%(=mxx9i%ye=s4bb^2q=p@#g%&'

# SECURITY WARNING: don't run with debug turned on in production!

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST':'localhost',
        'USER': 'root',
        'PASSWORD': 'Password3',
            }
}