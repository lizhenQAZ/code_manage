# coding: utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
print(driver.get_cookies())
driver.implicitly_wait(3)
kw = driver.find_element_by_id('kw')
kw.send_keys('hello')
driver.implicitly_wait(10)
# a = driver.find_element_by_css_selector("*[id='1']>h3>a")
# a.click()
time.sleep(5)
driver.execute_script('alert($("#1 h3 a").html());')
time.sleep(5)
# driver.close()
