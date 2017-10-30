#!usr/bin/python
# -*- coding:utf-8 -*-
import time

# time.time
print "*" * 100
print "time.time结果: ", time.time()

# time.localtime
print "*" * 100
print "time.localtime结果: ", time.localtime()

# time.gmtime
print "*" * 100
print "time.gmtime结果: ", time.gmtime(time.time())

# time.mktime
print "*" * 100
print "time.mktime结果: ", time.mktime(time.localtime())

# time.strftime
print "*" * 100
print "time.strftime结果: ", time.strftime("%Y-%m-%d", time.localtime())

# time.strptime
print "*" * 100
print "time.strptime结果: ", time.strptime("2017-05-23", "%Y-%m-%d")

# time.asctime
print "*" * 100
print "time.asctime结果: ", time.asctime(time.localtime())

# time.ctime
print "*" * 100
print "time.ctime结果: ", time.ctime(time.time())
