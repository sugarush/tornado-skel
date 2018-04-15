from tornado.options import options, parse_command_line

from tornado_json import log

options.logging = 'debug'
parse_command_line()

settings = {
    'autoreload': True,
    'provider': 'sugarush',
    'version': 'v1',
    'origin': '*',
    'secret': 'secret',
    'log_function': log,
    'serve_traceback': True
}
