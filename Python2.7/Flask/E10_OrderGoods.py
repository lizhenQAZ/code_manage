# coding=utf-8
# from Day04 import app
# 循环导入问题：
# 两个文件互相导入对方文件中的模块，导致循环导入问题
# 文件导入，只能解决模块调用，不能解决路由映射

# 导入蓝图
from flask import Blueprint

# 第一步：创建蓝图对象
# 等号左边的api是蓝图对象，字符串api是蓝图名称
api = Blueprint('application', __name__)
# 交错导入，在需要使用对方文件的模块时，再使用导入语句
from E10_News import new

# 第二步：使用蓝图对象


@api.route('/order')
def order():
    return 'order'


@api.route('/goods')
def goods():
    return 'goods'


@api.route('/list')
def list():
    return 'list'
