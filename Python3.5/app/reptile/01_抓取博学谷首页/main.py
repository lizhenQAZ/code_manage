import get_links
import build_files

'''获取博学谷主页，存储在对应的路径下'''
url = 'http://nsdual.boxuegu.com/view/home.html'

# 获取主页上所有链接
url_set = get_links.get_url_links(url)
print(url_set)

# 把每个链接中资源取出放在相应的位置上
for url in url_set:
    build_files.build_by_url(url)