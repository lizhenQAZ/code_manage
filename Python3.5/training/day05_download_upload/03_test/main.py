import socket
import time
import threading
import multiprocessing
import FeiQCoreData
import FeiQRecv
import FeiQSend
import FeiQTcp


def create_udp_socket():
    """创建udp套接字"""
    FeiQCoreData.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    FeiQCoreData.udp_socket.bind(("", FeiQCoreData.feiq_port))

    # 设置允许广播
    FeiQCoreData.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


def print_online_user():
    """打印在线用户列表"""
    # print(FeiQCoreData.user_list)
    for i, user_info in enumerate(FeiQCoreData.user_list):
        print(i, user_info)

def print_all_waiting_files():
    """显示可以下载的文件"""
    for i, file_info in enumerate(FeiQCoreData.download_file_list):
        print(i, file_info)


def print_menu():
    """显示飞鸽传书的功能"""
    print("     飞鸽传书v1.0")
    print("1:上线广播")
    print("2:下线广播")
    print("3:给指定的ip发送数据")
    print("4:显示在线用户信息")
    print("5:给指定的ip发送文件")
    print("6:显示可以下载文件")
    print("7:下载文件")
    print("0:退出")


def main():

    FeiQCoreData.file_queue = multiprocessing.Queue()

    tcp_process = multiprocessing.Process(target=FeiQTcp.tcp_main, args=(FeiQCoreData.file_queue,))
    tcp_process.start()

    # 创建套接字
    create_udp_socket()

    # 创建一个子线程，接收数据
    recv_msg_thread = threading.Thread(target=FeiQRecv.recv_msg)
    recv_msg_thread.start()

    while True:

        print_menu()
        command_num = input("请输入要进行的操作:")
        if command_num == "1":
            # 发送上线提醒
            FeiQSend.send_broadcast_online_msg()
        elif command_num == "2":
            # 发送下线提醒
            FeiQSend.send_broadcast_offline_msg()
        elif command_num == "3":
            # 发送消息
            FeiQSend.send_chat_msg()
        elif command_num == "4":
            # 显示在线用户信息
            print_online_user()
        elif command_num == "5":
            # 给指定的ip发送文件
            FeiQSend.send_file_msg()
        elif command_num == "6":
            # 显示可以下载的文件
            print_all_waiting_files()
        elif command_num == "7":
            # 下载文件
            FeiQSend.download_file()
        elif command_num == "0":
            FeiQSend.send_broadcast_offline_msg()
            # 关闭套接字
            FeiQCoreData.udp_socket.close()
            exit()


if __name__ == "__main__":
    main()