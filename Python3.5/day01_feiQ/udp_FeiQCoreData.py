udp_socket = None


feiQ_version = 1
feiQ_username = 'youknow'
feiQ_hostname = 'hp_laptop'
feiQ_broadcast_ip = '255.255.255.255'
feiQ_port = 2425


IPMSG_BR_ENTRY = 0x00000001  # 上线提醒
IPMSG_BR_EXIT = 0x00000002  # 下线提醒
IPMSG_SENDMSG = 0x00000020 # 发送信息
IPMSG_RECVMSG = 0x00000021  # 告知对方已收到消息
IPMSG_ANSENTRY = 0x00000003  # 表示通报在线


user_list = []