from urllib.request import urlopen
import re


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
    # print(url_sub_list)
    url_sub_set = set(url_sub_list)
    print(url_sub_set)

    # 获取网址的根路径
    match = re.match(r'(http://[^/]*)(.*)', url)
    url_root = match.group(1)

    # 获取所有网址
    url_set = set()
    for url_sub_info in url_sub_set:
        sub_path = re.match(r'[^/]*(.*)', url_sub_info).group(1)
        filename_path = url_root + sub_path
        url_set.add(filename_path)
    # print(url_set)
    return url_set

if __name__ == '__main__':
    '''获取博学谷主页，存储在对应的路径下'''
    url = 'http://nsdual.boxuegu.com/view/home.html'
    url_set = get_url_links(url)
    print(url_set)