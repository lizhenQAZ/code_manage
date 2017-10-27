import urllib.parse
import urllib.request
# # urlencode
# print('*'*100)
# word = {'wd': '传智博客'}
# print('url编码: ', urllib.parse.urlencode(word))
# print('url编码还原字符串: ', urllib.parse.unquote('wd=%E4%BC%A0%E6%99%BA%E5%8D%9A%E5%AE%A2'))
# # get
# print('*'*100)
# url = 'http://www.baidu.com/s'
# word = {'wd': '传智博客'}
# word = urllib.parse.urlencode(word)
# newurl = url + '?' + word
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, "
#                          "like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
# request = urllib.request.Request(newurl, headers=headers)
# response = urllib.request.urlopen(request)
# print('get方式请求拼接字符串的结果: ', response.read())
# """
#     百度贴吧爬虫
# """
#
#
# def write_file(html, filename):
#     """
#         作用：保存服务器响应文件到本地磁盘文件里
#         html: 服务器响应文件
#         filename: 本地磁盘文件名
#     """
#     print("正在存储" + filename)
#     with open(filename, 'w') as f:
#         f.write(html)
#     print("-" * 100)
#
#
# def load_page(url, filename):
#     '''
#         作用：根据url发送请求，获取服务器响应文件
#         url：需要爬取的url地址
#         filename: 文件名
#     '''
#     print("正在下载" + filename)
#     headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}
#     request = urllib.request.Request(url, headers=headers)
#     response = urllib.request.urlopen(request)
#     return response.read().decode()
#
#
# def tieba_spider(url, begin_page, end_page):
#     """
#         作用：负责处理url，分配每个url去发送请求
#         url：需要处理的第一个url
#         beginPage: 爬虫执行的起始页面
#         endPage: 爬虫执行的截止页面
#     """
#     for page in range(begin_page, end_page + 1):
#         pn = (page - 1) * 50
#         if page < 10:
#             filename = "06_保存贴吧第0" + str(page) + "页.html"
#         else:
#             filename = "06_保存贴吧第" + str(page) + "页.html"
#         # 组合为完整的 url，并且pn值每次增加50
#         fullurl = url + "&pn=" + str(pn)
#         # print(fullurl)
#         # 调用loadPage()发送请求获取HTML页面
#         html = load_page(fullurl, filename)
#         # 将获取到的HTML页面写入本地磁盘文件
#         write_file(html, filename)
#
#
# kw = input("请输入需要爬取的贴吧:")
# # 输入起始页和终止页，str转成int类型
# begin_page = int(input("请输入起始页："))
# end_page = int(input("请输入终止页："))
# url = "http://tieba.baidu.com/f?"
# key = urllib.parse.urlencode({"kw": kw})
# # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
# url = url + key
# tieba_spider(url, begin_page, end_page)

# 有道词典翻译网站
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,"
                         " like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
formdata = {
    "type": "AUTO",
    "i": "i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true",
}
data = urllib.parse.urlencode(formdata)
request = urllib.request.Request(url, data=data.encode(), headers=headers)
response = urllib.request.urlopen(request)
print(response.read())
