#coding:utf-8
import requests
import re


# 构建url
url = 'http://www.renren.com/960768847'
# 构建headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Cookie": "anonymid=j9c9vipb-37il0d; depovince=GW; _r01_=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; JSESSIONID=abc7Xwza1EGI9hnavUY9v; __utma=151146938.1308121632.1509458351.1509458351.1509458351.1; __utmb=151146938.11.10.1509458351; __utmc=151146938; __utmz=151146938.1509458351.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/960768703/profile; ick_login=8559d347-0b7a-4e2d-af11-c758f33faf11; ick=b137a2e3-f775-42c4-b1ad-d89e887344e3; t=dd104a746c88d8384ed80a549600d8a57; societyguester=dd104a746c88d8384ed80a549600d8a57; id=960768847; xnsid=8d42e0f0; jebe_key=4bd33cce-cd37-4a7d-b6b0-71120acc8501%7C932cb64c4b2269f17d75e9016741092f%7C1509458706205%7C1%7C1509458705053; jebecookies=43283214-7473-4cb7-b032-e35e6c7ede4f|||||; ch_id=10016; wp_fold=0; ver=7.0; loginfrom=null",
}
# 发起请求
response = requests.get(url, headers=headers)
# 验证是否登录成功
if re.findall(r'李震',response.content.decode()):
    # 记录登录成功的页面
    with open('004_renren_cookie.html','wb')as f:
        f.write(response.content)
else:
    print('not found!')
