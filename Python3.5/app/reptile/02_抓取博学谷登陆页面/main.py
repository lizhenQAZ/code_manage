import get_links
import build_files

'''获取博学谷主页，存储在对应的路径下'''
url = 'http://nsdual.boxuegu.com/view/home.html'
# url = 'http://nsdual.boxuegu.com/login.jsp'

# 获取主页上所有链接
url_root, url_sub_list = get_links.get_url_links(url)
print(1, url_root, url_sub_list)

# 获取所有页面的链接
get_links.get_full_url_links(url_root, url_sub_list)
print(2, get_links.g_url_links_list)

# 去除重复的链接
url_links_set = set(get_links.g_url_links_list)
print(3, url_links_set)

# 把每个链接中资源取出放在相应的位置上
for url in url_links_set:
    build_files.build_by_url(url)
print(4, '--------end---------')