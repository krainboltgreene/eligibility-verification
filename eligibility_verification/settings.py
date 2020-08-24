"""
Django settings for eligibility_verification project.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/

When moving to production, see the Deployment checklist
https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
"""
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DJANGO_DEBUG", False))

ADMIN = bool(os.environ.get("DJANGO_ADMIN", False))

TRANSIT_AGENCY = os.environ.get("DJANGO_TRANSIT_AGENCY", False)

ALLOWED_HOSTS = []

if DEBUG:
    ALLOWED_HOSTS.extend([
        'localhost',
        '127.0.0.1',
        '[::1]'
    ])

# Application definition

INSTALLED_APPS = [
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "eligibility_verification.core",
    "eligibility_verification.eligibility"
]

if ADMIN:
    INSTALLED_APPS.extend([
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
    ])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "eligibility_verification.core.middleware.DebugMiddleware",
    "eligibility_verification.core.middleware.TransitAgencyMiddleware"
]

if ADMIN:
    MIDDLEWARE.extend([
        "django.contrib.auth.middleware.AuthenticationMiddleware",
    ])

ROOT_URLCONF = "eligibility_verification.urls"

template_ctx_processors = [
    "django.template.context_processors.request",
    "django.contrib.messages.context_processors.messages",
]

if DEBUG:
    template_ctx_processors.extend([
        "django.template.context_processors.debug",
    ])

if ADMIN:
    template_ctx_processors.extend([
        "django.contrib.auth.context_processors.auth",
    ])

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": template_ctx_processors,
        },
    },
]

WSGI_APPLICATION = "eligibility_verification.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"]
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []

if ADMIN:
    AUTH_PASSWORD_VALIDATORS.extend([
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
    ])

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
