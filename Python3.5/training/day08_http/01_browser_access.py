import socket
import threading


def send_file(client_socket):
    content = "HTTP/1.1 200 OK \r\n\r\n bchsdbcgv"
    client_socket.send(content.encode('utf-8'))
    client_socket.close()


def tcp_server_main():
    # 1.新建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_server_socket.bind(('', 8081))

    # 3.监听端口
    tcp_server_socket.listen(128)

    while True:
        tcp_client_socket, tcp_client_data = tcp_server_socket.accept()
        recv_data = tcp_client_socket.recv(1024)
        print(recv_data.decode('utf-8'))
        t = threading.Thread(target=send_file, args=(tcp_client_socket,))
        t.start()


if __name__ == '__main__':
    tcp_server_main()