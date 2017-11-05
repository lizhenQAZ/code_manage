# coding:utf-8
from selenium import webdriver
import time


# 构建url
url = 'https://weibo.com/'
# 构建浏览器驱动
driver = webdriver.Chrome()
# 访问登录界面
driver.get(url)
driver.implicitly_wait(25)
# 点击登录
el_login = driver.find_element_by_xpath('//a[@node-type="loginBtn"]')
el_login.click()
time.sleep(3)
# 输入账号
user = input('请输入用户名: ')
pwd = input('请输入密码: ')
el_user = driver.find_element_by_xpath('//div[@node-type="username_box"]/input')
el_user.send_keys(user)
# 输入密码
el_pwd = driver.find_element_by_xpath('//div[@node-type="password_box"]/input')
el_pwd.send_keys(pwd)
# 点击登陆
el_sub = driver.find_element_by_xpath('//*[@node-type="login_frame"]//a[@node-type="submitBtn"]')
el_sub.click()
time.sleep(2)
driver.close()
