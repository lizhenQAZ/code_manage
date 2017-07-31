#!usr/bin/python
#-*- coding:utf-8 -*-

#from __future__ import print_function

#mysql-connector
'''
print 'mysql-connector'.center(44,'=')
from mysql import connector
sql=('SELECT * from pythonest.new_table limit 10')
cnx=connector.connect(host="127.0.0.1",port="3306",user="guest",password="guest",database="pythonest",charset="utf8")
db0=cnx.cursor()
db0.execute(sql)
for each in db0:
    print each[0],each[1],each[2],each[3],each[4]
'''

#MySQLdb
print 'MySQLdb'.center(44,'=')
import MySQLdb
sql=('SELECT * from pythonest.new_table limit 10')
cnx=MySQLdb.connect(host="127.0.0.1",port="3306",user="guest",password="guest",db="pythonest",charset="utf8")
cnx.autocommit(True)
db1=cnx.cursor()
db1.execute(sql)
for each in db1:
    print each[0],each[1],each[2],each[3],each[4]

'''
#torndb
print 'torndb'.center(44,'=')
import torndb
import simplejson as json
sql=('SELECT * from pythonest.new_table limit 10')
db2=torndb.connect(host="127.0.0.1",port="3306",user="guest",password="guest",database="pythonest",charset="utf8")
rows=db2.query(sql)
for row in rows:
    print json.dumps(row,ensure_ascii=False)
'''