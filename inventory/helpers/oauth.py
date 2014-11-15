# -*- coding: utf-8 -*-
__author__ = 'Jaeyoung'

from flask.ext.oauthlib.client import OAuth
from settings import FACEBOOK_OAUTH

facebook_oauth = OAuth()
facebook = facebook_oauth.remote_app('facebook',
                                     base_url='https://graph.facebook.com/',
                                     request_token_url=None,
                                     access_token_url='/oauth/access_token',
                                     authorize_url='https://www.facebook.com/dialog/oauth',
                                     consumer_key=FACEBOOK_OAUTH.get('APP_ID', ''),
                                     consumer_secret=FACEBOOK_OAUTH.get('APP_SECRET', ''),
                                     request_token_params={'scope': 'email'})


class FacebookProfileFetcher(object):
    def __init__(self, access_token, fields):
        self.access_token = access_token
        self.fields = fields

    def fetch(self):
        fields_str = ','.join(self.fields)
        param = {
            'access_token': self.access_token,
            'locale': 'ko_KR',
            'fields': fields_str,
        }
        r = facebook.get('/me', data=param)
        return r
