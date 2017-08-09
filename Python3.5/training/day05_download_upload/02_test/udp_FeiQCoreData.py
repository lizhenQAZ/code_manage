udp_socket = None


feiQ_version = 1
feiQ_username = 'youknow'
feiQ_hostname = 'hp_laptop'
feiQ_broadcast_ip = '255.255.255.255'
feiQ_port = 2425
file_info_queue = None
packet_id = 0


IPMSG_BR_ENTRY = 0x00000001  # 上线提醒
IPMSG_BR_EXIT = 0x00000002  # 下线提醒
IPMSG_SENDMSG = 0x00000020  # 发送信息
IPMSG_RECVMSG = 0x00000021  # 告知对方已收到消息
IPMSG_ANSENTRY = 0x00000003  # 表示通报在线


# option for all command
IPMSG_FILEATTACHOPT = 0x00200000  # 文件消息  # -------添加---------

# file types for fileattach command
IPMSG_FILE_REGULAR = 0x00000001  # 普通文件  # -------添加---------


user_list = []
download_file_list = list()