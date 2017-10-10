import socket


def handle_client(client_socket):
    recv_data = client_socket.recv(1024).decode('utf-8')
    request_lines = recv_data.splitlines()
    for line in request_lines:
        print(line)
    response_header = 'HTTP/1.1 200 ok\r\n'
    response_header += '\r\n'
    response_body = 'hello world'
    responese = response_header + response_body
    client_socket.send(responese.encode('utf-8'))
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 7788))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        handle_client(client_socket)


if __name__ == '__main__':
    main()
