import urllib.request


# 四个模块:request、error、parse、robotparser
# url = "https://www.douban.com/login"
# f = urllib.request.urlopen(url)
# print("---1---", f.read(300))
# print("---2---", f.read(300).decode('utf-8'))

# url = "https://www.douban.com/login"
# f = urllib.request.urlopen(url=url, data="this is CGI".encode('utf-8'))
# print("---3---", f.read())
# f = urllib.request.urlopen(url=url, data="this is CGI".encode('utf-8'))
# print("---4---", f.read().decode('utf-8'))
#
# import sys
# data = sys.stdin.read()
# print('---5---', 'Content-type: text/plain\n\nGot Data: "%s"' % data)

# DATA = b'some data'
# req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
# with urllib.request.urlopen(req) as f:
#     pass
# print('---6---', f.status)
# print('---7---', f.reason)

# 增加认证
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# f = urllib.request.urlopen('http://www.example.com/login.html')
# print('---8---', f.read())

# 增加IP代理
# proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
# opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# opener.open('http://www.example.com/login.html')

# 增加请求头
# req = urllib.request.Request('http://www.example.com/')
# req.add_header('Referer', 'http://www.python.org/')
# req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
# r = urllib.request.urlopen(req)
# print(r.read())

# 增加url编码处理get请求
# import urllib.parse
# params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# url = "http://www.musi-cal.com/cgi-bin/query?%s" % params
# with urllib.request.urlopen(url) as f:
#      print(f.read().decode('utf-8'))

# 增加encode编码处理post请求
# import urllib.parse
# params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# data = params.encode('utf-8')
# url = "http://www.musi-cal.com/cgi-bin/"
# with urllib.request.urlopen(url, data) as f:
#     print(f.read().decode('utf-8'))

# 使用代理访问
# proxies = {'http': 'http://proxy.example.com:8080/'}
# opener = urllib.request.FancyURLopener(proxies)
# with opener.open("http://www.python.org") as f:
#     print(f.read().decode('utf-8'))

# 不使用代理访问
# opener = urllib.request.FancyURLopener({})
# with opener.open("http://www.python.org") as f:
#     print(f.read().decode('utf-8'))

# 快速存储文件
# local_filename, headers = urllib.request.urlretrieve('http://python.org/')
# html = open(local_filename)

# 直接处理请求
# req = urllib.request.Request('http://www.voidspace.org.uk')
# with urllib.request.urlopen(req) as response:
#    the_page = response.read()


# 拼接字典组成url
# import urllib.parse
# data = {}
# data['name'] = 'Somebody Here'
# data['location'] = 'Northampton'
# data['language'] = 'Python'
# url_values = urllib.parse.urlencode(data)
# print(url_values)  # The order may differ from below.
# # name = Somebody+Here&language=Python&location=Northampton
# url = 'http://www.example.com/example.cgi'
# full_url = url + '?' + url_values
# data = urllib.request.urlopen(full_url)


# 增加请求头
# import urllib.parse
# url = 'http://www.someserver.com/cgi-bin/register.cgi'
# user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
# values = {'name': 'Michael Foord',
#           'location': 'Northampton',
#           'language': 'Python' }
# headers = {'User-Agent': user_agent}
#
# data = urllib.parse.urlencode(values)
# data = data.encode('ascii')
# req = urllib.request.Request(url, data, headers)
# with urllib.request.urlopen(req) as response:
#     the_page = response.read()

# 常见HTTP错误类型
# responses = {
#     100: ('Continue', 'Request received, please continue'),
#     101: ('Switching Protocols',
#           'Switching to new protocol; obey Upgrade header'),
#
#     200: ('OK', 'Request fulfilled, document follows'),
#     201: ('Created', 'Document created, URL follows'),
#     202: ('Accepted',
#           'Request accepted, processing continues off-line'),
#     203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
#     204: ('No Content', 'Request fulfilled, nothing follows'),
#     205: ('Reset Content', 'Clear input form for further input.'),
#     206: ('Partial Content', 'Partial content follows.'),
#
#     300: ('Multiple Choices',
#           'Object has several resources -- see URI list'),
#     301: ('Moved Permanently', 'Object moved permanently -- see URI list'),
#     302: ('Found', 'Object moved temporarily -- see URI list'),
#     303: ('See Other', 'Object moved -- see Method and URL list'),
#     304: ('Not Modified',
#           'Document has not changed since given time'),
#     305: ('Use Proxy',
#           'You must use proxy specified in Location to access this '
#           'resource.'),
#     307: ('Temporary Redirect',
#           'Object moved temporarily -- see URI list'),
#
#     400: ('Bad Request',
#           'Bad request syntax or unsupported method'),
#     401: ('Unauthorized',
#           'No permission -- see authorization schemes'),
#     402: ('Payment Required',
#           'No payment -- see charging schemes'),
#     403: ('Forbidden',
#           'Request forbidden -- authorization will not help'),
#     404: ('Not Found', 'Nothing matches the given URI'),
#     405: ('Method Not Allowed',
#           'Specified method is invalid for this server.'),
#     406: ('Not Acceptable', 'URI not available in preferred format.'),
#     407: ('Proxy Authentication Required', 'You must authenticate with '
#           'this proxy before proceeding.'),
#     408: ('Request Timeout', 'Request timed out; try again later.'),
#     409: ('Conflict', 'Request conflict.'),
#     410: ('Gone',
#           'URI no longer exists and has been permanently removed.'),
#     411: ('Length Required', 'Client must specify Content-Length.'),
#     412: ('Precondition Failed', 'Precondition in headers is false.'),
#     413: ('Request Entity Too Large', 'Entity is too large.'),
#     414: ('Request-URI Too Long', 'URI is too long.'),
#     415: ('Unsupported Media Type', 'Entity body in unsupported format.'),
#     416: ('Requested Range Not Satisfiable',
#           'Cannot satisfy request range.'),
#     417: ('Expectation Failed',
#           'Expect condition could not be satisfied.'),
#
#     500: ('Internal Server Error', 'Server got itself in trouble'),
#     501: ('Not Implemented',
#           'Server does not support this operation'),
#     502: ('Bad Gateway', 'Invalid responses from another server/proxy.'),
#     503: ('Service Unavailable',
#           'The server cannot process the request due to a high load'),
#     504: ('Gateway Timeout',
#           'The gateway server did not receive a timely response'),
#     505: ('HTTP Version Not Supported', 'Cannot fulfill request.'),
#     }

# 设置默认超时时间
# import socket
#
# timeout = 10
# socket.setdefaulttimeout(timeout)

# url解析和拼接
# from urllib.parse import urlparse, urljoin, urlunparse
# o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
# print('---1---', o)
# print('---2---', o.scheme)
# print('---3---', o.port)
# print('---4---', o.geturl())
# print('---5---', urlparse('//www.cwi.nl:80/%7Eguido/Python.html'))
# print('---6---', urlparse('www.cwi.nl/%7Eguido/Python.html'))
# print('---7---', urlparse('help/Python.html'))
# print('---8---', urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html'))
# print('---9---', urljoin('http://www.cwi.nl/%7Eguido/Python.html', '//www.python.org/%7Eguido'))
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
# print(urlunparse(data))

# robot文件的过滤
# import urllib.robotparser
#
# rp = urllib.robotparser.RobotFileParser()
# rp.set_url("http://www.musi-cal.com/robots.txt")
# print('---10---', rp.read())
# print('---11---', rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco"))
# print('---12---', rp.can_fetch("*", "http://www.musi-cal.com/"))
