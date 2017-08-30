from socket import *
import time


udp_socket = None
feiQ_version = 1
feiQ_username = 'youknow'
feiQ_hostname = 'hp_laptop'
feiQ_broadcast_ip = '255.255.255.255'
feiQ_port = 2425
IPMSG_BR_ENTRY = 0x00000001  # 表示 上线提醒
IPMSG_BR_EXIT = 0x00000002  #下线提醒


def create_socket():
    global udp_socket
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', feiQ_port))
    udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


def print_menu():
    print('='*40)
    print('1-上线提醒')
    print('2-下线提醒')
    print('0-退出')
    print('='*40)


def online_broadcast():
    msg = '%s:%d:%s:%s:%d:%s' % (feiQ_version, int(time.time()), feiQ_username, feiQ_hostname, IPMSG_BR_ENTRY,
                   feiQ_username)
    udp_socket.sendto(msg.encode('gbk'), (feiQ_broadcast_ip, feiQ_port))


def offline_broadcast():
    msg = '%s:%d:%s:%s:%d:%s' % (feiQ_version, int(time.time()), feiQ_username, feiQ_hostname, IPMSG_BR_EXIT,
                   feiQ_username)
    udp_socket.sendto(msg.encode('gbk'), (feiQ_broadcast_ip, feiQ_port))


def udp_main():
    # 1.创建套接字，绑定服务器端口，允许广播
    # 2.构造数据格式
    # 版本号:数据包编号:发送者姓名:发送者主机名:命令字:附加选项
    # 1:123456789:itcast-python:localhost:32:hello
    # 3.发送数据包
    # 4.关闭套接字
    create_socket()
    while True:
        print_menu()
        cmd = input('please enter your cmd number: ')
        if cmd == '1':
            online_broadcast()
            continue

        elif cmd == '2':
            offline_broadcast()
            continue

        elif cmd == '0':
            offline_broadcast()
            udp_socket.close()
            exit(0)


if __name__ == "__main__":
    udp_main()