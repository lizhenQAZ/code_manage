from socket import *
import time


udp_socket = None
feiQ_version = 1
feiQ_username = 'youknow'
feiQ_hostname = 'hp_laptop'
feiQ_broadcast_ip = '255.255.255.255'
feiQ_port = 2425
IPMSG_BR_EXIT = 0x00000002  #下线提醒


def udp_main():
    # 1.创建套接字，绑定服务器端口，允许广播
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', feiQ_port))
    udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    # 2.构造数据格式
    # 版本号:数据包编号:发送者姓名:发送者主机名:命令字:附加选项
    # 1:123456789:itcast-python:localhost:32:hello
    msg = '%s:%d:%s:%s:%d:%s' % (feiQ_version, int(time.time()), feiQ_username, feiQ_hostname, IPMSG_BR_EXIT,
                   feiQ_username)

    # 3.发送数据包
    udp_socket.sendto(msg.encode('gbk'), (feiQ_broadcast_ip, feiQ_port))

    # 4.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    udp_main()