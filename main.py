
from tornado import gen
from tornado.ioloop import IOLoop

@gen.coroutine
def main():
    pass

if __name__ == '__main__':
    IOLoop.current().run_sync(main)
