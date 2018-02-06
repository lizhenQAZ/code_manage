from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


# url = 'http://www.baudu.com'
url = 'https://segmentfault.com/q/1010000006258352'
html = urlopen(url)
time.sleep(1)
bsObj = BeautifulSoup(html.read())
# 读取h1标签下的内容
print(bsObj.h1)