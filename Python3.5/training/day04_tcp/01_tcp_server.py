import socket


def tcp_server_main():
    # 1.新建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_server_socket.bind(('',8081))

    # 3.监听端口
    tcp_server_socket.listen(128)

    # 4.等待连接
    tcp_client_socket, tcp_client_addr = tcp_server_socket.accept()

    # 5.响应链接
    tcp_client_recv_data = tcp_client_socket.recv(1024)
    print(tcp_client_recv_data.decode('gbk'))
    tcp_client_socket.send('communication is finished, over!'.encode('gbk'))

    # 6.关闭套接字
    tcp_client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    tcp_server_main()