import FeiQCoreData
import FeiQSend


def deal_with_recv_msg(recv_msg):
    """处理接收到的数据"""
    # 解码
    recv_msg = recv_msg.decode("gbk", errors="ignore")

    # 切割
    feiq_info_list = recv_msg.split(":", 5)

    feiq_data = dict()
    feiq_data['version'] = feiq_info_list[0]
    feiq_data['packet_id'] = feiq_info_list[1]
    feiq_data['user_name'] = feiq_info_list[2]
    feiq_data['host_name'] = feiq_info_list[3]
    feiq_data['command_num'] = feiq_info_list[4]
    feiq_data['option'] = feiq_info_list[5]

    return feiq_data


def get_command_option(command_num):
    """提取命令以及命令选项"""
    command = int(command_num) & 0x000000ff
    option = int(command_num) & 0xffffff00

    return command, option


def recv_msg():
    """接收数据"""
    while True:
        recv_data, dest_addr = FeiQCoreData.udp_socket.recvfrom(1024)
        # print("(接收到的数据)%s>>>%s" % (str(dest_addr), recv_data.decode("gbk")))

        feiq_data = deal_with_recv_msg(recv_data)
        # print("(处理之后的数据)", feiq_data)

        # 0000 0001
        # 0000 0010
        # 0000 0100
        #
        # 0000 0001, 0000 0010, 0000 0100
        #
        # 0000 0111

        command, option = get_command_option(feiq_data['command_num'])
        # print(command, option)

        if command == FeiQCoreData.IPMSG_BR_ENTRY:
            # 用户上线
            print("%s上线" % feiq_data['user_name'])


            find_position = feiq_data['option'].find("\0")
            if find_position != -1:
                user_name = feiq_data['option'][:find_position]
            else:
                user_name = feiq_data['option']

            new_user_info = dict()
            new_user_info['ip'] = dest_addr[0]
            new_user_info['user_name'] = user_name

            if new_user_info not in FeiQCoreData.user_list:
                FeiQCoreData.user_list.append(new_user_info)

            # 通报给对方 我已在线
            answer_online_msg = FeiQSend.build_msg(FeiQCoreData.IPMSG_ANSENTRY)
            FeiQSend.send_msg(answer_online_msg, dest_addr[0])

        elif command == FeiQCoreData.IPMSG_BR_EXIT:
            # 用户下线
            print("%s下线" % feiq_data['user_name'])

            for user_info in FeiQCoreData.user_list:
                if dest_addr[0] == user_info['ip']:
                    FeiQCoreData.user_list.remove(user_info)
                    break

        elif command == FeiQCoreData.IPMSG_ANSENTRY:
            # 其他用户通报在线
            print("%s已经在线" % feiq_data['user_name'])

            find_position = feiq_data['option'].find("\0")
            if find_position != -1:
                user_name = feiq_data['option'][:find_position]
            else:
                user_name = feiq_data['option']

            new_user_info = dict()
            new_user_info['ip'] = dest_addr[0]
            new_user_info['user_name'] = user_name
            if new_user_info not in FeiQCoreData.user_list:
                FeiQCoreData.user_list.append(new_user_info)

        elif command == FeiQCoreData.IPMSG_SENDMSG:
            # 其他用户发送过来新的消息

            # 判断如果发送过来的是文件消息
            if option & 0x00f00000 == FeiQCoreData.IPMSG_FILEATTACHOPT:
                # 飞鸽传书中的选项为  \0 文件序号:文件名:文件大小:文件修改时间:文件类型:
                file_info_msg = dict()
                file_info_list = feiq_data['option'][1:].split(":", 5)
                file_info_msg['packet_id'] = int(feiq_data['packet_id'])
                file_info_msg['file_id'] = int(file_info_list[0])
                file_info_msg['file_name'] = file_info_list[1]
                file_info_msg['file_size'] = int(file_info_list[2], 16)
                file_info_msg['dest_ip'] = dest_addr[0]
                FeiQCoreData.download_file_list.append(file_info_msg)

            else:
                print("%s(%s)>>>%s" % (feiq_data['user_name'], str(dest_addr), feiq_data['option']))

            # 告知对方已经接收到数据
            recv_ok_msg = FeiQSend.build_msg(FeiQCoreData.IPMSG_RECVMSG)
            FeiQSend.send_msg(recv_ok_msg, dest_addr[0])