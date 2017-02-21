from tornado_jwt import MongoDBAuthenticator

from config import settings

# from handlers.skel import *

VERSION = settings['version']
r = lambda path: '/{version}{path}'.format(version=VERSION, path=path)

routes = [

    (r('/auth'), MongoDBAuthenticator),

    # (r('/skel'), SkelHandler)
]
