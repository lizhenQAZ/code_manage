import requests

# 基本的post方法
print('*'*100)
data = '呵呵'.encode()
response = requests.post('http://www.baidu.com/', data=data)
print('post请求的结果: ', response)
# 传入data数据
# TODO  post请求访问被拒
print('*'*100)
formdata = {
    "type": "AUTO",
    "i": "i love python",
    "doctype": "json",
    "xmlVersion": "1.8",
    "keyfrom": "fanyi.web",
    "ue": "UTF-8",
    "action": "FY_BY_ENTER",
    "typoResult": "true"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.post(url, data = formdata, headers = headers)
print('post请求的响应文本: ', response.text)
print('post请求的json文本: ', response.json())
# 使用代理
# TODO 使用代理不能访问
print('*'*100)
# 根据协议类型，选择不同的代理
proxies = {
  "http": "http://12.34.56.79:9527",
  "https": "http://12.34.56.79:9527",
}
# response = requests.get('http://www.baidu.com/', proxies=proxies)
# print('get请求代理响应文本内容: ', response.text)
# 私密代理
# TODO 使用私密代理没有返回数据
print('*'*100)
proxy = {"http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816"}
response = requests.get("http://www.baidu.com", proxies=proxy)
print(response.text)
# web客户端验证
# TODO web客户端访问ip不存在
print('*'*100)
auth = ('test', '123456')
# response = requests.get('http://192.168.199.107', auth=auth)
# print(response.text)
# cookie
print('*'*100)
response = requests.get('http://www.baidu.com/')
cookiejar = response.cookies
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print('cookiejar内容: ', cookiejar)
print('cookiedict内容: ', cookiedict)
# 实现人人网登录
ssion = requests.session()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}
ssion.post("http://www.renren.com/PLogin.do", data = data)
response = ssion.get("http://www.renren.com/410043129/profile")
print('session读取打印内容: ', response.text)
# 处理http请求SSL证书验证
response = requests.get("http://www.baidu.com/", verify=True)
print('请求SSL证书: ', response.text)
try:
    response = requests.get("https://www.12306.cn/mormhweb/")
except Exception as e:
    print('12306测试请求SSL证书: ', e)
response = requests.get("https://www.12306.cn/mormhweb/", verify=False)
print('12306跳过SSL证书认证: ', response.text)
