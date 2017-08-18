import json
import global_data


def create():
    global_data.g_json_fd = open(global_data.g_json_filename, 'w+')


def write():
    f = global_data.g_json_fd
    json.dump(global_data.g_json_websites_list, f)


def close():
    global_data.g_json_fd.close()


def json_main():
    create()
    temp_list = [1, 2]
    global_data.g_json_websites_list = temp_list
    write()
    close()


if __name__ == '__main__':
    json_main()
