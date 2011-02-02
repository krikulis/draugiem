from draugiem.api import api as dr_api
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

if not hasattr(settings, 'DRAUGIEM_APP_KEY'):
    raise ImproperlyConfigured("DRAUGIEM_APP_KEY not in settings")
api = dr_api(settings.DRAUGIEM_APP_KEY)
