# coding: utf-8
from pymongo import MongoClient
mc = MongoClient('localhost', 27017)
db = mc['Mongo_Test']
col = db['mongo_test']

# 1.mongo与python交互
# 1.1 增加数据
col.insert({'name': 'zhangsan'})
result = col.find_one()
print(result)
print('*'*100)
col.insert([{'name': 'lisi'}, {'name': 'wangwu'}])
results = col.find()
print(results)
for result in results:
    print(result)
print('*'*100, 1.1, '*'*100)

# 1.2 修改数据
col.update_one({'name': 'lisi'}, {'$set': {'name': 'lisi_'}})
results = col.find()
for result in results:
    print(result)
print('*'*100)
col.update_many({'name': 'lisi'}, {'$set': {'name': 'lisi_'}})
results = col.find()
for result in results:
    print(result)
print('*'*100, 1.2, '*'*100)

# 1.3 删除数据
col.delete_one({'name': 'lisi'})
results = col.find()
for result in results:
    print(result)
print('*'*100)
col.delete_many({})
results = col.find()
for result in results:
    print(result)
print('*'*100, 1.3, '*'*100)

# 1.4 批量产生数据和自定义查询
for index in range(1000):
    col.insert({'_id': index, 'name': 'test' + str(index)})
results = col.find({'$where': 'function(){return this._id % 100 == 0;}'}, {'name': 1, '_id': 0})
for result in results:
    print(result)
print('*'*100, 1.4, '*'*100)

mc.close()
