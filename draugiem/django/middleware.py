
class SafariFixMiddleware(object):
    """ force safari to accept iframe cookies """
    def process_request(self, request):
        if 'HTTP_USER_AGENT' not in request.META:
            return 
        if request.META['HTTP_USER_AGENT'].find("Safari") != -1 and \
            'session_id' not in request.COOKIES and \
            'cookie_fix' not in request.GET:
            return render_to_response("draugiem/safari_fix.html",
                                        {'get' : request.GET})

           
