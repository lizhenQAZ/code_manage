import socket
import select
import re
import time


class WSGISever(object):
    def __init__(self, port, filename_root):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2.绑定端口
        self.tcp_server_socket.bind(('', port))

        # 3.监听端口
        self.tcp_server_socket.listen(128)

        self.epoll = select.epoll()

        self.epoll.register(self.tcp_server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

        self.fd_socket_dict = dict()

        self.filename_root = filename_root

    def run_forever(self):
        while True:
            fd_event_list = self.epoll.poll()
            for fd, event in fd_event_list:
                if fd == self.tcp_server_socket.fileno():
                    tcp_client_socket, tcp_client_data = self.tcp_server_socket.accept()
                    self.fd_socket_dict[tcp_client_socket.fileno()] = tcp_client_socket
                    self.epoll.register(tcp_client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
                elif event == select.EPOLLIN:
                    recv_data = self.fd_socket_dict[fd].recv(1024)
                    print(recv_data)
                    if recv_data:
                        self.deal_with_data(self.fd_socket_dict[fd], recv_data)
                    else:
                        self.epoll.unregister(fd)
                        self.fd_socket_dict[fd].close()
                        del(self.fd_socket_dict[fd])

    def deal_with_data(self, tcp_client_socket, recv_data):
            html_lines = recv_data.decode('utf-8').splitlines()
            print(html_lines)
            ret = re.match(r'([^/]+)([^ ]+)', html_lines[0])
            if ret:
                filename = ret.group(2)
                print('-------', filename)
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