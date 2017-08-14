from urllib.request import urlopen
import re
import random
import datetime
from time import sleep
import global_data


g_url_links_list = list()
g_query_links_list = list()
e_file_type_set = {'ico', 'png', 'js', 'css'}


def get_all_links(url):
    # 获取登陆页面上所有链接
    url_root, url_sub_list = get_url_links(url)
    # print('--------', url_root, url_sub_list)

    # 获取登陆页面的所有链接
    get_full_url_links(url_root, url_sub_list)
    # print('********', global_data.g_url_links_list)


# 拼接、过滤所有的链接地址，可以直接使用
def get_full_url_links(url_root, url_sub_list):
    # 获取随机数种子
    random.seed(datetime.datetime.now())
    count = 0

    # 获取所有网址
    while len(url_sub_list) > 0:
        url_sub = url_sub_list[random.randint(0, len(url_sub_list)-1)]
        # print(33, url_sub)
        sub_path = '/%s' % url_sub
        # print(33, sub_path)
        file_type = re.search(r'.*\.([^.]*)', sub_path).group(1)
        # print(44, file_type)
        filename_path = url_root + sub_path
        # print(55, filename_path)
        # 判断是否有新的地址，如果超出网址的长度的次数，没有新元素，则停止寻找
        if filename_path not in global_data.g_url_links_list:
            global_data.g_url_links_list.append(filename_path)
            count = 0
        else:
            if count <= len(url_sub_list)*5:
                count += 1
            else:
                break
        # sleep(1)

        # 需排除类型的地址不用遍历,只有新的元素才会被加入列表
        if file_type not in global_data.e_file_type_set:
            if filename_path not in global_data.g_query_links_list:
                global_data.g_query_links_list.append(filename_path)
                # print(6, filename_path)
                url_root, url_sub_list = get_url_links(filename_path)
    # print(7, g_url_links_list)


# 获取html页面下的链接地址
def get_url_links(url):
    # 新建网址的对象
    url_obj = urlopen(url)

    # 读取文件内容
    content = url_obj.read()

    # 获取需要的子路径
    src_sub_list = re.findall(r'src=\"([^":#]*)\"', content.decode('utf-8'))
    for i, src in enumerate(src_sub_list):
        # print(re.match(r'(\.{2}/)?(.*)', src).groups())
        src_sub_list[i] = re.match(r'(\.{2}/)?(.*)', src).group(2)
    # print(src_sub_list)
    href_sub_list = re.findall(r'href=\"([^":#]*)\"', content.decode('utf-8'))
    for i, href in enumerate(href_sub_list):
        href_sub_list[i] = re.match(r'(\.{2}/)?(.*)', href).group(2)
    # print(href_sub_list)
    url_sub_list = list()
    url_sub_list.extend(href_sub_list)
    url_sub_list.extend(src_sub_list)
    # print(11, url_sub_list)

    # 获取网址的根路径
    match = re.match(r'(http://[^/]*)(.*)', url)
    url_root = match.group(1)
    # print(22, url_root)

    return url_root, url_sub_list


if __name__ == '__main__':
    '''获取博学谷主页，存储在对应的路径下'''
    url = 'http://nsdual.boxuegu.com/view/home.html'
    url_root, url_sub_list = get_url_links(url)
    get_full_url_links(url_root, url_sub_list)
    url_links_set = set(global_data.g_url_links_list)
    print(8, url_links_set)
