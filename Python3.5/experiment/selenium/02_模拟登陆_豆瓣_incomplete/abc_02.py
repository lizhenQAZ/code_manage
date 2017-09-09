from selenium import webdriver
import os


"""解决不了只获取a不存在的情况"""
file = 'search.html'
if not os.path.isfile(file):
    browser = webdriver.Chrome("C://Users/lizhen/AppData/Local/Google/Chrome/chromedriver_win32/chromedriver.exe")
    url = "https://book.douban.com/"
    browser.get(url)
    html = browser.find_elements_by_xpath("//div[@class='hd']/h2/span")
    # print('---1---', html[0], html[0].text, len(html))
    with open(file, 'w', errors='ignore', encoding='utf-8') as fp:
        for item in html:
            fp.write(item.text)
    browser.close()
    browser.quit()

    with open(file, encoding='utf-8') as f:
        html = f.read()
        print('---2---', html)
