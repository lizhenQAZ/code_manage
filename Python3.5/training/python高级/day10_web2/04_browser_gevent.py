from gevent import monkey
import gevent
import socket
import threading
import re


monkey.patch_all()


class WSGISever(object):
    def __init__(self, port, filename_root):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2.绑定端口
        self.tcp_server_socket.bind(('', port))

        # 3.监听端口
        self.tcp_server_socket.listen(128)

        self.tcp_client_socket = None

        self.filename_root = filename_root

    def run_forever(self):
        while True:
            tcp_client_socket, tcp_client_data = self.tcp_server_socket.accept()
            gevent.spawn(self.deal_with_request, tcp_client_socket)

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
                try:
                    f = open(self.filename_root + filename, 'rb')

                except IOError:
                    # response_header = 'HTTP/1.1 404 not found'
                    # response_header += '\r\n\r\n'
                    # response_body = 'sorry, 没有网页!'.encode('gbk')
                    response_body = 'sorry, 没有网页!'.encode('utf-8')
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


def tcp_server_main():
    httpserver = WSGISever(8093, './html')
    httpserver.run_forever()


if __name__ == '__main__':
    tcp_server_main()