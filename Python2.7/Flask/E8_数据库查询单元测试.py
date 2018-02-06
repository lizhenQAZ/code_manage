# coding=utf-8
"""
功能：
1.查询数据是否插入成功
    测试类执行方式：python -m unittest 008数据库查询单元测试.DatabaseTest
"""
# 导入测试模块
import unittest
from E8_AuthBook import *


# 自定义测试类
class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        # 指定连接数据库
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://guest:guest@localhost/003test'
        # 创建表
        db.create_all()

    def tearDown(self):
        # 清除数据库会话对象
        db.session.remove()
        # 清除数据库
        # db.drop_all()

    def test_add_data(self):
        # 添加数据
        auth = Author(name='hehe')
        book = Book(info='python')
        # 提交数据到数据库
        db.session.add_all([auth,book])
        db.session.commit()
        # 提交数据后需要再次查询
        au = Author.query.filter_by(name='hehe').first()
        bk = Book.query.filter_by(info='python').first()
        # 断言数据存在
        self.assertIsNotNone(au)
        self.assertIsNotNone(bk)
