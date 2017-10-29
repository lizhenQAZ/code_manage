#coding:utf-8

import requests
import re

# 构建url
url = 'http://www.renren.com/923768535'
# 构建headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Cookie": "anonymid=j6c96snx6i82ml; _r01_=1; depovince=GW; JSESSIONID=abcAkp98KsJMlcCdQyB9v; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1509138190; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1509138190; _ga=GA1.3.1361939841.1504226199; _gid=GA1.3.1490576702.1509138190; jebe_key=2b511d4c-0b0e-4e77-bcbd-28616d344a3d%7Ceda913e449d4d8cd6ac80727da63a1fe%7C1507298042637%7C1%7C1509156000796; _ga=GA1.2.1361939841.1504226199; _gid=GA1.2.1490576702.1509138190; ch_id=10016; jebecookies=e3dcdf12-f78d-4db0-8c65-0e8006593fd2|||||; ick_login=9f3e5cb1-41e4-4f62-bcb2-57da85db6ef3; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=317901afe0e3ea16b3942ef5caee08745; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=23ac11c3af7507823e58f9fa14ddf4335; societyguester=23ac11c3af7507823e58f9fa14ddf4335; id=923768535; xnsid=9dfe8d81; ver=7.0; loginfrom=null; wp_fold=0"
}
# 发起请求
response = requests.get(url, headers=headers)
with open('renren.html','wb')as f:
    f.write(response.content)

# 验证是否登录成功
re.findall(r'迷途',response.content.decode())