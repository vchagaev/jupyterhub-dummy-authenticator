from jupyterhub.auth import Authenticator

from tornado import gen


class DummyAuthenticator(Authenticator):
    @gen.coroutine
    def authenticate(self, handler, data):
	if hasattr(data, 'password'):
	    setattr(self, 'test_token', data['password'])
        return data['username']
