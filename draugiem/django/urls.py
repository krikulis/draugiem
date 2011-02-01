from django.conf.urls.defaults import *



urlpatterns = patterns('draugiem_django.views',
    (r'^login/$', 'capture_url_parameters'),
)
