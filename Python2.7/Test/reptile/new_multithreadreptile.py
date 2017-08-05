#!usr/bin/python
#-*- coding:utf-8 -*-

from requests import *
from lxml import etree
fp=open('source_code.txt','r')
html=fp.read()
fp.close()
#print html
Sector=etree.HTML(html)
pic_url=Sector.xpath('//div[@class="lessonimg-box"]/a/img/@src')
pic_name=Sector.xpath('//div[@class="lessonimg-box"]/a/img/@title')
print pic_url,pic_name
i=0
for url,name in zip(pic_url,pic_name):
    print 'now load'+url
    pic=get(url)
    fp=open(str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i+=1