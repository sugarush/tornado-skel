from tornado_jwt import MemoryAuthenticator, MemoryDB

from config import settings

# from handlers.skel import *
from handlers.echo import EchoHandler

VERSION = settings['version']
r = lambda path: '/{version}{path}'.format(version=VERSION, path=path)

routes = [

    (r('/auth'), MemoryAuthenticator, { 'database': MemoryDB() }),
    (r('/echo'), EchoHandler)
]
