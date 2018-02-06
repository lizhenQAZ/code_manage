from pymysql import *
from hashlib import *


if __name__ == '__main__':
    try:
        # 用户输入用户名和密码
        uname = input('请输入用户名：')
        upwd = input('请输入密码:')

        # 对密码进行加密
        s1 = sha1()
        s1.update(upwd.encode())
        upwd_sha1 = s1.hexdigest()

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
        # 存在，则提醒用户名已占用
        # 不存在，则可以注册
        if pwd:
            print("该用户名已被使用,注册失败")
        else:
            insert_sql = 'insert into register values(0, %s, %s)'
            insert_params = [uname, upwd_sha1]
            count = csr.execute(insert_sql, insert_params)
            print(count)
            conn.commit()
            if count == 1:
                print('注册成功')
            else:
                print('注册失败')
        csr.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()
