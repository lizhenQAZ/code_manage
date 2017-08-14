import get_links
import build_files
import global_data
from tkinter import Tk
import os
import save_excel
import save_mysql


# 1.获取链接
def set_all_links():
    # 获取登陆页面上所有链接
    get_links.get_all_links(global_data.g_url_init)
    print(1, global_data.g_url_links_list)

    # 遍历所有的登陆页面链接
    for i, url in enumerate(global_data.g_url_links_list):
        # string = '%s' % (i+1)
        # print(string*3, url)
        count = 0
        for f_type in global_data.g_url_links_list:
            if url.endswith(f_type):
                count += 1
        if count == 0:
            get_links.get_all_links(url)
        # print(string*3, global_data.g_url_links_list)

    # 获取包括登陆页面在内所有链接
    print(2, global_data.g_url_links_list)

    # 去除重复的链接
    global_data.g_url_links_set = set(global_data.g_url_links_list)
    print(3, global_data.g_url_links_set)


# 2.保存链接
def save_all_files():
    # 把每个链接中资源取出放在相应的位置上
    for i, url in enumerate(global_data.g_url_links_set):
        string = '%s' % (i+1)
        print(string*5, url)
        build_files.build_by_url(url)
    print(4, '--------URLNo=%d--------end---------' % len(global_data.g_url_links_set))


# 3.保存excel表格
def save_2_excel():
    Tk().withdraw()
    global_data.g_workspace = os.getcwd()
    save_excel.excel()


# 4.保存mysql数据库
def save_2_mysql():
    save_mysql.create_connection()
    for i, website in enumerate(global_data.g_query_links_list):
        global_data.g_mysql_insert_sql = '''INSERT INTO scrapy_websites(id, websites) VALUES ('%d', '%s')''' % (i+1, website)
        save_mysql.insert()
    for i, resource in enumerate(global_data.g_url_links_set):
        global_data.g_mysql_insert_sql = '''INSERT INTO resource_websites(id, resource) VALUES ('%d', '%s')''' % (i+1, resource)
        save_mysql.insert()
    save_mysql.close_connection()


def main():
    # 获取博学谷登陆页面，存储在对应的路径下
    set_all_links()
    # save_all_files(global_data.g_url_links_set)
    # save_2_excel()
    save_2_mysql()

if __name__ == '__main__':
    main()
