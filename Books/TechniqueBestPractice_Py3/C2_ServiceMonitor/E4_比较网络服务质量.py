import pycurl


url = "http://www.baidu.com"
c = pycurl.Curl()
print("请求指定的URL: ", c.setopt(pycurl.URL, url))
print("连接等待时间: ", c.setopt(pycurl.CONNECTTIMEOUT, 5))
print("请求等待时间: ", c.setopt(pycurl.TIMEOUT, 5))
print("屏蔽下载进度条: ", c.setopt(pycurl.NOPROGRESS, 0))
print("指定HTTP最大重定向数: ", c.setopt(pycurl.MAXREDIRS, 5))
print("完成交互后强制断开连接: ", c.setopt(pycurl.FORBID_REUSE, 1))
print("强制获取新的连接: ", c.setopt(pycurl.FRESH_CONNECT, 1))
print("设置保存DNS信息的时间: ", c.setopt(pycurl.DNS_CACHE_TIMEOUT, 60))
print("设置请求头的用户代理: ", c.setopt(pycurl.USERAGENT, 'Mozilla/5.2 (compatible; MSIE 6.0; Windows NT 5.1; SV1; '
                                                 '.NET CLR 1.1.4322; .NET CLR 2.0.50324)'))
# print("返回的头定向到回调函数getheader: ", c.setopt(pycurl.HEADERFUNCTION, getheader))
# print("返回的内容定向到回调函数getbody: ", c.setopt(pycurl.WRITEFUNCTION, getbody))
# print("返回的头定向到fileobj文件对象: ", c.setopt(pycurl.WRITEHEADER, fileobj))
# print("返回的HTML内容到fileobj文件对象: ", c.setopt(pycurl.WRITEDATA, fileobj))

# 执行访问操作
c.perform()
print("返回的HTTP状态码: ", c.getinfo(c.HTTP_CODE))
print("返回的传输结束的总消耗时间: ", c.getinfo(c.TOTAL_TIME))
print("返回的DNS解析所消耗的时间: ", c.getinfo(c.NAMELOOKUP_TIME))
print("返回的建立连接所消耗的时间: ", c.getinfo(c.CONNECT_TIME))
print("返回的建立连接到准备传输所消耗的时间: ", c.getinfo(c.PRETRANSFER_TIME))
print("返回的建立连接到传输开始所消耗的时间: ", c.getinfo(c.STARTTRANSFER_TIME))
print("返回的重定向所消耗的时间: ", c.getinfo(c.REDIRECT_TIME))
print("返回的上传数据包大小: ", c.getinfo(c.SIZE_UPLOAD))
print("返回的下载数据包大小: ", c.getinfo(c.SIZE_DOWNLOAD))
print("返回的平均上传速度: ", c.getinfo(c.SPEED_UPLOAD))
print("返回的平均下载速度: ", c.getinfo(c.SPEED_DOWNLOAD))
print("返回的HTTP头部大小: ", c.getinfo(c.HEADER_SIZE))
