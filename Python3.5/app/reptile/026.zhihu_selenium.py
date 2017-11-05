# coding:utf-8
from selenium import webdriver
import time


# 构建url
url = 'https://www.zhihu.com/#signin'
# 修改浏览器请求头
# option = webdriver.ChromeOptions()
# option.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36')
# 构建浏览器驱动
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()
# 访问登录界面
driver.get(url)
driver.implicitly_wait(10)
# 切换登录界面
el_login_switch = driver.find_element_by_xpath('//a[@class="AppHeader-authLink"]')
el_login_switch.click()
time.sleep(3)
# # 点击登录
# el_login = driver.find_element_by_xpath('//div[@class="qrcode-signin-step1"]/div/span')
# el_login.click()
# time.sleep(3)
# # 输入账号
# user = input('请输入用户名: ')
# pwd = input('请输入密码: ')
# el_user = driver.find_element_by_xpath('//input[@name="account"]')
# el_user.send_keys(user)
# # 输入密码
# el_pwd = driver.find_element_by_xpath('//div[@class="verification input-wrapper"]/input')
# el_pwd.send_keys(pwd)
# # 点击登陆
# el_sub = driver.find_element_by_xpath('//div[@class="view view-signin"]//div[@class="button-wrapper command"]/button')
# el_sub.click()
# # time.sleep(2)
# # 选择验证码
# # 点击登录
# # driver.close()
