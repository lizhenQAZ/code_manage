#!usr/bin/python
# -*- coding:utf-8 -*-
import time

#time.time
print time.time()

#time.localtime
print time.localtime(time.time())

#time.gmtime
print time.gmtime(time.time())

#time.mktime
print time.mktime(time.localtime())

#time.strftime
print time.strftime("%Y-%m-%d",time.localtime())

#time.strptime
print time.strptime("2017-05-23","%Y-%m-%d")

#time.asctime
print time.asctime(time.localtime())

#time.ctime
print time.ctime(time.time())