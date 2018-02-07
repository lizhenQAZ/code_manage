#coding:utf-8

# 导入webdriver
from selenium import webdriver
import time
# 创建浏览器对象
# driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

# 获取url对应的响应
driver.get('http://www.baidu.com')

# 保存快照
# driver.save_screenshot('baidu.png')

# 定位到输入框
# el = driver.find_element_by_id('kw')
# el = driver.find_element_by_xpath('//*[@id="kw"]')
# el = driver.find_element_by_css_selector('#kw')
# el = driver.find_element_by_name('wd')
el = driver.find_element_by_xpath('//*[@id="u1"]/a[2]')
# el.click()

print (el.text,el.get_attribute('href'))
# print (el)
# el.send_keys('上海python2期')


time.sleep(5)
# 打印源码
# print (driver.page_source)
# 打印cookies
# print (driver.get_cookies())
# 打印标题和当前url
# print (driver.title)
# print (driver.current_url)

# driver.close()
driver.quit()