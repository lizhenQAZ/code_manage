# coding: utf-8
from redis import StrictRedis

# 连接数据库
sr = StrictRedis()

# 1.string类型的增删改查
# 1.1 增加
sr.set('str1', '1')
print(sr.get('str1'))
print('*'*100, 1.1, '*'*100)
# 1.2 查找
print(sr.type('str1'))
print(sr.keys('str1'))
print(sr.get('str1'))
print('*'*100, 1.2, '*'*100)
# 1.3 修改
sr.set('str1', '2')
print(sr.get('str1'))
print('*'*100, 1.3, '*'*100)
# 1.4 删除
sr.delete('str1')
print(sr.get('str1'))
print('*'*100, 1.4, '*'*100)

# 2.hash类型的增删改查
# 2.1 增加
sr.hset('hash1', 'key1', 'val1')
print(sr.hget('hash1', 'key1'))
print('*'*100, 2.1, '*'*100)
# 2.2 查找
print(sr.type('hash1'))
print(sr.keys('hash1'))
print(sr.hkeys('hash1'))
print(sr.hvals('hash1'))
print(sr.hget('hash1', 'key1'))
print(sr.hmget('hash1', 'key1'))
print('*'*100, 2.2, '*'*100)
# 2.3 修改
sr.hset('hash1', 'key1', 'val2')
print(sr.hget('hash1', 'key1'))
sr.hmset('hash1', {'key1': 'val3'})
print(sr.hmget('hash1', 'key1'))
sr.hmset('hash1', {'key1': ['val4', 'val5']})
print(sr.hmget('hash1', 'key1'))
print('*'*100, 2.3, '*'*100)
# 2.4 删除
sr.hdel('hash1', 'key1')
print(sr.hget('hash1', 'key1'))
sr.delete('str1')
print(sr.get('str1'))
print('*'*100, 2.4, '*'*100)

# 3.list类型的增删改查
# 3.1 增加
sr.lpush('list1', 'lpush')
print(sr.lrange('list1', 0, -1))
sr.rpush('list1', 'rpush')
print(sr.lrange('list1', 0, -1))
sr.linsert('list1', 'before', 'lpush', 'before')
print(sr.lrange('list1', 0, -1))
sr.rpush('list1', {'key1': 'val1'})
print(sr.lrange('list1', 0,  -1))
print('*'*100, 3.1, '*'*100)
# 3.2 查找
print(sr.lrange('list1', 0, -1))
print('*'*100, 3.2, '*'*100)
# 3.3 修改
sr.lset('list1', 0, 0)
print(sr.lrange('list1', 0, -1))
print('*'*100, 3.3, '*'*100)
# 3.4 删除
sr.lrem('list1', '10', 'lpush')
print(sr.lrange('list1', 0, -1))
sr.delete('list1')
print(sr.lrange('list1', 0, -1))
print('*'*100, 3.4, '*'*100)
