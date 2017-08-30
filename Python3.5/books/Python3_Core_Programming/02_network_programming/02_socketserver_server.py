from socketserver import (TCPServer as Tcp, StreamRequestHandler as Srh)
from time import ctime


host = ''
port = 10001
addr = (host, port)


class RequestHandlerFunc(Srh):
    def handle(self):
        print('...send message to...', self.client_address)
        msg = '[%s] %s' % (ctime(), self.rfile.readline())
        print(msg)
        self.wfile.write(msg.encode('utf-8'))


def main():
    # 1.绑定TCP服务器的地址和处理方法
    tcp_server = Tcp(addr, RequestHandlerFunc)

    # 2.TCP服务器运行等待事件驱动
    tcp_server.serve_forever()


if __name__ == '__main__':
    main()