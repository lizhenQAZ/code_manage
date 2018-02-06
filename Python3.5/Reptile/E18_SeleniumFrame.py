# coding:utf-8
from selenium import webdriver
import time


# 构建url
url = 'https://qzone.qq.com/'
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
el_user = driver.find_element_by_xpath('//*[@id="u"]')
el_user.send_keys('')
# 输入密码
el_pwd = driver.find_element_by_xpath('//*[@id="p"]')
el_pwd.send_keys('')
# 点击登陆
el_sub = driver.find_element_by_xpath('//*[@id="login_button"]')
el_sub.click()
time.sleep(2)
el_sub.click()
