from tornado import gen

from tornado_jwt import Authenticated

class EchoHandler(Authenticated):

    @gen.coroutine
    def post(self):
        self.send_json(200, self.body)
