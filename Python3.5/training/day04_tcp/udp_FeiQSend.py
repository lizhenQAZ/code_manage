import socket
import time
import os
import udp_FeiQCoreData


def build_msg(command, option=''):
    udp_FeiQCoreData.packet_id = int(time.time())
    msg = '%s:%d:%s:%s:%d:%s' % (udp_FeiQCoreData.feiQ_version, udp_FeiQCoreData.packet_id, udp_FeiQCoreData.feiQ_username,
                                 udp_FeiQCoreData.feiQ_hostname, command, option)
    return msg


def build_file_msg(filename):
    # 文件序号:文件名:文件大小:修改时间:文件的属性
    command = udp_FeiQCoreData.IPMSG_SENDMSG | udp_FeiQCoreData.IPMSG_FILEATTACHOPT
    file_property = udp_FeiQCoreData.IPMSG_FILE_REGULAR
    try:
        file_size = os.path.getsize(filename)
        file_ctime = os.path.getctime(filename)
    except:
        print('no file found')
    else:
        file_msg = '%d:%s:%x:%x:%x' % (0, filename, file_size, int(file_ctime), file_property)
        file_str = '\0' + file_msg
        return build_msg(command, file_str)


def online_broadcast():
    msg = build_msg(udp_FeiQCoreData.IPMSG_BR_ENTRY, udp_FeiQCoreData.feiQ_username)
    print(msg)
    udp_FeiQCoreData.udp_socket.sendto(msg.encode('gbk'), (udp_FeiQCoreData.feiQ_broadcast_ip, udp_FeiQCoreData.feiQ_port))


def offline_broadcast():
    msg = build_msg(udp_FeiQCoreData.IPMSG_BR_EXIT)
    udp_FeiQCoreData.udp_socket.sendto(msg.encode('gbk'), (udp_FeiQCoreData.feiQ_broadcast_ip, udp_FeiQCoreData.feiQ_port))


def send_2_ip_msg():
    send_2_msg = input('please enter your msg； ')
    send_2_ip = input('please enter dest ip: ')
    if send_2_ip == '0':
        for i, user_data in enumerate(udp_FeiQCoreData.user_list):
            print('%d  %s' % (i, user_data))
        num = input('please enter the num:')
        send_2_ip = udp_FeiQCoreData.user_list[int(num)]['ip']
    msg = build_msg(udp_FeiQCoreData.IPMSG_SENDMSG, send_2_msg)
    udp_FeiQCoreData.udp_socket.sendto(msg.encode('gbk'), (send_2_ip, udp_FeiQCoreData.feiQ_port))


def send_2_file_msg():
    send_addr = input('please enter your address(0-display user_list):')
    if send_addr == '0':
        for i, addr in enumerate(udp_FeiQCoreData.user_list):
            print(i, addr)
        num = input('please enter the num: ')
        send_addr = udp_FeiQCoreData.user_list[i]
    print('the ip is: %s' % send_addr)
    filename = input('please enter filename(0-显示当前路径下的文件名)')
    if filename == '0':
        files_list = os.listdir()
        for i, file in enumerate(files_list):
            print(i, file)
        num = input('please enter the num: ')
        filename = files_list[int(num)]
    print('the filename is： %s' % filename)
    if filename and send_addr:
        file_msg = build_file_msg(filename)
        udp_FeiQCoreData.udp_socket.sendto(file_msg.encode('gbk'),(send_addr, udp_FeiQCoreData.feiQ_port))
        file_info = dict()
        file_info['packet_id'] = udp_FeiQCoreData.packet_id
        file_info['file_id'] = 0
        file_info['file_name'] = filename
        udp_FeiQCoreData.file_info_queue.put(file_info)