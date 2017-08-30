import FeiQCoreData
import time
import os


def build_msg(command_num, option=""):
    """构建飞鸽传书的数据包"""

    FeiQCoreData.packet_id = int(time.time())

    msg = "%d:%d:%s:%s:%d:%s" % (FeiQCoreData.feiq_version, FeiQCoreData.packet_id,
                                 FeiQCoreData.feiq_user_name, FeiQCoreData.feiq_host_name,
                                 command_num, option)

    return msg


def send_msg(msg, dest_ip):
    """发送飞鸽传书数据"""
    FeiQCoreData.udp_socket.sendto(msg.encode("gbk"), (dest_ip, FeiQCoreData.feiq_port))


def send_broadcast_online_msg():
    """发送上线提醒"""
    online_msg = build_msg(FeiQCoreData.IPMSG_BR_ENTRY, FeiQCoreData.feiq_user_name)
    send_msg(online_msg, FeiQCoreData.broadcast_ip)


def send_broadcast_offline_msg():
    """发送下线提醒"""
    offline_msg = build_msg(FeiQCoreData.IPMSG_BR_EXIT, FeiQCoreData.feiq_user_name)
    send_msg(offline_msg, FeiQCoreData.broadcast_ip)


def send_chat_msg():
    """发送聊天信息"""

    dest_ip = input("请输入对方的ip(输入0显示当前所有的在线用户):")
    if dest_ip == "0":
        # 显示用户列表
        print("="*30)
        for i, user_info in enumerate(FeiQCoreData.user_list):
            print(i, user_info)
        print("="*30)

        # 从中取一个用户的ip
        try:
            num = int(input("请输入用户对应的序号："))
        except:
            print("输入有误...")
            return
        else:
            dest_ip = FeiQCoreData.user_list[num]['ip']

    send_data = input("请输入要发送的内容:")

    # 判断是否有目的ip以及要发送的内容，有则发送
    if dest_ip and send_data:
        chat_msg = build_msg(FeiQCoreData.IPMSG_SENDMSG, send_data)
        send_msg(chat_msg, dest_ip)


def send_file_msg():
    """给指定的ip发送文件"""



    # 1:123123:dongge:ubuntu:文件消息命令字:消息内容(可以没有) \0 0:hello.py:123:12123:文件类型:

    # 获取对方的ip
    dest_ip = input("请输入对方的ip(输入0显示当前所有的在线用户):")
    if dest_ip == "0":
        # 显示用户列表
        print("="*30)
        for i, user_info in enumerate(FeiQCoreData.user_list):
            print(i, user_info)
        print("="*30)

        # 从中取一个用户的ip
        try:
            num = int(input("请输入用户对应的序号："))
        except:
            print("输入有误...")
            return
        else:
            dest_ip = FeiQCoreData.user_list[num]['ip']

    # 获取要发送的文件名
    file_name = input("请输入要发送的文件名:")

    # 判断是否有目的ip以及要发送的内容，有则发送
    if dest_ip and file_name:

        try:
            file_size = os.path.getsize(file_name)
            file_ctime = os.path.getctime(file_name)
        except:
            print("没有此文件。。。。")
        else:
            # 文件序号:文件名:文件大小:文件修改时间:文件类型:
            option = "%d:%s:%x:%x:%x:" % (0, file_name, file_size, int(file_ctime), FeiQCoreData.IPMSG_FILE_REGULAR)

            option = "\0" + option


            file_msg = build_msg(FeiQCoreData.IPMSG_SENDMSG|FeiQCoreData.IPMSG_FILEATTACHOPT, option)
            send_msg(file_msg, dest_ip)


            # 向子进程中发送包编号/文件序号/文件名
            send_file_info = dict()
            send_file_info['packet_id'] = FeiQCoreData.packet_id
            send_file_info['file_id'] = 0
            send_file_info['file_name'] = file_name

            queue_info = dict()
            queue_info['type'] = "send_file"  # 添加一个key-value用来标记类型
            queue_info['data'] = send_file_info

            FeiQCoreData.file_queue.put(queue_info)


def download_file():
    """下载文件"""

    for i, file_info in enumerate(FeiQCoreData.download_file_list):
        print(i, file_info)

    try:
        num = int(input("请输入要下载的文件序号:"))
    except:
        print("输入数据有误....")
        return
    else:
        file_info = FeiQCoreData.download_file_list[num]

        queue_info = dict()
        queue_info['type'] = "download_file"  # 添加一个key-value用来标记类型
        queue_info['data'] = file_info

        # 发送到Queue中
        FeiQCoreData.file_queue.put(queue_info)