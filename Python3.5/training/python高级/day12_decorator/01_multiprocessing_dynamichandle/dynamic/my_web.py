import time
import re


g_templates_root = './templates'
g_url_handle = dict()


def route(url):
    def set_func(func):
        g_url_handle[url] = func
        def call_func(filename):
            return func(filename)
        return call_func
    return set_func


@route('/index.py')
def index(filename):
    filename = filename.replace('.py', '.html')
    try:
        fd = open(g_templates_root + filename)
    except Exception as e:
        return '%s' % e
    else:
        content = fd.read()
        fd.close()
        replace_data = 'replace data!'
        content = re.sub(r'\{content\}', replace_data, content)
        return content


@route('/center.py')
def center(filename):
    filename = filename.replace('.py', '.html')
    try:
        fd = open(g_templates_root + filename)
    except Exception as e:
        return '%s' % e
    else:
        content = fd.read()
        fd.close()
        replace_data = 'replace data!'
        content = re.sub(r'\{content\}', replace_data, content)
        return content


def app(environ, start_handle):
    status = '200 OK'
    start_handle(status, [('Content-Type', 'text/html')])
    filename = environ['PATH_INFO']
    try:
        return g_url_handle[filename](filename)
    except:
        return str(environ) + 'send to...>>%s' % time.ctime()
