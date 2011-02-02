===============
Draugiem Python
===============
Draugiem ir python aplikācija  `draugiem.lv <http://www.draugiem.lv>`_ API
+ django aplikācija, lai veidotu draugiem.lv IFrame aplikācijas

Instalācija
===============
#. vajadzīgs Python > 2.4 (ja versija ir mazāka par 2.6, jāuzinstalē arī `simplejson <http://pypi.python.org/pypi/simplejson/>`_.
#. atarhivējam arhīvu un python setup.py install vai arī pip install draugiem

Django integrācija
===================
#. Pievienojam `draugiem.django` pie `INSTALLED_APPS`
#. norādam
    `AUTHENTICATION_BACKENDS = ('draugiem_django.backend.DraugiemIntegratedBackend', )`
#. pievienojam 
    `(r'^draugiem/', include('draugiem.django.urls')),`
#. uzliekam http://www.domēns.lv/draugiem/login/ kā aplikācijas URL draugiem.lv. Mums ir autorizējies lietotājs.


Licence
=======
bibliotēkas autors ir Kristaps Kūlis <kristaps.kulis@gmail.com>
2 clause BSD licence. Skatīt LICENCE. 
 
 
