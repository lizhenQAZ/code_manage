# coding=utf-8
"""
功能：
1.个人中心
    index、user与detail
2.消息
    new
3.订单商品
    order、goods与list
"""
from flask import Flask
# 导入蓝图对象
from E10_OrderGoods import api

app = Flask(__name__)

# 第三步：注册蓝图对象到程序实例上
app.register_blueprint(api)


@app.route('/')
def indedx():
    return 'index'


@app.route('/user')
def user():
    return 'user'


@app.route('/detail')
def detail():
    return 'detail'

if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
