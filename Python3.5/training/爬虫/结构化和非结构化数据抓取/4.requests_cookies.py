#coding:utf-8
import requests
import re
# 构建url
url = 'http://www.renren.com/923768535'
# 构建headers
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}
# 构建cookies变量
temp = "anonymid=j6c96snx6i82ml; _r01_=1; depovince=GW; JSESSIONID=abcAkp98KsJMlcCdQyB9v; Hm_lvt_966bff0a868cd407a416b4e3993b9dc8=1509138190; Hm_lpvt_966bff0a868cd407a416b4e3993b9dc8=1509138190; _ga=GA1.3.1361939841.1504226199; _gid=GA1.3.1490576702.1509138190; jebe_key=2b511d4c-0b0e-4e77-bcbd-28616d344a3d%7Ceda913e449d4d8cd6ac80727da63a1fe%7C1507298042637%7C1%7C1509156000796; _ga=GA1.2.1361939841.1504226199; _gid=GA1.2.1490576702.1509138190; jebecookies=0c4a9c00-4c80-4934-a74b-e0b55cd778ee|||||; ick_login=9f3e5cb1-41e4-4f62-bcb2-57da85db6ef3; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=961c9d30a637a805935728b5d56788d45; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=5d91f2b398d50387bd18f2c975ce25fe5; societyguester=5d91f2b398d50387bd18f2c975ce25fe5; id=9237685"

cookies = {}
for i in temp.split('; '):
    # key = i.split('=')[0]
    # value = i.split('=')[0]
    cookies[i.split('=')[0]] = i.split('=')[0]
print (cookies)

# 发起请求
response = requests.get(url,headers=headers, cookies=cookies)
with open('renren2.html','wb')as f:
    f.write(response.content)
# 验证是否登录成功
print (re.findall('迷途',response.content.decode()))