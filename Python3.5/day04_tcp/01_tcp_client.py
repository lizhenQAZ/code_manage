import socket


def tcp_client_main():
    # 1.新建套接字
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.建立连接
    ip = input('please enter the ip address: ')
    port = input('please enter the port: ')
    tcp_client_socket.connect((ip,int(port)))

    # 3.收发数据
    tcp_client_data = input('please enter the communication data: ')
    tcp_client_socket.send(tcp_client_data.encode('gbk'))# windows平台编码格式为'gbk'
    tcp_client_recv_data = tcp_client_socket.recv(1024)
    print(tcp_client_recv_data.decode('gbk'))

    # 4.关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    tcp_client_main()