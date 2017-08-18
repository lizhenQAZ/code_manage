import pickle
import global_data


def create():
    global_data.g_pickle_fd = open(global_data.g_pickle_filename, 'wb')


def write():
    f = global_data.g_pickle_fd
    pickle.dump(global_data.g_pickle_websites_list, f, -1)


def close():
    global_data.g_pickle_fd.close()


def __pickle_main():
    create()
    temp_list = [1, 2]
    global_data.g_pickle_websites_list = temp_list
    write()
    close()


if __name__ == '__main__':
    __pickle_main()
