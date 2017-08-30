from pymysql import *
from hashlib import *
from pymongo import *

def login():
    try:
        # 创建数据库连接
        # self, host=None, user=None, password="",
        # database=None, port=0, unix_socket=None,
        # charset=''
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'mysql',
            'database': 'user',
            'port': 3306,
            'charset': 'utf8',
        }
        conn = connect(**config)
        # 获取游标对象
        csr = conn.cursor()
        # 执行SQL语句
        select_sql = 'select password from register where username=%s'
        select_params = [uname]
        csr.execute(select_sql, select_params)
        pwd = csr.fetchone()
        print(pwd)
        # 通过用户名查找该用户是否存在
        # 不存在，则提醒用户名错误,登录失败
        # 存在，查看密码是否正确
        # 正确，登录成功
        # 错误，用户名或密码错误，登录失败
        if pwd is None:
            print("该用户名错误，登录失败")
        else:
            pwd = pwd[0]
            print(pwd)
            if pwd == upwd_sha1:
                print('登录成功')
                print('mysql', uname)
                col.insert_one({'username': uname, 'password': upwd_sha1})
            else:
                print('用户名或密码错误，登录失败')
        csr.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    try:
        # 用户输入用户名和密码
        uname = input('请输入用户名：')
        upwd = input('请输入密码:')

        # 对密码进行加密
        s1 = sha1()
        s1.update(upwd.encode())
        upwd_sha1 = s1.hexdigest()

        # 创建mongo的数据库连接
        # host = None,
        # port = None,
        mc = MongoClient(host='127.0.0.1', port=27017)
        # 创建数据库对象
        db = mc.user
        # 创建集合对象
        col = db.register
        # mongo中查找数据
        # 没有找到，在mysql中查找
        # 找到，则显示登录成功
        result = col.find_one({'username': uname})
        print(result)
        if result is None:
            login()
        else:
            if result['password'] == upwd_sha1:
                print('登陆成功')
                print('mongo', uname)
            else:
                print('用户名或密码错误，登录失败')
    except Exception as e:
        print(e)
