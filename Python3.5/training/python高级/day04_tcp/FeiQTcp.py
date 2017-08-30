import threading
import os
import socket
import udp_FeiQCoreData


g_file_infos = list()
tcp_server_socket = None  # 存储TCP服务器


def handle_feiq_data(data):
    recv_data = data.decode('gbk', errors='ignore')
    feiq_data_list = recv_data.split(':', 5)
    feiq_data = dict()
    feiq_data['version'] = feiq_data_list[0]
    feiq_data['packet_id'] = feiq_data_list[1]
    feiq_data['username'] = feiq_data_list[2]
    feiq_data['hostname'] = feiq_data_list[3]
    feiq_data['command'] = feiq_data_list[4]
    feiq_data['option'] = feiq_data_list[5]
    return feiq_data


def get_file_info(file_info):
    file_list = file_info.split(':', 3)
    packet_id = file_list[0]
    file_id = file_list[1]
    return int(packet_id, 16), int(file_id)


# 新建文件夹用于发送文件
def send_file(client_socket):
    request_data = client_socket.recv(1024)
    feiq_dict = handle_feiq_data(request_data)
    packet_id, file_id = get_file_info(feiq_dict['option'])
    print('包编号%d, 文件编号%d' % (packet_id, file_id))
    for i, file_info in enumerate(g_file_infos):
        if file_info['packet_id'] == packet_id and file_info['file_id'] == file_id:
            filename = file_info['file_name']
            try:
                f = open(filename, 'rb')
                while True:
                    content = f.read()
                    if content:
                        client_socket.send(content)
                    else:
                        break
                f.close()
            except Exception as ret:
                print('文件异常...%s' % ret)
            else:
                print('文件发送成功...')
                g_file_infos.remove(file_info)
                print('列表删除成功...')
            break
    else:
        print('no file found!')
    client_socket.close()


def get_file_info_from_queue(file_info_queue):
    while True:
        file_info = file_info_queue.get()
        g_file_infos.append(file_info)
        for i, element in enumerate(g_file_infos):
            print(i, element)


def tcp_main(file_info_queue):
    global tcp_server_socket
    recv_queue_thread = threading.Thread(target=get_file_info_from_queue, args=(file_info_queue,))
    recv_queue_thread.start()
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 2425))
    tcp_server_socket.listen(128)
    while True:
        tcp_client_socket, tcp_client_data = tcp_server_socket.accept()
        t = threading.Thread(target=send_file, args=(tcp_client_socket,))
        t.start()


if __name__ == '__main__':
    tcp_main()