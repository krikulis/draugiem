from draugiem.api import Api as dr_api
from django.conf import settings

api = dr_api(settings.APP_CODE)
