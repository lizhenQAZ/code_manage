# 初始化入口
g_url_init = '''http://nsdual.boxuegu.com/login.jsp'''  # 设置网址的初始地址

# 1.所有资源的链接
g_url_links_list = list()  # 存储所有的网络连接
g_url_links_set = set()  # 存储所有的网络连接

# 2.所有爬取网址的链接
g_query_links_list = list()  # 存储所有可以爬取网址的网络连接
e_file_type_set = {'ico', 'png', 'js', 'css'}  # 存储爬取网址时需要排除的文件类型

# 3.excel存储的信息
g_sheetname = 'url_links'
g_exclname = 'websites.xlsx'
g_app = 'Excel'
g_workspace = None

# 4.保存mysql数据库
g_mysql_conn = None
g_mysql_config = {
    'host': '127.0.0.1',
    'user': 'guest',
    'password': 'guest',
    'db': 'test_db',
    }
g_mysql_query_sql = '''SELECT * FROM user_tbl'''
g_mysql_insert_sql = None

# 5.保存CSV文件
g_csv_fd = None
g_csv_filename = 'csv_websites.csv'
g_csv_websites_list = list()

# 6.保存json文件
g_json_fd = None
g_json_filename = 'json_websites.json'
g_json_websites_list = list()
