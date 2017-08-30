import socket
import threading
import multiprocessing
import udp_FeiQCoreData
import udp_FeiQSend
import udp_FeiQRecv
import FeiQTcp


def create_socket():
    udp_FeiQCoreData.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_FeiQCoreData.udp_socket.bind(('', udp_FeiQCoreData.feiQ_port))
    udp_FeiQCoreData.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def print_all_user_info():
    for i, user_info in enumerate(udp_FeiQCoreData.user_list):
        print('%d  %s' % (i , user_info))


def print_all_waiting_files():
    print('jbycsdct%s' % udp_FeiQCoreData.download_file_list)
    for i, file_info in enumerate(udp_FeiQCoreData.download_file_list):
        print(i, file_info)


def print_menu():
    print('='*40)
    print('1-上线提醒')
    print('2-下线提醒')
    print('3-向指定ip地址发送信息')
    print('4-显示所有的在线用户')
    # print('4-收到一次消息')
    print('5-向指定ip地址发送文件')
    print('6-显示可以下载文件')
    print('7-下载文件')
    print('0-退出')
    print('='*40)


def udp_main():
    # 1.创建套接字，绑定服务器端口，允许广播
    # 2.构造数据格式
    # 版本号:数据包编号:发送者姓名:发送者主机名:命令字:附加选项
    # 1:123456789:itcast-python:localhost:32:hello
    # 3.发送数据包
    # 4.关闭套接字
    udp_FeiQCoreData.file_info_queue = multiprocessing.Queue()
    tcp_proc = multiprocessing.Process(target=FeiQTcp.tcp_main, args=(udp_FeiQCoreData.file_info_queue,))
    tcp_proc.start()
    create_socket()

    t = threading.Thread(target=udp_FeiQRecv.recv_1_msg)
    t.start()

    while True:
        print_menu()
        cmd = input('please enter your cmd number: ')

        # 上线提醒
        if cmd == '1':
            udp_FeiQSend.online_broadcast()

        # 下线提醒
        elif cmd == '2':
            udp_FeiQSend.offline_broadcast()

        # 向指定地址发送消息
        elif cmd == '3':
            udp_FeiQSend.send_2_ip_msg()

        # 显示所有用户的信息
        elif cmd == '4':
            print_all_user_info()

        # 向指定地址发送文件
        elif cmd == '5':
            udp_FeiQSend.send_2_file_msg()

        # 显示可以下载文件
        elif cmd == '6':
            print_all_waiting_files()

        # 下载文件
        elif cmd == '7':
            udp_FeiQSend.download_file()

        # 关闭套接字
        elif cmd == '0':
            udp_FeiQSend.offline_broadcast()
            udp_FeiQCoreData.udp_socket.close()
            exit(0)


if __name__ == "__main__":
    udp_main()