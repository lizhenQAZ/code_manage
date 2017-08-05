#!usr/bin/python
#-*- coding:utf-8 -*-

from re import *
from requests import *
fp=open('source_code.txt','r')
html=fp.read()
fp.close()
#print html
match_info=findall('<img src="(.*?)" class="lessonimg" title="(.*?)"',html)
print match_info
print len(match_info)
i=0
for info in match_info:
    pic_url=info[0]
    pic_name=info[1]
    print pic_url,pic_name
    print 'nwpw load'+pic_url
    pic=get(pic_url)
    fp=open(str(i)+'.jpg','wb')
    fp.write(pic.content)
    fp.close()
    i+=1