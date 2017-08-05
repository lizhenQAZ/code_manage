import socket
import udp_FeiQCoreData
import udp_FeiQSend
import udp_FeiQRecv


def create_socket():
    udp_FeiQCoreData.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_FeiQCoreData.udp_socket.bind(('', udp_FeiQCoreData.feiQ_port))
    udp_FeiQCoreData.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def print_menu():
    print('='*40)
    print('1-上线提醒')
    print('2-下线提醒')
    print('3-向指定ip地址发送信息')
    print('4-收到一次消息')
    print('0-退出')
    print('='*40)


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

        # 上线提醒
        if cmd == '1':
            udp_FeiQSend.online_broadcast()
            continue

        # 下线提醒
        elif cmd == '2':
            udp_FeiQSend.offline_broadcast()
            continue

        # 向指定地址发送消息
        elif cmd == '3':
            udp_FeiQSend.send_2_ip_msg()
            continue

        elif cmd == '4':
            udp_FeiQRecv.recv_1_msg()
            continue

        elif cmd == '0':
            udp_FeiQSend.offline_broadcast()
            udp_FeiQCoreData.udp_socket.close()
            exit(0)


if __name__ == "__main__":
    udp_main()