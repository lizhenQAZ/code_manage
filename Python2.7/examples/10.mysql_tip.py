#!usr/bin/python
# -*- coding:utf-8 -*-
from mysql import connector
import MySQLdb


# # mysql-connector
# print '*' * 100
# print 'mysql-connector结果: '
# sql = 'SELECT * from test_data.location limit 10'
# conn = connector.connect(
#     host="localhost",
#     port="3306",
#     user="root",
#     password="root",
#     database="test_data",
#     charset="utf8",
# )
# curs = conn.cursor()
# curs.execute(sql, )
# for each in curs:
#     print each[1].encode('utf-8')

# # MySQLdb
# print '*' * 100
# print 'mysqldb结果: '
# sql = 'SELECT * from test_data.location limit 10'
# conn = MySQLdb.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="root",
#         db="test_data",
#         charset="utf8",
# )
# conn.autocommit(True)
# curs = conn.cursor()
# curs.execute(sql)
# for each in curs:
#     print each[1].encode('utf-8')
