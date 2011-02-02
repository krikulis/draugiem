def is_valid_iframe_request(request):
    if request.GET.has_key('dr_auth_status') and \
        request.GET.has_key('dr_auth_code') and \
        request.GET.has_key('session_hash') and \
        request.GET.has_key('domain'):
        return True
    else:
        return False

