# coding=utf-8
"""
功能：
1.发送邮件单元测试：
    测试类执行方式：python -m unittest 007发送邮件单元测试.MailTest
"""
# 导入测试模块
import unittest
from E7_SendMail import app


# 自定义测试类，必须继承自TestCase
class MailTest(unittest.TestCase):
    # 测试初始化
    def setUp(self):
        self.app = app
        # 构造客户端
        self.client = self.app.test_client()

    # 测试结束方法
    def tearDown(self):
        pass

    # 测试代码，函数名定义必须以test开头
    def test_send_mail(self):
        resp = self.client.get('/')
        print resp.data
        self.assertEqual('Send successfully', resp.data)
