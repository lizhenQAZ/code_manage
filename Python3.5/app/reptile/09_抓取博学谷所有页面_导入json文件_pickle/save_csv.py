import csv
import global_data


def create():
    global_data.g_csv_fd = open(global_data.g_csv_filename, 'w+')


def write():
    f = global_data.g_csv_fd
    cw = csv.writer(f)
    cw.writerow(global_data.g_csv_websites_list)


def close():
    global_data.g_csv_fd.close()


def __csv_main():
    create()
    temp_list = [1, 2]
    global_data.g_csv_websites_list = temp_list
    write()
    close()


if __name__ == '__main__':
    __csv_main()
