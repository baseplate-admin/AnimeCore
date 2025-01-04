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

# https://github.com/typeddjango/django-stubs/tree/54a1e894257f6eea49b63fcd3a6eb89af00daf55/django_stubs_ext#usage
import django_stubs_ext

django_stubs_ext.monkeypatch()

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-mn19l@e%r^s&a^pa9%(bf173v-0c54^@3s(pb!ts_yuts0$+6p",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get("DEBUG") else True
# DEBUG = True

# Increase this in future
# If you increase this make sure to run `migrations`
DISCRIMINATOR_LENGTH = 4


# Our Secret Keys
MAL_CLIENT_ID = os.environ.get("MAL_CLIENT_ID")
MAL_CLIENT_SECRET = os.environ.get("MAL_CLIENT_SECRET")
# Stream SB
STREAMSB_KEY = os.environ.get("STREAMSB_KEY")
# Stream Tape
STREAMTAPE_LOGIN = os.getenv("STREAMTAPE_LOGIN")
STREAMTAPE_KEY = os.getenv("STREAMTAPE_KEY")
STREAMTAPE_PARENT_FOLDER_ID = os.getenv("STREAMTAPE_PARENT_FOLDER_ID")


# HOST configurations
# We are using this to hyperlink model relations

SITE_ADDRESS = os.environ.get("SITE_ADDRESS")

# Application definition

INSTALLED_APPS = [
    # user must be above auth
    "apps.user",
    # Django stuff
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # Humanize
    "django.contrib.humanize",
    # Postgres
    "django.contrib.postgres",
    # HTMX
    "django_htmx",
    # Whitenoise
    "whitenoise.runserver_nostatic",
    # Components
    "django.contrib.staticfiles",
    # 3rd party rest framework stuff
    "corsheaders",
    # 3rd party Django stuff
    "django_cleanup.apps.CleanupConfig",
    # 3rd Party Models
    "colorfield",
    # 3rd party adminpanel
    "django_hstore_widget",
    # Block users
    "defender",
    # Tree
    "django_ltree",
    # Api
    "rest_framework",
    "rest_framework.authtoken",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "django_filters",
    # Crispy forms
    "crispy_forms",
    "crispy_bootstrap4",
    # Vite Plugin
    "django_vite",
    # Models
    "apps.comments",
    "apps.pages",
    "apps.anime",
    "apps.trackers",
    "apps.characters",
    "apps.producers",
    "apps.staffs",
    "apps.episodes",
    "apps.torrent",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

SILENCED_SYSTEM_CHECKS = [
    "rest_framework.W001",
]
# Rest framework
REST_FRAMEWORK = {
    # YOUR SETTINGS
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "PAGE_SIZE": 100,
}
SPECTACULAR_SETTINGS = {
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    # OTHER SETTINGS
}
# Debug Toolbar Add
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#install-the-app
if DEBUG:
    INSTALLED_APPS += (
        "debug_toolbar",
        "dbbackup",  # django-dbbackup
        # Django browser Reload
        "django_browser_reload",
        # Django extensions
        "django_extensions",
    )


MIDDLEWARE = [
    # HTMX
    "django_htmx.middleware.HtmxMiddleware",
    # Django Specific
    "django.middleware.security.SecurityMiddleware",
    # Whitenoise
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Cors headers
    "corsheaders.middleware.CorsMiddleware",
    # Django
    "django.middleware.cache.UpdateCacheMiddleware",  # Cache
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",  # Cache
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Django defender
    "defender.middleware.FailedLoginMiddleware",
]

if DEBUG:
    MIDDLEWARE += (
        # Debug Toolbar Middleware
        # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-middleware
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        # CProfile middleware
        # https://github.com/omarish/django-cprofile-middleware/blob/80e27f3876949e0d9c452c0e48ed03d73e026b73/README.md#installing
        "django_cprofile_middleware.middleware.ProfilerMiddleware",
        # Browser Reload Middleware
        # "django_browser_reload.middleware.BrowserReloadMiddleware",
    )

# https://docs.djangoproject.com/en/4.0/topics/cache/#the-per-site-cache-1
CACHE_MIDDLEWARE_SECONDS = int(os.environ.get("CACHE_MIDDLEWARE_SECONDS", 0))


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
                # Custom
                "apps.pages.context_processors.urls",
                "apps.pages.context_processors.request_dict",
            ],
        },
    },
]

