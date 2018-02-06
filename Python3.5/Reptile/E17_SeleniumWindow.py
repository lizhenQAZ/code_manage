#coding:utf-8
from selenium import webdriver

# 构建url
url = 'http://sh.58.com'

# 创建浏览器驱动
driver = webdriver.Chrome()

# 发起请求
driver.get(url)
# 定位到房屋出租元素，点击元素
el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/em[1]/a')
el.click()
# 打印url
print(driver.current_url)

# 查看所有的标签列表
window_list = driver.window_handles
print (window_list)

# 切换列表
driver.switch_to.window(window_list[1])
print(driver.current_url)
