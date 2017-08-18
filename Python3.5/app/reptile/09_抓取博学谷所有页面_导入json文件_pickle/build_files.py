from urllib.request import urlopen
import os
import re
import global_data


def build_folder_file(url_root, url_begin):
    # 获取当前的工作路径
    current_path = os.getcwd()

    # 根据网址获取文件夹及文件的位置信息
    split_dir_list = url_begin.split('/')

    # 新建相应的文件夹
    for i, dir_info in enumerate(split_dir_list):
        if dir_info != '' and i != (len(split_dir_list)-1):
            if not os.path.isdir(dir_info):
                os.mkdir(dir_info)
            os.chdir(dir_info)

    # 在相应的路径下新建目标文件
    filename = split_dir_list[-1]
    url_obj = urlopen(url_root + url_begin)
    print(url_root + url_begin)
    content = url_obj.read()
    # print(5555)
    try:
        f = open(filename, 'wb+')
        # print(6666)
    except Exception as e:
        print('%s' % e)
    else:
        f.write('%s'.encode('utf-8') % content)
    finally:
        f.close()
        os.chdir(current_path)


def build_by_url(url):
    # 分割根路径和子路径
    match = re.match(r'(http://[^/]*)(.*)', url)
    url_root = match.group(1)
    url_begin = match.group(2)
    # print(url_root, url_begin)
    build_folder_file(url_root, url_begin)


def __main():
    '''获取博学谷主页，存储在对应的路径下'''
    url = global_data.g_url_init
    build_by_url(url)


if __name__ == '__main__':
    __main()
