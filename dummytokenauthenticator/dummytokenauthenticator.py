from jupyterhub.auth import Authenticator

from tornado import gen


class DummyTokenAuthenticator(Authenticator):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.test_token = None

    @gen.coroutine
    def authenticate(self, handler, data):
        self.test_token = data['password']
        return data['username']
