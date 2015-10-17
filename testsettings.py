DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'encrypted_cookies',
)

# Pretend this is a random, secure key you created that was
# longer than 32 characters.
ENCRYPTED_COOKIE_KEY = 'IyMxemFqLW9kXmoyZGwhYl5vdDNsK2khNSkqMjQtcDg='

SECRET_KEY = 'stub-value-for-django'