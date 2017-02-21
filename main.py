from tornado.web import Application
from tornado.ioloop import IOLoop

from router import routes
from config import settings

if __name__ == '__main__':
    try:
        Application(routes, **settings).listen(8081)
        IOLoop.current().start()
    except KeyboardInterrupt:
        IOLoop.current().stop()
