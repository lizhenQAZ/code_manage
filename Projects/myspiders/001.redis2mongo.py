# coding: utf-8
from redis import StrictRedis
from pymongo import MongoClient
import json
import re

sr = StrictRedis()
mc = MongoClient('localhost', 27017)
db = mc['MFW']
col = db['mfw']
source, data = sr.blpop('mafengwo')
str_data = data.decode().replace("'", "\"").replace("\\xa0", "").replace("\\t", "").replace("\\n", "")
json_data = "".join(str_data.split())
try:
    dict_data = json.loads(json_data)
    col.insert(dict_data)
except json.JSONDecodeError as e:
    print(e)
    with open('001.insert_error.json', 'wb+') as f:
        f.write(json_data.encode())