ASGI_APPLICATION = "core.asgi.application"

# Override the default redis_url
# Hours wasted -> 3
DEFENDER_REDIS_URL = os.environ.get("DEFENDER_REDIS_URL", "redis://127.0.0.1:6379")


# Override the login url
# https://stackoverflow.com/questions/49532708/custom-login-url-in-django#49532812
LOGIN_URL = "login_page"

# Cache
# https://docs.djangoproject.com/en/4.0/topics/cache/#filesystem-caching

if CACHE_MIDDLEWARE_SECONDS != 0:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": os.environ.get("DJANGO_CACHE_LOCATION", "redis://127.0.0.1:6379"),
        }
    }

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# POSTGRES
# https://www.enterprisedb.com/postgres-tutorials/how-use-postgresql-django

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # Database name
        "NAME": os.environ.get("POSTGRES_NAME", "coreproject"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "supersecretpassword"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", 5432),
        # https://stackoverflow.com/questions/23504483/django-conn-max-age-setting-error
        # "CONN_MAX_AGE": 10,
        "CONN_HEALTH_CHECKS": True,
    }
}

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
    Path(BASE_DIR, "static_src"),
]

STATIC_ROOT = Path(BASE_DIR, "staticfiles")

# Enable when django 4.2 is released
# http://whitenoise.evans.io/en/latest/django.html#add-compression-and-caching-support
# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

MEDIA_URL = "/media/"
MEDIA_ROOT = Path(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# django-cors-headers settings
# https://pypi.org/project/django-cors-headers/


CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS = []

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

if environs := os.environ.get("DJANGO_ALLOWED_HOSTS"):
    environ = environs.split(" ")
    ALLOWED_HOSTS += environ

for entry in ALLOWED_HOSTS:
    CORS_ALLOWED_ORIGINS.append(f"https://{entry}")
    CSRF_TRUSTED_ORIGINS.append(f"https://{entry}")

# Uncomment this following block to allow access to only subdomains
# if SITE_ADDRESS:
#    SITE_ADDRESS_ESCAPED = SITE_ADDRESS.replace(".", "\\.")
#    CORS_ALLOWED_ORIGIN_REGEXES = [
#        rf"^(https?:\/\/)?([\w-]+\.)?{SITE_ADDRESS_ESCAPED}$",
#    ]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_CREDENTIALS = True

DBBACKUP_STORAGE = "django.core.files.storage.FileSystemStorage" if DEBUG else ""
DBBACKUP_STORAGE_OPTIONS = {"location": os.path.join(BASE_DIR, "backup")}

# https://django-tailwind.readthedocs.io/en/latest/installation.html

TAILWIND_APP_NAME = "tailwind_src"
if os.name == "nt":
    NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
elif os.name == "posix":
    NPM_BIN_PATH = "/usr/bin/npm"

# WhiteNoise Patch

import re

# Vite generates files with 8 hash digits
# http://whitenoise.evans.io/en/stable/django.html#WHITENOISE_IMMUTABLE_FILE_TEST


def immutable_file_test(path, url):
    # Match filename with 12 hex digits before the extension
    # e.g. app.db8f2edc0c8a.js
    return re.match(r"^.+\.[0-9a-f]{8,12}\..+$", url)


WHITENOISE_IMMUTABLE_FILE_TEST = immutable_file_test
DJANGO_VITE = {
    "default": {
        "dev_mode": DEBUG,
        "dev_server_port": 5173,
    },
}
# Where ViteJS assets are built.
DJANGO_VITE_ASSETS_PATH = BASE_DIR / "static"
