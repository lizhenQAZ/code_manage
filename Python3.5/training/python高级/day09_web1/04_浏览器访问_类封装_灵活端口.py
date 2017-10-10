import socket
import re
import sys


class WSGIServer(object):
    def __init__(self, server_addr):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(server_addr)
        self.server_socket.listen(128)

    def run_forever(self):
        while True:
            client_socket, client_addr = self.server_socket.accept()
            self.handle_client(client_socket)

    def handle_client(self, client_socket):
        # 获取请求文件地址
        recv_data = client_socket.recv(1024).decode('utf-8')
        request_lines = recv_data.splitlines()
        # for line in request_lines:
        #     print(line)
        # GET / HTTP / 1.1
        http_request_line = request_lines[0]
        print(http_request_line)
        http_request_header = re.match(r'[^/]+(/[^ ]*)', http_request_line).group(1)
        print(http_request_header)

        # 拼接文件地址
        if http_request_header == '/':
            g_request_file = g_templates_root + '/index.html'
        else:
            g_request_file = g_templates_root + http_request_header

        # 返回响应给浏览器
        try:
            fd = open(g_request_file)
        except IOError:
            response_header = 'HTTP/1.1 404 page not found\r\n'
            response_header += '\r\n'
            response_body = 'sorry, page not found!'
        else:
            response_header = 'HTTP/1.1 200 ok\r\n'
            response_header += '\r\n'
            response_body = fd.read()
        finally:
            responese = response_header + response_body
            client_socket.send(responese.encode('utf-8'))
            client_socket.close()


if __name__ == '__main__':
    g_templates_root = './templates'
    if len(sys.argv) == 1:
        server_addr = (host, port) = ('', 8000)
    elif len(sys.argv) == 2:
        server_addr = (host, port) = ('', int(sys.argv[1]))
    httpd = WSGIServer(server_addr)
    httpd.run_forever()
