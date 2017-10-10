import socket
import re
import sys
from gevent import monkey
import gevent


monkey.patch_all()


class WSGIServer(object):
    def __init__(self, server_addr, document_root):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(server_addr)
        self.document_root = document_root
        self.server_socket.listen(128)

    def run_forever(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            gevent.spawn(self.handle_client, client_socket)

    def handle_client(self, client_socket):
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            client_socket.close()
            return
        # 获取请求文件地址
        request_lines = request.splitlines()
        # for line in request_lines:
        #     print(line)
        # GET / HTTP / 1.1
        http_request_line = request_lines[0]
        print(http_request_line)
        http_request_header = re.match(r'[^/]+(/[^ ]*)', http_request_line).group(1)
        print(http_request_header)

        # 拼接文件地址
        if http_request_header == '/':
            g_request_file = self.document_root + '/index.html'
        else:
            g_request_file = self.document_root + http_request_header

        # 返回响应给浏览器
        try:
            fd = open(g_request_file, 'rb')
        except IOError:
            response_body = '页面没有找到!'
            response_header = 'HTTP/1.1 404 page not found\r\n'
            response_header += 'Content-Type: text/html; charset=utf-8\r\n'
            response_header += 'Content-Length: %d\r\n' % (len(response_body))
            response_header += '\r\n'
            response = response_header + response_body
            response = response.encode('utf-8')
        else:
            response_body = fd.read()
            response_header = 'HTTP/1.1 200 ok\r\n'
            response_header += 'Content-Length: %d\r\n' % (len(response_body))
            response_header += '\r\n'
            response = response_header.encode('utf-8') + response_body
        finally:
            fd.close()
            client_socket.send(response)
            client_socket.close()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        server_addr = (host, port) = ('', 8000)
    elif len(sys.argv) == 2:
        server_addr = (host, port) = ('', int(sys.argv[1]))
    httpd = WSGIServer(server_addr, './templates')
    httpd.run_forever()
