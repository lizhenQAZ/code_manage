from pymysql import *
from hashlib import *
from pymongo import *
from redis import *


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
                sr.set(uname, upwd_sha1)
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

        # 创建redis的数据库连接
        # host = None,
        # port = None,
        # host='localhost', port=6379,
        # db=0, password=None,
        sr = StrictRedis(host='192.168.41.33', port=6379)
        # 获取键值
        result = sr.get(uname)
        # redis中查找数
        print(result)
        if result is None:
            login()
        else:
            if result.decode() == upwd_sha1:
                print('登陆成功')
                print('redis', uname)
            else:
                print('用户名或密码错误，登录失败')
    except Exception as e:
        print(e)
