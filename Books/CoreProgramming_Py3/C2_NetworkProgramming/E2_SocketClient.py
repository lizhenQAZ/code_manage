from socket import *


host = 'localhost'
port = 10001
buffersize = 1024
addr = (host, port)


def main():
    while True:
        tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        tcp_client_socket.connect(addr)
        # print('5151515')
        data = input('>')
        data += '\n'
        if data == '\n' and len(data) == 1:
            # continue
            break
        tcp_client_socket.send(data.encode('utf-8'))
        while True:
            recv_data = tcp_client_socket.recv(buffersize)
            if recv_data:
                print(recv_data.decode('utf-8'))
            else:
                tcp_client_socket.close()
                break


if __name__ == '__main__':
    main()