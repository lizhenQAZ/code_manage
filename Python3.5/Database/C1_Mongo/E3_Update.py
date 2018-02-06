from pymongo import *

if __name__ == '__main__':
    try:
        # 创建连接对象
        client = MongoClient(host='192.168.79.71', port=27017)
        # 创建数据库
        db = client.mytest
        # 创建集合
        col = db.test
        # 执行SQL语句
        result = col.update_many({'name': 'lisi1'}, {'$set': {'name': 'lisi'}})
        print(help(result))
        print(result.matched_count)
        print('ok')
    except Exception as e:
        print('false')
        print(e)
