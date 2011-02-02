from django.conf.urls.defaults import *



urlpatterns = patterns('draugiem.django.views',
    (r'^login/$', 'capture_url_parameters'),
)
