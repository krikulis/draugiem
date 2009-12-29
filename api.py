try:
    import json 
except ImportError:
    import simplejson as json 

import urllib

BASE_URL = "http://api.draugiem.lv/json/?%s"
""" draugiem.lv api base key """

class DraugiemAPIError(Exception):
    """ describes draugiem.lv api exceptions """
    pass

class api:
    """ 
        Draugiem.lv API wrapper  
        Attribute `user_key` defines user authorized api session key 
    """
    user_key = None
    """ user authorized api session key """
    def __init__(self, api_key, user_key = None):
       """ 
            Initialize Draugiem.lv API wrapper
            Argument key` is draugiem.lv API applications key, 
       """
       self.__api_key = api_key
       self.user_key = user_key
    def call(self, **kwargs):
        """ 
            Draugiem.lv API JSON call abstractor 
            Keyword arguments are converted to 
            URL arguments. Return converted response
            or raise DraugiemAPIError on error
        """
        if self.user_key is not None:
            kwargs['apikey'] = self.user_key
        kwargs['app'] = self.__api_key
        not_null = lambda item: item[1] is not None
        kwargs = dict(filter(not_null, kwargs.items()))
        arguments = urllib.urlencode(kwargs)
        response = urllib.urlopen(BASE_URL % arguments).read()
        response = json.loads(response)
        if 'error' in response:
            raise DraugiemAPIError(response['error'])
        return response
    def begin_authorization(self, email):
        """ 
            begin api authorization procedure
            return api authorization request key 
        """
        authcode = self.call(action = "authorize", email = email)['authcode']
        self.__authcode = authcode
        return authcode
    def finish_authorization(self, key = None, **kwargs):
        """
           finish authorization and return 
           permament user authorized session api 
           key
           Argument `key` respresents authorization
           request key, if it not given, last
           authorization request key is used 
           keyword argument - userinfo . If True, user information 
           also included in response
        """
        if key is None:
            key = self.__authcode
        result = self.call(action = "authorize", code = key)
        self.user_key = result['apikey']
        if 'userinfo' in kwargs and kwargs['userinfo'] == True:
            return result
        else: 
            return result['apikey']
    def counters(self, counter = None):
        """ 
           return user profile counters 
           if argument `counter` is given, only
           one specific counter is given, if not -
           dictionary of all of them. 
           for available counters see 
           http://www.draugiem.lv/development/?view=docs#d57e347
        """
        result = self.call(action = "counters")
        if(counter is not None):
            return result['counters'].get(counter, 0)
        else:
            return result['counters']
    def login_info(self):
        """
          return user profile information 
        """
        return self.call(action = "login")['login']
    def events(self, only_my = False, type = None, timestamp = None):
        """ 
          get last 15 activities  
          argument `only_my` controls friend activity display 
          argument `type` is list of displayed types - see `get_event_types` for
          supported types
          timestamp - date from to display user activities
        """
        args = {}
        if only_my == True:
            show = "my"
        else:
            show = "friends"
        if(type):
            types = ",".join(type)
        else:
            types = None
        return self.call(action = "activities", show = show, types = types, timestamp = timestamp)['events']

    def event_types(self):
        """
          return list of available event types 
        """
        return self.call(action = "event_types")['eventtypes']
    def messages(self, unread = False):
        """ 
          return list of messages
          only headings are available
          argument `unread` controls whenever 
          to read just unread messages
        """
        if unread is False:
            unread = None
        messages = self.call(action = "messages", show = unread)
        message_list = []
        for message in messages['messages'].items():
            message_list.append(dict(message[1]))
        for message in message_list:
            message['user'] = messages['users'][message['uid']]
        return message_list
    def app_friends(self, page = 1, limit = 20, just_id = False):
        """
          return user friends, who are using same application
          `page` = page number
          `limit` = users per page
          `just_id` = return just ids
        """
        if just_id is False:
            just_id = None
        return self.call(action = "app_friends", show = just_id, page = page, limit = limit)
