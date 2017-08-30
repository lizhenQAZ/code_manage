import socket
import threading
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


def deal_with_file_option(option_data):
    # 59819fd7:0:0:
    file_info_list = option_data.split(":", 3)
    return int(file_info_list[0], 16), int(file_info_list[1])


def send_file(client_socket):
    request_info = client_socket.recv(1024)

    # 1_lbt80_0#128#000C29770BAB#0#0#0#4000#9:1501684876:Administrator:DONGGE-32E5DBE1:96:59819fd7:0:0:

    # print(request_info)

    feiq_data = deal_with_recv_msg(request_info)

    packet_id, file_id = deal_with_file_option(feiq_data['option'])  # 59819fd7:0:0:

    print("下载的文件包编号是:%d, 文件序号:%d" % (packet_id, file_id))

    file_name = ""

    for file_info in FeiQCoreData.send_file_list:
        if file_info['packet_id'] == packet_id and file_info['file_id'] == file_id:
            file_name = file_info['file_name']
            break
    else:
        print("对方需要下载的文件不存在")

    f = open(file_name, "rb")
    while True:
        content = f.read(1024)
        if content:
            client_socket.send(content)
        else:
            break

    f.close()

    client_socket.close()


def download_file(file_info):
    """下载文件"""

    # 创建tcp套接字
    client_tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 构建需要发送的请求数据
    option = "%x:%x:%x" % (file_info['packet_id'], file_info['file_id'], 0)
    request_info = FeiQSend.build_msg(FeiQCoreData.IPMSG_GETFILEDATA, option)

    # 链接tcp服务器
    client_tcp_socket.connect((file_info['dest_ip'], FeiQCoreData.feiq_port))

    # 发送请求
    client_tcp_socket.send(request_info.encode("gbk"))

    # 新建文件，等待数据到来后，写入到文件中
    f = open(file_info['file_name'] ,"wb")  # 因为接收到的数据是二进制，需要使用wb

    recv_data_length = 0
    while True:
        recv_data = client_tcp_socket.recv(1024)
        if recv_data:
            f.write(recv_data)
        else:
            break

        # 如果接收到的数据超过了文件大小，那么也结束
        recv_data_length += len(recv_data)
        if recv_data_length >= file_info['file_size']:
            break

    f.close()
    print("下载(%s)ok" % file_info['file_name'])


def get_file_msg_from_queue(file_queue):
    """从Queue 获取需要下载或者发送的文件信息"""
    while True:
        data_info = file_queue.get()
        if data_info['type'] == "download_file":
            # 下载文件请求
            print("需要下载。。。。", data_info['data'])

            # 使用tcp下载文件
            download_file(data_info['data'])

        elif data_info['type'] == "send_file":
            # 发送文件请求
            print("发送文件......", data_info['data'])

            FeiQCoreData.send_file_list.append(data_info['data'])


def tcp_main(file_queue):

    # 创建一个子线程 从queue中接收数据
    get_file_thread = threading.Thread(target=get_file_msg_from_queue, args=(file_queue,))
    get_file_thread.start()

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", FeiQCoreData.feiq_port))
    tcp_server_socket.listen(128)

    while True:

        client_socket, client_addr = tcp_server_socket.accept()

        send_file_thread = threading.Thread(target=send_file, args=(client_socket,))
        send_file_thread.start()

if __name__ == '__main__':
    tcp_main()