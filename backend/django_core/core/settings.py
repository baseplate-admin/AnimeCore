"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mn19l@e%r^s&a^pa9%(bf173v-0c54^@3s(pb!ts_yuts0$+6p"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Increase this in future
# If you increase this make sure to run `migrations`
USERNAME_DISCRIMINATOR_LENGTH = 4

MAL_CLIENT_ID = os.environ.get("MAL_CLIENT_ID")
MAL_CLIENT_SECRET = os.environ.get("MAL_CLIENT_SECRET")

# Max retires for request
MAX_RETRY = 10
MAX_REQUESTS_PER_MINUTE = 55
REQUEST_STATUS_CODES_TO_RETRY = [408, 429, 500, 502, 503, 504]
BUCKET_NAME = "coreproject"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
]

# HOST configurations
# We are using this to hyperlink model relations

HOSTNAME = "http://127.0.0.1:8000"

# Application definition

INSTALLED_APPS = [
    # user must be above auth
    "apps.user",
    "apps.__discord__",
    # Django stuff
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Whitenoise
    "django.contrib.staticfiles",
    # Advanced Filters
    "advanced_filters",
    # Form tools
    "crispy_forms",
    "crispy_bootstrap5",
    # Rest Framework
    "ninja",
    # 3rd party rest framework stuff
    "corsheaders",
    # 3rd party Django stuff
    "django_cleanup.apps.CleanupConfig",
    "huey.contrib.djhuey",
    # APIS
    "apps.anime",
    "apps.trackers",
    "apps.characters",
    "apps.producers",
    "apps.studios",
    "apps.staffs",
]

# Debug Toolbar Add
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#install`-the-app
if DEBUG:
    INSTALLED_APPS += (
        "debug_toolbar",
        "dbbackup",  # django-dbbackup
        "django_browser_reload",
    )


MIDDLEWARE = [
    # Django Specific
    "django.middleware.security.SecurityMiddleware",
    # Whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Cors headers
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",  # Cache
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",  # Cache
]


# https://docs.djangoproject.com/en/4.0/topics/cache/#the-per-site-cache-1
CACHE_MIDDLEWARE_SECONDS = 0

# Debug Toolbar Middleware
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-middleware
if DEBUG:
    MIDDLEWARE += (
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "django_cprofile_middleware.middleware.ProfilerMiddleware",
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    )


# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips
if DEBUG:
    INTERNAL_IPS = [
        "127.0.0.1",
    ]
# Cookie override
CSRF_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_SAMESITE = "Strict"
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ASGI_APPLICATION = "core.asgi.application"

# Override the login url
# https://stackoverflow.com/questions/49532708/custom-login-url-in-django#49532812
LOGIN_URL = "login_page"

# Cache
# https://docs.djangoproject.com/en/4.0/topics/cache/#filesystem-caching

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "CONN_MAX_AGE": None,
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# POSTGRES
# https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "django",
#         "USER": "postgres",
#         "PASSWORD": "supersecretpassword",
#         "HOST": "",
#         "PORT": "",
#     }
# }

# Allow more fields to be deleted at once
# https://stackoverflow.com/questions/47585583/the-number-of-get-post-parameters-exceeded-settings-data-upload-max-number-field
DATA_UPLOAD_MAX_NUMBER_FIELDS = 50_000


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Custom user model
# https://testdriven.io/blog/django-custom-user-model/

AUTH_USER_MODEL = "user.CustomUser"

# Username or Email backend
# https://stackoverflow.com/questions/25316765/log-in-user-using-either-email-address-or-username-in-django#35836674

AUTHENTICATION_BACKENDS = ["apps.user.backends.EmailOrUsernameModelBackend"]

# Password hashers
# https://docs.djangoproject.com/en/3.2/topics/auth/passwords/#using-argon2-with-django

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    Path(BASE_DIR, "static"),
]

STATIC_ROOT = Path(BASE_DIR, "staticfiles")
# STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = Path(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# django-cors-headers settings
# https://pypi.org/project/django-cors-headers/

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://localhost:8000",
]

# settings.py -- alternative configuration method
# https://huey.readthedocs.io/en/latest/contrib.html#setting-things-up

from huey import PriorityRedisHuey
from redis import ConnectionPool

pool = ConnectionPool(host="localhost", port=6379, max_connections=20)
HUEY = PriorityRedisHuey(
    "coreproject_huey",
    use_zlib=True,
    compression=True,
    connection_pool=pool,
)

DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage"
DBBACKUP_STORAGE_OPTIONS = {"location": os.path.join(BASE_DIR, "backup")}

# Mappings from AIOHTTP
BASE_AIOHTTP_URL = "http://localhost:8000"
AIOHTTP_AVATAR_URL = f"{BASE_AIOHTTP_URL}/user/avatar/"  # /id

# Crispy forms
# https://github.com/django-crispy-forms/crispy-bootstrap5#usage

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
