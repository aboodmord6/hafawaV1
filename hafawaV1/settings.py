from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-x1qm)1yw8nw^4nqcum*8mjx!ou3tounh8faf2_u*z08bf5ws_t"
WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "BLXuDiHZy63CUW3nIP3fnuaR3QuHQIsjhOXBJKDnVK3GzOtQa2RJuqCPjyrI8QBs-Gtj9Een0DpvJ16-3CrzL6w",
    "VAPID_PRIVATE_KEY": "0H1hYr7-6Eli2-e_scSjxoh1XBTVXMCd3nKq7bnGn7Q",
    "VAPID_ADMIN_EMAIL": "aboodmord7@gmail.com",
}
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]
PWA_APP_DEBUG_MODE = False
PWA_APP_DISPLAY = "standalone"
PWA_APP_NAME = "hafawa"
PWA_APP_DESCRIPTION = "HI"
PWA_SPLASH_SCREEN = [
    {
        'src': "/static/app/splash_screens/iPhone_15_Pro_Max__iPhone_15_Plus__iPhone_14_Pro_Max_landscape.png",
        'media': "screen and (device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_15_Pro__iPhone_15__iPhone_14_Pro_landscape.png",
        'media': "screen and (device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_14_Plus__iPhone_13_Pro_Max__iPhone_12_Pro_Max_landscape.png",
        'media': "screen and (device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_14__iPhone_13_Pro__iPhone_13__iPhone_12_Pro__iPhone_12_landscape.png",
        'media': "screen and (device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_13_mini__iPhone_12_mini__iPhone_11_Pro__iPhone_XS__iPhone_X_landscape.png",
        'media': "screen and (device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_11_Pro_Max__iPhone_XS_Max_landscape.png",
        'media': "screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_11__iPhone_XR_landscape.png",
        'media': "screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_8_Plus__iPhone_7_Plus__iPhone_6s_Plus__iPhone_6_Plus_landscape.png",
        'media': "screen and (device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_8__iPhone_7__iPhone_6s__iPhone_6__4.7__iPhone_SE_landscape.png",
        'media': "screen and (device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/4__iPhone_SE__iPod_touch_5th_generation_and_later_landscape.png",
        'media': "screen and (device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/12.9__iPad_Pro_landscape.png",
        'media': "screen and (device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/11__iPad_Pro__10.5__iPad_Pro_landscape.png",
        'media': "screen and (device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/10.9__iPad_Air_landscape.png",
        'media': "screen and (device-width: 820px) and (device-height: 1180px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/10.5__iPad_Air_landscape.png",
        'media': "screen and (device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/10.2__iPad_landscape.png",
        'media': "screen and (device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/9.7__iPad_Pro__7.9__iPad_mini__9.7__iPad_Air__9.7__iPad_landscape.png",
        'media': "screen and (device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/8.3__iPad_Mini_landscape.png",
        'media': "screen and (device-width: 744px) and (device-height: 1133px) and (-webkit-device-pixel-ratio: 2) and (orientation: landscape)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_15_Pro_Max__iPhone_15_Plus__iPhone_14_Pro_Max_portrait.png",
        'media': "screen and (device-width: 430px) and (device-height: 932px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_15_Pro__iPhone_15__iPhone_14_Pro_portrait.png",
        'media': "screen and (device-width: 393px) and (device-height: 852px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_14_Plus__iPhone_13_Pro_Max__iPhone_12_Pro_Max_portrait.png",
        'media': "screen and (device-width: 428px) and (device-height: 926px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_14__iPhone_13_Pro__iPhone_13__iPhone_12_Pro__iPhone_12_portrait.png",
        'media': "screen and (device-width: 390px) and (device-height: 844px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_13_mini__iPhone_12_mini__iPhone_11_Pro__iPhone_XS__iPhone_X_portrait.png",
        'media': "screen and (device-width: 375px) and (device-height: 812px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_11_Pro_Max__iPhone_XS_Max_portrait.png",
        'media': "screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_11__iPhone_XR_portrait.png",
        'media': "screen and (device-width: 414px) and (device-height: 896px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_8_Plus__iPhone_7_Plus__iPhone_6s_Plus__iPhone_6_Plus_portrait.png",
        'media': "screen and (device-width: 414px) and (device-height: 736px) and (-webkit-device-pixel-ratio: 3) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/iPhone_8__iPhone_7__iPhone_6s__iPhone_6__4.7__iPhone_SE_portrait.png",
        'media': "screen and (device-width: 375px) and (device-height: 667px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/4__iPhone_SE__iPod_touch_5th_generation_and_later_portrait.png",
        'media': "screen and (device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/12.9__iPad_Pro_portrait.png",
        'media': "screen and (device-width: 1024px) and (device-height: 1366px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/11__iPad_Pro__10.5__iPad_Pro_portrait.png",
        'media': "screen and (device-width: 834px) and (device-height: 1194px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/10.9__iPad_Air_portrait.png",
        'media': "screen and (device-width: 820px) and (device-height: 1180px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/10.5__iPad_Air_portrait.png",
        'media': "screen and (device-width: 834px) and (device-height: 1112px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/10.2__iPad_portrait.png",
        'media': "screen and (device-width: 810px) and (device-height: 1080px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/9.7__iPad_Pro__7.9__iPad_mini__9.7__iPad_Air__9.7__iPad_portrait.png",
        'media': "screen and (device-width: 768px) and (device-height: 1024px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
    {
        'src': "/static/app/splash_screens/8.3__iPad_Mini_portrait.png",
        'media': "screen and (device-width: 744px) and (device-height: 1133px) and (-webkit-device-pixel-ratio: 2) and (orientation: portrait)"
    },
]
PWA_APP_ICONS = [
    {
        "src": "/static/app/android/android-launchericon-512-512.png",
        "sizes": "512x512",
    },
    {
        "src": "/static/app/android/android-launchericon-192-192.png",
        "sizes": "192x192",
    },
    {
        "src": "/static/app/android/android-launchericon-144-144.png",
        "sizes": "144x144",
    },
    {"src": "/static/app/android/android-launchericon-96-96.png", "sizes": "96x96"},
    {"src": "/static/app/android/android-launchericon-72-72.png", "sizes": "72x72"},
    {"src": "/static/app/android/android-launchericon-48-48.png", "sizes": "48x48"},
]
PWA_APP_ICONS_APPLE = [
    {"src": "/static/app/ios/16.png", "sizes": "16x16"},
    {"src": "/static/app/ios/20.png", "sizes": "20x20"},
    {"src": "/static/app/ios/29.png", "sizes": "29x29"},
    {"src": "/static/app/ios/32.png", "sizes": "32x32"},
    {"src": "/static/app/ios/40.png", "sizes": "40x40"},
    {"src": "/static/app/ios/50.png", "sizes": "50x50"},
    {"src": "/static/app/ios/57.png", "sizes": "57x57"},
    {"src": "/static/app/ios/58.png", "sizes": "58x58"},
    {"src": "/static/app/ios/60.png", "sizes": "60x60"},
    {"src": "/static/app/ios/64.png", "sizes": "64x64"},
    {"src": "/static/app/ios/72.png", "sizes": "72x72"},
    {"src": "/static/app/ios/76.png", "sizes": "76x76"},
    {"src": "/static/app/ios/80.png", "sizes": "80x80"},
    {"src": "/static/app/ios/87.png", "sizes": "87x87"},
    {"src": "/static/app/ios/100.png", "sizes": "100x100"},
    {"src": "/static/app/ios/114.png", "sizes": "114x114"},
    {"src": "/static/app/ios/120.png", "sizes": "120x120"},
    {"src": "/static/app/ios/128.png", "sizes": "128x128"},
    {"src": "/static/app/ios/144.png", "sizes": "144x144"},
    {"src": "/static/app/ios/152.png", "sizes": "152x152"},
    {"src": "/static/app/ios/167.png", "sizes": "167x167"},
    {"src": "/static/app/ios/180.png", "sizes": "180x180"},
    {"src": "/static/app/ios/192.png", "sizes": "192x192"},
    {"src": "/static/app/ios/256.png", "sizes": "256x256"},
    {"src": "/static/app/ios/512.png", "sizes": "512x512"},
    {"src": "/static/app/ios/1024.png", "sizes": "1024x1024"},
]
PWA_APP_SCREENSHOTS = [
    {
        "src": "/static/app/splash.png",
        "sizes": "1080x1920",
    }
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_htmx",
    # "storages",
    "django_user_agents",
    "webpush",
    #   Css famework
    "tailwind",
    "cssFramework",
    #   branches
    "Main",
    "ControlPanel",
    "visitor",
    "event",
    "pwa",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]

ROOT_URLCONF = "hafawaV1.urls"

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

WSGI_APPLICATION = "hafawaV1.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "Main.MyUser"
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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
TAILWIND_APP_NAME = "cssFramework"
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
LOGIN_URL = "login"
USER_AGENTS_CACHE = "default"
PWA_SERVICE_WORKER_PATH = BASE_DIR / "static/js/sw.js"


