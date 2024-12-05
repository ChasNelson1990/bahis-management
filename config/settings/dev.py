import socket

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="vZk63gRGrV9xKtDH3uyIONbNOQiMQrq69vjhdCpaLyDIeT1Bau8kChVL1k9OKwJe",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "0.0.0.0", "127.0.0.1"])

# https://stackoverflow.com/questions/70612439/csrf-failed-origin-checking-failed-http-localhost8000-does-not-match-any
CSRF_TRUSTED_ORIGINS = env.list("DJANGO_CSRF_TRUSTED_ORIGINS")

# WhiteNoise
# ------------------------------------------------------------------------------
# http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
INSTALLED_APPS = ["whitenoise.runserver_nostatic"] + INSTALLED_APPS  # noqa: F405


# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa: F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa: F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["localhost", "0.0.0.0", "127.0.0.1"]

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
try:
    _, _, ips = socket.gethostbyname_ex("node")
    INTERNAL_IPS.extend(ips)
except socket.gaierror:
    # The node container isn't started (yet?)
    pass

# DEBUGGING FOR TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES[0]["OPTIONS"]["debug"] = True  # type: ignore # noqa: F405

# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa: F405

SESSION_ENGINE = 'redis_sessions.session'
redis_session_url = env.cache_url(
    'REDIS_SESSION_URL', default='redis://redis_cache:6380/2'
)
SESSION_REDIS = {
    'url': redis_session_url['LOCATION'],
    'prefix': env.str('REDIS_SESSION_PREFIX', 'session'),
    'socket_timeout': env.int('REDIS_SESSION_SOCKET_TIMEOUT', 1),
}

CACHES = {
    # Set CACHE_URL to override
    'default': env.cache_url(default='redis://redis_cache:6380/3'),
    'enketo_redis_main': env.cache_url(
        'ENKETO_REDIS_MAIN_URL', default='redis://change-me.invalid/0'
    ),
}

SESSION_COOKIE_NAME = env('DJANGO_SESSION_COOKIE_NAME')
SESSION_COOKIE_DOMAIN = env('DJANGO_SESSION_COOKIE_DOMAIN')
