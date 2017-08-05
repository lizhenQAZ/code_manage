import socket


def udp_main():
    # 1.新建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(('',10001))

    # 2.收发数据
    udp_data = input("please enter the messege: ")
    udp_addr = ('192.168.110.1',8001)
    udp_socket.sendto(udp_data.encode('utf-8'), udp_addr)
    udp_recv_data = udp_socket.recvfrom(1024)
    print(udp_recv_data[0].decode('gbk'))
    print(udp_recv_data[1])

    # 3.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    udp_main()