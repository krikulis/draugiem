from django.contrib.auth.models import User
from draugiem.django.api import api
from draugiem.api import APIError
from signals import created
from signals import authorized

class DraugiemIntegratedBackend(object):
    """ Draugiem iFrame application authentication backend """
    def get_user(self, user_id):
        try:
            return User.objects.get(pk = user_id)
        except User.DoesNotExist: 
            raise
            return False

    def authenticate(self, dr_auth_code = None):
        """
            provides signals:
                authorized - existing user authed
                created - user first auth 
        """ 
        try:
            user_data = api.authorize(dr_auth_code)
        except:
            raise
            return None
            
        try:
            user = User.objects.get(username = user_data['uid'])
            authorized.send(sender = user, 
                            api_key = user_data['apikey'])
        except User.DoesNotExist:
            user = User()
            user.username = user_data['uid']
            user.password = u'DRAUGIEM.LV'
            user.first_name = user_data['users'][user.username]['name']
            user.last_name = user_data['users'][user.username]['surname']
            user.save()
            user = User.objects.get(username = user_data['uid'])
            created.send(sender = user,
                         api_key = user_data['apikey'])

        return user

