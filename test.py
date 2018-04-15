from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application

from tornado.httpclient import HTTPRequest
from tornado.httputil import HTTPHeaders

from tornado_json import JSONHandler

from config import settings
from router import routes

class TestEchoHandler(AsyncHTTPTestCase):

    def get_app(self):
        self.token = None
        self.credentials = { 'username': 'user', 'password': 'pass' }
        return Application(routes, **settings)

    def login(self):
        response = self.fetch('/v1/auth',
            method='PUT',
            body=JSONHandler.encode(self.credentials)
        )
        if response.code == 401:
            response = self.fetch('/v1/auth',
                method='POST',
                body=JSONHandler.encode(self.credentials)
            )
        body = JSONHandler.decode(response.body)
        self.token = body['token']

    def request(self, path, **kargs):
        kargs['headers'] = HTTPHeaders({
            'Authorization': 'Bearer %s' % self.token
        })
        return self.fetch(path, **kargs)

    def test_echo_handler(self):
        self.login()
        response = self.request('/v1/echo',
            method = 'POST',
            body = JSONHandler.encode({ 'echo': 'hello world' })
        )
        self.assertEqual('{"echo":"hello world"}', response.body.decode('utf-8'))
