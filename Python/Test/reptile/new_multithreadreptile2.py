#!usr/bin/python
#-*- coding:utf-8 -*-
#incomplete
import requests
from lxml import etree
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
class spider():
    def __init__(self):
        print "正在下载网页爬虫..."

    def changeurl(self,url,newpage):
        new_url=re.sub('pageNum=\d+','pageNum=%d'%newpage,url)
        return new_url

    def getcontent(self,url):
        url_content=requests.get(url)
        targetlist=re.findall('<li id="\\d+" test="\\d+" deg="\\d+" >.*?</li>',url_content.text,re.S)
        return targetlist

    def getdesccontentlist(self,url_string):
        info={}
        Sector=etree.HTML(url_string)
        lessonname=Sector.xpath('//li/div[@class="lesson-infor"]/h2/a/text()')
        lessonintroduction=Sector.xpath('//li/div[@class="lesson-infor"]/p/text()')
        lessontime=Sector.xpath('//li/div[@class="lesson-infor"]/div[@class="timeandicon"]/div/dl/dd/em/text()')
        lessongrade=Sector.xpath('//li/div[@class="lesson-infor"]/div[@class="timeandicon"]/div/dl/dd/em/text()')
        lessoncount=Sector.xpath('//li/div[@class="lesson-infor"]/div[@class="timeandicon"]/div/em/text()')
        #print lessonname,lessonintroduction,lessontime
        info['lessonname']=lessonname[0]
        info['lessonintroduction']=lessonintroduction[0]
        info['lessontime']=lessontime[0]
        info['lessongrade']=lessongrade[1]
        info['lessoncount']=lessoncount[0]
        return info

    def saveinfo(self,info):
        fp=open('jikexueyuan.txt','a')
        for each in info:
            fp.writelines('lessonname:'+each['lessonname'].replace("\n","").replace("space","").replace("\t","")+'\n')
            fp.writelines('lessonintroduction:' + each['lessonintroduction'].replace("\n","").replace("space","").replace("\t","")+'\n')
            fp.writelines('lessontime:' + each['lessontime'].replace("\n","").replace("space","").replace("\t","")+'\n' )
            fp.writelines('lessongrade:' + each['lessongrade'].replace("\n","").replace("space","").replace("\t","")+'\n')
            fp.writelines('lessoncount:' + each['lessoncount'].replace("\n","").replace("space","").replace("\t","")+'\n\n')
        fp.close()

if __name__=='__main__':
    classinfo=[]
    default_url='http://www.jikexueyuan.com/course/?pageNum=1'
    max_pagenum=1
    spider=spider()
    for i in range(1,max_pagenum+1):
        new_url=spider.changeurl(default_url,i)
        print "正在处理网址"+new_url
        content=spider.getcontent(new_url)
        for each in content:
            #print each
            contentinfo=spider.getdesccontentlist(each)
            classinfo.append(contentinfo)
    spider.saveinfo(classinfo)