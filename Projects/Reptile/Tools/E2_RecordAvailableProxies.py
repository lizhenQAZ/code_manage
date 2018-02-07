# coding:utf-8
import requests
import time

# 构建一个url
url = 'http://www.baidu.com'
# 构建一个请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
# 构建代理
proxies = [
    {
        "http": "http://89.236.17.106:3128",
        "https": "https://89.236.17.106:3128",
    },
    {
        "http": "http://124.192.39.248:3128",
        "https": "https://124.192.39.248:3128",
    },
    {
        "http": "http://113.214.13.1:8000",
        "https": "https://113.214.13.1:8000",
    },
]
# 记录可用的ip代理池
ip_list = []
for proxy in proxies:
    # 发送请求获取响应
    # print(proxy)
    for key, value in proxy.items():
        temp = {}
        temp[key] = value
        # print(temp)
        try:
            start = time.time()
            response = requests.head(url, headers=headers, proxies=temp)
            end = time.time()
            print(end - start, response.status_code, temp)
            if (end - start) <= 2 and response.status_code == 200:
                ip_list.append(temp)
        except TimeoutError as e:
            print('TimeoutError: ', temp, '*' * 20, e)
        except OSError as e:
            print('OSError: ', temp, '*' * 20, e)
print(ip_list)
