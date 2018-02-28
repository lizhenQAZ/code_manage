# coding: utf-8
import json
from redis import Redis
from pymongo import MongoClient


# 创建redis数据库连接
redis_cli = Redis('192.168.0.1', 6379, 0)
# 创建mongo数据库连接
mongo_cli = MongoClient('127.0.0.1', 27017)
db = mongo_cli['Tuniu']
col = db['tuniu']
while True:
    source, data = redis_cli.blpop('tuniu:items')
    print(source)
    print(data)
    dict_data = json.loads(data.decode())
    col.insert(dict_data)
