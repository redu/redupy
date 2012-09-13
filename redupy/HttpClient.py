from rauth.service import OAuth2Service
import requests


class HttpClient(object):

    def __init__(self, consumer_key, consumer_secret, pin=None):
        self.redu = OAuth2Service(
        name='redu',
        authorize_url='http://redu.com.br/oauth/authorize',
        access_token_url='http://redu.com.br/oauth/token',
        consumer_key=consumer_key,
        consumer_secret=consumer_secret)
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        if pin:
            self.initClient(pin)

    def getAuthorizeUrl(self):
        return self.redu.get_authorize_url()

    def initClient(self, pin):
        data = dict(code=pin,
            grant_type="authorization_code",
            redirect_uri="")
        access_token = self.redu.get_access_token("POST",
            data=data).content["access_token"]
        self.client = requests.session(params={"oauth_token": access_token},
            headers={"Content-type": "application/json"})

    def get(self, url, **kargs):
        r = self.client.get(url, **kargs)
        return r

    def post(self, url, **kargs):
        r = self.client.post(url, **kargs)
        return r

    def delete(self, url, **kargs):
        r = self.client.delete(url, **kargs)
        return r

    def put(self, url, **kargs):
        r = self.client.put(url, **kargs)
        return r
