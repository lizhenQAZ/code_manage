import socket
import time
import udp_FeiQCoreData


def build_msg(command, option = ''):
    msg = '%s:%d:%s:%s:%d:%s' % (udp_FeiQCoreData.feiQ_version, int(time.time()), udp_FeiQCoreData.feiQ_username,
                                 udp_FeiQCoreData.feiQ_hostname, command, option)
    return msg

def online_broadcast():
    msg = build_msg(udp_FeiQCoreData.IPMSG_BR_ENTRY, udp_FeiQCoreData.feiQ_username)
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