from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


"""=========================>1<=============================="""
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get('http://seleniumhq.org/')

"""=========================>2<=============================="""
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get('http://www.yahoo.com')
# assert 'Yahoo' in browser.title
# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# browser.quit()

"""=========================>3<=============================="""
# import unittest
#
#
# class GoogleTestCase(unittest.TestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
#         self.addCleanup(self.browser.quit)
#
#     def testPageTitle(self):
#         self.browser.get('https://www.baidu.com')
#         self.assertIn('百度一下，你就知道', self.browser.title)
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)


"""============================>4<====================================="""
# # 声明浏览器
# chromedriver = "C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe"
#
# os.environ["webdriver.chrome.driver"] = chromedriver
#
# driver = webdriver.Chrome(chromedriver)
#
# driver.get("http://www.baidu.com")
#
# driver.close()

# driver.quit()


"""============================>5<====================================="""
# # 单个元素查找
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
#
# browser.get("http://www.baidu.com")
# input_first = browser.find_element_by_id("kw")
# input_second = browser.find_element_by_css_selector("#kw")
# input_third = browser.find_element_by_xpath('//*[@id="kw"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()
#
# from selenium import webdriver
#
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
#
# browser.get("http://www.baidu.com")
# input_first = browser.find_element(By.ID, "kw")
# print(input_first)
# browser.close()


"""============================>6<====================================="""
# 多个元素查找
# from selenium import webdriver
#
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get("http://www.baidu.com")
# lis = browser.find_elements_by_css_selector('.head_wrapper li')
# print(lis)
# browser.close()


"""============================>7<====================================="""
# # 元素交互  搜索框功能
# from selenium import webdriver
#
# import time
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()

"""============================>8<====================================="""
# 交互动作  拖拽功能
# from selenium import webdriver
# from selenium.webdriver import ActionChains
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
#
# url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()


# """============================>9<====================================="""
# # 执行Javascript   将页面拖到最底部，并且发出警告提醒
# from selenium import webdriver
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get("http://www.zhihu.com/explore")
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')


"""============================>9<====================================="""
# 执行Javascript   获取属性
# from selenium import webdriver
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# logo = browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))


"""============================>9<====================================="""
# # 执行Javascript   获取文本值
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

"""============================>9<====================================="""
# # 执行Javascript   获取文本值
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# url = 'https://www.zhihu.com/explore'
# browser.get(url)
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

"""============================>10<====================================="""
# # 执行Javascript   Frame切入切出
# import time
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# print(source)
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

"""============================>11<====================================="""
# # 执行Javascript   隐式等待
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.implicitly_wait(10)
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_element_by_class_name('zu-top-add-question')
# print(input)


"""============================>12<====================================="""
# # 执行Javascript   显示等待
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get('https://www.taobao.com/')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)


"""============================>13<====================================="""
# # 执行Javascript   浏览器的前进和后退
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get('https://www.baidu.com/')
# browser.get('https://www.taobao.com/')
# browser.get('https://www.python.org/')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

"""============================>14<====================================="""
# # 执行Javascript   cookie操作
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'zhaofan'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

"""============================>15<====================================="""
# # 执行Javascript   选项卡切换和跳转
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')

"""============================>16<====================================="""
# # 执行Javascript   异常处理
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException, NoSuchElementException
#
# browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
# try:
#     browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     browser.close()
