import django.dispatch 

created = django.dispatch.Signal(providing_args=['apikey'])
authorized = django.dispatch.Signal(providing_args=['apikey'])
