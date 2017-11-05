# coding:utf-8
from selenium import webdriver
import time
import requests
import re


# 构建url
url = 'https://qzone.qq.com/'
tar_url = 'https://user.qzone.qq.com/516960831'
# 构建浏览器驱动
driver = webdriver.Chrome()
# 访问登录界面
driver.get(url)
time.sleep(3)
# 框架需要先进入，再在里面进行元素定位
el_iframe = driver.find_element_by_xpath('//*[@id="login_frame"]')
# 进入框架
driver.switch_to.frame(el_iframe)
# 点击账号密码登录(获取到节点，调用模拟点击)
el = driver.find_element_by_xpath('//*[@id="switcher_plogin"]')
# print (el.text)
el.click()
time.sleep(2)
# 输入账号
user = input('请输入用户名: ')
pwd = input('请输入密码: ')
el_user = driver.find_element_by_xpath('//*[@id="u"]')
el_user.send_keys(user)
# 输入密码
el_pwd = driver.find_element_by_xpath('//*[@id="p"]')
el_pwd.send_keys(pwd)
# 点击登陆
el_sub = driver.find_element_by_xpath('//*[@id="login_button"]')
el_sub.click()
time.sleep(3)
# 设置请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}
# 获取cookie
cookies_dict = {}
list_cookies = driver.get_cookies()  #这里返回的是一个更多信息的字典列表
print(list_cookies)
for infos in list_cookies:
    print(infos)
    cookies_dict[infos['name']] = infos['value']
print(cookies_dict)
# 切换访问
response = requests.get(tar_url, headers=headers, cookies=cookies_dict, verify=False)
# 验证是否登录成功
if re.findall(r'浅唱流年', response.content.decode()):
    # 记录登录成功的页面
    with open('027_qzone_selenium_cookie.html', 'wb')as f:
        f.write(response.content)
else:
    print('not found!')
driver.close()
