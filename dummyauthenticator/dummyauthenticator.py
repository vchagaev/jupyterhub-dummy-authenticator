from jupyterhub.auth import Authenticator

from tornado import gen


class DummyAuthenticator(Authenticator):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self._test_token = None

    @gen.coroutine
    def authenticate(self, handler, data):
        self.test_token = data['password']
        return data['username']

    @property
    def test_token(self):
        return self._test_token

    @test_token.setter
    def test_token(self, value):
        self._test_token = value


