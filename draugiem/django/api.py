
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


if not hasattr(settings, 'DRAUGIEM_APP_KEY'):
    raise ImproperlyConfigured("No DRAUGIEM_APP_KEY in settings.py ")

api = api(settings.DRAUGIEM_APP_KEY)
