import socket
import re
import multiprocessing
import time
import sys


class WSGISever(object):
    def __init__(self, port, filename_root, app):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2.绑定端口
        self.tcp_server_socket.bind(('', port))

        # 3.监听端口
        self.tcp_server_socket.listen(128)

        self.tcp_client_socket = None

        self.filename_root = filename_root

        self.app = app

    def run_forever(self):
        while True:
            tcp_client_socket, tcp_client_data = self.tcp_server_socket.accept()
            p = multiprocessing.Process(target=self.deal_with_request, args=(tcp_client_socket,))
            p.start()

    def deal_with_request(self, tcp_client_socket):
        while True:
            recv_data = tcp_client_socket.recv(1024)
            # print(recv_data.decode('utf-8'))
            if not recv_data:
                tcp_client_socket.close()
                return
            html_lines = recv_data.decode('utf-8').splitlines()
            print(html_lines)
            ret = re.match(r'([^/]+)([^ ]+)', html_lines[0])
            if ret:
                filename = ret.group(2)
                if filename == '/':
                    filename = '/index.html'

                if not filename.endswith('.html'):
                    try:
                        print(self.filename_root + filename)
                        f = open(self.filename_root + filename, 'rb')

                    except IOError:
                        # response_header = 'HTTP/1.1 404 not found'
                        # response_header += '\r\n\r\n'
                        # response_body = 'sorry, 没有网页!'.encode('gbk')
                        response_body = 'sorry, 没有网页! %s' % time.ctime()
                        response_body = response_body.encode('utf-8')
                        response_header = 'HTTP/1.1 404 not found\r\n'
                        response_header += 'Content-Type: text/html; charset=utf-8\r\n'
                        response_header += 'Content-Length: %d\r\n\r\n' % len(response_body)

                        tcp_client_socket.send(response_header.encode('utf-8') + response_body)

                    else:
                        content = f.read()
                        f.close()

                        response_body = content
                        response_header = 'HTTP/1.1 200 OK\r\n'
                        response_header += 'Content-Length: %d\r\n\r\n' % len(response_body)

                        tcp_client_socket.send(response_header.encode('utf-8') + response_body)

                else:
                    env = dict()
                    env['PATH_INFO'] = filename
                    response_body = self.app(env, self.set_headers)
                    # print('-------------->self.headers<-------------------')
                    # print(self.headers)
                    # print('-------------->response_body<-------------------')
                    # print(response_body)                   
                    response_header = 'HTTP/1.1 %s\r\n' % self.headers[0]
                    for response_style in self.headers[1]:
                        response_header += '%s:%s\r\n' % (response_style[0], response_style[1])
                    response_header += 'Content-Length: %d\r\n\r\n' % len(response_body.encode('utf-8'))
                    response = response_header + response_body
                    tcp_client_socket.send(response.encode('utf-8'))

    def set_headers(self, status, response_headers):
        self.headers = [status, response_headers]


g_static_root = './static'
g_templates_root = './templates'
g_dynamic_root = './dynamic'


def tcp_server_main():
    if len(sys.argv) == 3:
        port = sys.argv[1]
        if port.isdigit():
            port = int(port)
        print(port)
        web_frame_app_name = sys.argv[2]
        print(web_frame_app_name)

        frame_app_list = web_frame_app_name.split(':')
        web_frame = frame_app_list[0]
        app_name = frame_app_list[1]

        # 修改库的搜索路径
        sys.path.append(g_dynamic_root)
        module_name = __import__(web_frame)
        app = getattr(module_name, app_name)
        httpserver = WSGISever(port, g_static_root, app)
        httpserver.run_forever()
    else:
        print("请以下面方式运行程序：python3 web_server.py 8000 web:app")


if __name__ == '__main__':
    tcp_server_main()
