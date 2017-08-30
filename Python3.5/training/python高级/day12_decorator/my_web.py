import time


def app(environ, start_handle):
    status = '200 OK'
    start_handle(status, [('Content-Type', 'text/plain')])
    return str(environ) + 'send to...>>%s' % time.ctime()