from socket import *
import time


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', 2425))
    udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    print(udp_socket)
    msg = '%s:%d:%s:%s:%d:%s' % ('1', int(time.time()), 'you know',
                                 'localhost', 0x00000020, '宿管来查房了!!!')
    # data, addr = udp_socket.recvfrom(1024)
    # print(data, addr)
    udp_socket.sendto(msg.encode('gbk'), ('255.255.255.255', 2425))
    udp_socket.close()


if __name__ == '__main__':
    main()