# 初始化入口
g_url_init = 'http://nsdual.boxuegu.com/login.jsp'  # 设置网址的初始地址

# 所有资源的链接
g_url_links_list = list()  # 存储所有的网络连接
g_url_links_set = set()  # 存储所有的网络连接

# 所有爬取网址的链接
g_query_links_list = list()  # 存储所有可以爬取网址的网络连接
e_file_type_set = {'ico', 'png', 'js', 'css'}  # 存储爬取网址时需要排除的文件类型

# excel存储的信息
g_sheetname = 'url_links'
g_exclname = 'websites.xlsx'
g_app = 'Excel'
g_workspace = None
