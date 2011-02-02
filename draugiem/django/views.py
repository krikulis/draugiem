from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from draugiem.django.utils import is_valid_iframe_request
from django.contrib.auth import login 
from django.contrib.auth import logout 
from django.contrib.auth import authenticate
from django.conf import settings

def capture_url_parameters(request):
        context = RequestContext(request)
        if not is_valid_iframe_request(request): 
            return render_to_response("draugiem/use_draugiem.html", context)
        if request.session.get('session_hash'):
            new_hash = request.GET['session_hash']
            old_hash = request.session['session_hash']
            if new_hash != old_hash:
                logout(request)
        if not request.user.is_authenticated():
            user = authenticate(dr_auth_code = request.GET['dr_auth_code'])
            if user is None:
                return render_to_response("draugiem/use_draugiem.html", 
                                            context)
            login(request, user)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

