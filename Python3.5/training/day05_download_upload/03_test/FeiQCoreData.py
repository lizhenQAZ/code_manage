udp_socket = None  # 保存udp套接字
feiq_version = 1  # 飞秋的版本
feiq_user_name = "dong-test"  # 用户名
feiq_host_name = "ubuntu-64-1604"  # 主机名字
broadcast_ip = "255.255.255.255"  # 广播ip
feiq_port = 2425  # 飞鸽传书的端口

# 飞秋command
IPMSG_BR_ENTRY = 0x00000001  # 上线
IPMSG_BR_EXIT = 0x00000002  # 下线
IPMSG_SENDMSG = 0x00000020  # 发送 消息
IPMSG_ANSENTRY = 0x00000003  # 应答在线
IPMSG_RECVMSG = 0x00000021  # 告知对方 已收到消息
IPMSG_GETFILEDATA = 0x00000060  # 表示下载文件 tcp发送
IPMSG_FILEATTACHOPT = 0x00200000  # 表示文件消息
IPMSG_FILE_REGULAR = 0x00000001  # 表示普通文件

user_list = list()  # 保存在线用户的列表

send_file_list = list()  # 用来存储需要发送的文件

download_file_list = list()  # 用来保存需要现在的文件


file_queue = None
packet_id = 0