import socket
import udp_FeiQCoreData
import udp_FeiQSend


def handele_recv_msg(dest_addr):
    recv_dict = dict()
    recv_info = dest_addr.split(':',5)
    recv_dict['version_id'] = recv_info[0]
    recv_dict['packet_id'] = recv_info[1]
    recv_dict['username'] = recv_info[2]
    recv_dict['hostname'] = recv_info[3]
    recv_dict['command'] = recv_info[4]
    recv_dict['option'] = recv_info[5]
    return  recv_dict


def handle_command(command_content):
    command = command_content & 0x000000ff
    command_option = command_content & 0xffffff00
    return command, command_option


def add_new_user_info(username, hostname, ip):
    for user_data in udp_FeiQCoreData.user_list:
        if user_data['ip'] == ip:
            break
    else:
        user_data_info = dict()
        user_data_info['ip'] = ip
        user_data_info['hostname'] = hostname
        user_data_info['username'] = username
        udp_FeiQCoreData.user_list.append(user_data_info)


def del_user_info(ip):
    for user_data in udp_FeiQCoreData.user_list:
        if user_data['ip'] == ip:
            udp_FeiQCoreData.user_list.remove(user_data)
            break


def recv_1_msg():
    while True:
        recv_data, dest_addr = udp_FeiQCoreData.udp_socket.recvfrom(1024)
        if recv_data and dest_addr:
            # recv_msg = '%s >>> %s' % (dest_addr, recv_data)
            # print(recv_msg)
            data_dict = handele_recv_msg(recv_data.decode('gbk'))
            command, command_option = handle_command(int(data_dict['command']))

            # 判断命令字回复不同信息
            # print(command)
            if udp_FeiQCoreData.IPMSG_BR_ENTRY == command:
                print('新用户上线信息：%s' % (data_dict['option']))
                # option_info = data_dict['option']
                # username_pos = option_info.find('\0')
                # if -1 != username_pos:
                #     username = option_info[:username_pos]
                # else:
                #     username = option_info
                # add_new_user_info(username, data_dict['hostname'], dest_addr[0])
                add_new_user_info(data_dict['username'], data_dict['hostname'], dest_addr[0])
                enter_msg = udp_FeiQSend.build_msg(udp_FeiQCoreData.IPMSG_ANSENTRY,'no zuo '
                                                                                   'no bi bi, you can you up--lizhen')
                udp_FeiQCoreData.udp_socket.sendto(enter_msg.encode('gbk'), (udp_FeiQCoreData.feiQ_broadcast_ip, udp_FeiQCoreData.feiQ_port))

            elif udp_FeiQCoreData.IPMSG_BR_EXIT == command:
                print('用户%s下线了' % (data_dict['username']))
                del_user_info(dest_addr[0])

            elif udp_FeiQCoreData.IPMSG_ANSENTRY == command:
                print('用户%s已经在线' % (data_dict['username']))
                # add_new_user_info(option_info[:option_info.find('\0')], data_dict['hostname'], dest_addr[0])
                add_new_user_info(data_dict['username'], data_dict['hostname'], dest_addr[0])

            elif udp_FeiQCoreData.IPMSG_SENDMSG == command:
                print('收到的消息为：%s' % (data_dict['option']))
                recv_ok_msg = udp_FeiQSend.build_msg(udp_FeiQCoreData.IPMSG_RECVMSG, 'no zuo '
                                                                                     'no bi bi, you can you up--lizhen')
                udp_FeiQCoreData.udp_socket.sendto(recv_ok_msg.encode('gbk'), (dest_addr[0], udp_FeiQCoreData.feiQ_port))

        else:
            print('no msg!')