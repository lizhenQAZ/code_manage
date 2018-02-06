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
        result = col.find({'name': 'lizhen'})
        print(result)
        for item in result:
            print(item)
        print('ok')
    except Exception as e:
        print('false')
        print(e)
