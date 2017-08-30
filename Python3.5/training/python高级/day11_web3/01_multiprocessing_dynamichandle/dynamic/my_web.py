import time
import re


g_templates_root = './templates'


def index(filename):
    filename = filename.replace('.py', '.html')
    try:
        fd = open(g_templates_root + filename, errors='ignore')
    except Exception as e:
        return '%s' % e
    else:
        content = fd.read()
        fd.close()
        replace_data = 'replace data!'
        content = re.sub(r'\{content\}', replace_data, content)
        return content


def center(filename):
    filename = filename.replace('.py', '.html')
    try:
        fd = open(g_templates_root + filename, errors='ignore')
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
    if filename == '/index.py':
        return index(filename)
    elif filename == '/center.py':
        return center(filename)
    else:
        return str(environ) + 'send to...>>%s' % time.ctime()