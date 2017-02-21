from tornado.options import options, parse_command_line
from tornado.log import access_log

import motor.motor_tornado

options.logging = 'debug'
parse_command_line()

client = motor.motor_tornado.MotorClient()
api = client.api

def log_function(handler):
    if handler.get_status() < 400:
        log_method = access_log.info
    elif handler.get_status() < 500:
        log_method = access_log.warning
    else:
        log_method = access_log.error
    request_time = 1000.0 * handler.request.request_time()
    log_method("%s %s %s %d %s %.2fms", handler.uuid, handler.request.method, handler.request.uri, handler.get_status(), handler._reason, request_time)

settings = {
    'autoreload': True,
    'provider': 'sugarush',
    'version': 'v1',
    'origin': '*',
    'secret': 'secret',
    'api_db': api,
    'log_function': log_function,
    'serve_traceback': True
}
