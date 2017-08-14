import get_links
import build_files
import global_data


def set_all_links(url):
    # 获取登陆页面上所有链接
    get_links.get_all_links(url)
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


def save_all_files(url_links_set):
    # 把每个链接中资源取出放在相应的位置上
    for i, url in enumerate(url_links_set):
        string = '%s' % (i+1)
        print(string*5, url)
        build_files.build_by_url(url)
    print(4, '--------URLNo=%d--------end---------' % len(url_links_set))


def save_all_links():
    pass


def main():
    # 获取博学谷登陆页面，存储在对应的路径下
    url = global_data.g_url_init
    set_all_links(url)
    # save_all_files(global_data.g_url_links_set)

if __name__ == '__main__':
    main()
