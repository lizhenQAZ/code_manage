#coding:utf-8

import requests
import re

# 构建url
url = 'http://www.renren.com/923768535'
# 构建headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Cookie": "anonymid=j9c9vipb-37il0d; depovince=GW; jebecookies=3967de04-ebe0-4cdf-875c-d3fbc860d7ea|||||; _r01_=1; JSESSIONID=abc7Zg04fxZJXhXHXCM9v; ick_login=e3af919d-80fe-479e-90b4-0f3aca8c21aa; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=8d80d2030c87e4c44385b755dfb658695; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=a7b199539a357dd5d3181fa2ebd18cd15; societyguester=a7b199539a357dd5d3181fa2ebd18cd15; id=923768535; xnsid=998c5f04; ch_id=10016; jebe_key=4bd33cce-cd37-4a7d-b6b0-71120acc8501%7Ceda913e449d4d8cd6ac80727da63a1fe%7C1509252431549%7C1%7C1509252430167; ver=7.0; loginfrom=null; wp_fold=0",
}
# 发起请求
response = requests.get(url, headers=headers)
with open('3_renren.html','wb')as f:
    f.write(response.content)

# 验证是否登录成功
print(re.findall(r'迷途',response.content.decode()))
