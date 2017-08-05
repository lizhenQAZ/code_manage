#-*- encoding:utf-8 -*-
import time
#time输出指定格式的日期，格式dd/mm/yyyy
print time.strftime('%d/%m/%Y',time.localtime(time.time()))

#datetime
import datetime
print datetime.date.today().strftime("%d/%m/%Y")

#
datetime1=datetime.date(2015,1,5)
print datetime1.strftime("%d/%m/%Y")

#
datetime2=datetime1+datetime.timedelta(days=1)
print datetime2.strftime("%d/%m/%Y")

#
datetime3=datetime1.replace(year=2017)
print datetime3.strftime("%d/%m/%Y")