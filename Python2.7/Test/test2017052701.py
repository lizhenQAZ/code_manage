#!usr/bin/python
# -*- coding:utf-8 -*-
import time
import calendar

#test1 get current timestamp
print "当前时间：" , time.time()

#test2 get current time
localtime = time.localtime(time.time())
print "当前时间：" , localtime

#test3 get formatting time
localtime = time.asctime(time.localtime(time.time()))
print "当前时间：" , localtime

#test4 get formatting date
#convert to "2017-05-27 19:55:56"
print "当前时间：" , time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime())
#convert to "Sat May 27 19:55:56 2017"
print "当前时间：" , time.strftime("%a %b %d %H:%M:%S %Y" , time.localtime())
#convert formatting date to timestamp
localtime = "Sat May 27 19:55:56 2017"
print time.mktime(time.strptime(localtime))

#test5 get current calendar
print "current calendar is:\n" , calendar.month(2017,5)