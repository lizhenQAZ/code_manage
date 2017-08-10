import socket
import threading
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

        self.tcp_server_socket.setblocking(False)

        self.tcp_client_sockets = list()

        self.filename_root = filename_root

    def run_forever(self):
        while True:
            try:
                time.sleep(0.5)
                print(self.tcp_client_sockets)
                tcp_client_socket, tcp_client_data = self.tcp_server_socket.accept()
                # print(tcp_client_socket.getpeername(), tcp_client_socket.getsockname())
            except Exception as e:
                print('---1---', e)
            else:
                tcp_client_socket.setblocking(False)
                self.tcp_client_sockets.append(tcp_client_socket)
                self.deal_with_request()

    def deal_with_request(self):
        for client_socket in self.tcp_client_sockets:
            try:
                recv_data = client_socket.recv(1024)
        # print(recv_data.decode('utf-8'))
            except Exception as e:
                print('---2---', e)
            else:
                if recv_data:
                    print('%s >>>> %s' % (client_socket.getpeername(), recv_data))
                else:
                    self.tcp_client_sockets.remove(client_socket)
                    client_socket.close()


def tcp_server_main():
    httpserver = WSGISever(8093, './html')
    httpserver.run_forever()


if __name__ == '__main__':
    tcp_server_main()