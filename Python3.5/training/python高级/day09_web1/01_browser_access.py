import socket
import threading
import re


g_filename_root = './html'


def send_file(client_socket, response_header, response_body):
    client_socket.send(response_header.encode('utf-8'))
    client_socket.send(response_body)
    client_socket.close()


def tcp_server_main():
    # 1.新建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口
    tcp_server_socket.bind(('', 8094))

    # 3.监听端口
    tcp_server_socket.listen(128)

    while True:
        tcp_client_socket, tcp_client_data = tcp_server_socket.accept()
        recv_data = tcp_client_socket.recv(1024)
        # print(recv_data   .decode('utf-8'))
        if not recv_data:
            tcp_client_socket.close()
            continue
        html_lines = recv_data.decode('utf-8').splitlines()
        print(html_lines)
        ret = re.match(r'([^/]+)([^ ]+)', html_lines[0])
        if ret:
            filename = ret.group(2)
            if filename == '/':
                filename = '/index.html'
        try:
            f = open(g_filename_root + filename, 'rb')

        except IOError:
            response_header = 'HTTP/1.1 404 not found'
            response_header += ';Content-Type:text/html; charset=utf-8\r\n\r\n'
            response_body = 'sorry, 没有网页!'.encode('utf-8')

            # send_file(tcp_client_socket, response_header, response_body)
            t = threading.Thread(target=send_file, args=(tcp_client_socket, response_header, response_body))
            t.start()
            # print('open file fail --- ', e)

        else:
            content = f.read()
            f.close()

            response_header = 'HTTP/1.1 200 OK'
            response_header += '\r\n\r\n'
            response_body = content

            t = threading.Thread(target=send_file, args=(tcp_client_socket, response_header, response_body))
            t.start()


if __name__ == '__main__':
    tcp_server_main()