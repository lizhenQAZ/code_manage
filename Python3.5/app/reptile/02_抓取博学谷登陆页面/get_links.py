from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import random
import datetime
from time import sleep


g_url_links_list = list()


# 拼接、过滤所有的链接地址，可以直接使用
def get_full_url_links(url_root, url_sub_list):
    # 获取随机数种子
    random.seed(datetime.datetime.now())
    e_file_type_set = {'ico', 'png', 'js', 'css'}
    count = 0

    # 获取所有网址
    while len(url_sub_list) > 0:
        sub_path = re.match(r'[^/]*(.*)', url_sub_list[random.randint(0, len(url_sub_list)-1)]).group(1)
        # print(3, sub_path)
        file_type = re.search(r'.*\.([^\.]*)', sub_path).group(1)
        # print(4, file_type)
        filename_path = url_root + sub_path
        print(5, filename_path)
        g_url_links_list.append(filename_path)
        # sleep(1)
        # 需排除类型的地址不用遍历,否则，就会轮询链接长度的次数
        if file_type not in e_file_type_set:
            # print(6, filename_path)
            url_sub_list = get_url_links(filename_path)
            count = 0
        else:
            if count < len(url_sub_list):
                count += 1
            else:
                break
    # print(7, g_url_links_list)


# 获取html页面下的链接地址
def get_url_links(url):
    # 新建网址的对象
    url_obj = urlopen(url)

    # 读取文件内容
    content = url_obj.read()

    # 获取需要的子路径
    src_sub_list = re.findall(r'src=\"([^\":#]*)\"', content.decode('utf-8'))
    # print(src_sub_list)
    href_sub_list = re.findall(r'href=\"([^\":#]*)\"', content.decode('utf-8'))
    # print(href_sub_list)
    url_sub_list = list()
    url_sub_list.extend(href_sub_list)
    url_sub_list.extend(src_sub_list)
    # print(1, url_sub_list)

    # 获取网址的根路径
    match = re.match(r'(http://[^/]*)(.*)', url)
    url_root = match.group(1)
    # print(2, url_root)

    return url_root, url_sub_list


if __name__ == '__main__':
    '''获取博学谷主页，存储在对应的路径下'''
    url = 'http://nsdual.boxuegu.com/view/home.html'
    url_root, url_sub_list = get_url_links(url)
    get_full_url_links(url_root, url_sub_list)
    url_links_set = set(g_url_links_list)
    print(8, url_links_set)