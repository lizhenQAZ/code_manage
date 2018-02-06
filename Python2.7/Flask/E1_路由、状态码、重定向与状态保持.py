# coding=utf-8
"""
功能：
1.固定路由、指定传参格式路由、自定义正则路由
2.abort函数、return函数、自定义状态码与errorhandler函数
3.重定向与url_for函数
4.cookie状态保持
"""
from flask import Flask, make_response, current_app, abort, redirect, request
from werkzeug.routing import BaseConverter
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def hello_world():
    return '<h1>hello world2018</h1>'


# 动态路由指定传参格式
@app.route('/strs/<int:strs>')
def hello_strs(strs):
    return '<h1>hello %s</h1>' % strs


# 使用自定义的正则类
class Regex(BaseConverter):
    def __init__(self, url, *args):
        super(Regex, self).__init__(url)
        self.regex = args[0]


# 调用自定义的正则类
app.url_map.converters['re'] = Regex


# 限制路由访问
@app.route('/re/<re(".*"):file>')
def hello_regex(file):
    if not file:
        file = 'html/001default.html'
    else:
        file = 'html/' + file
    resp = make_response(current_app.send_static_file(file))
    return resp


# 自定义状态码：前后端数据交互
@app.route('/resp')
def hello_resp_status():
    return 'hello response', 666


# abort函数：抛出符合http协议状态码
# 一般配合errorhandler实现自定义错误页面
@app.route('/abort')
def hello_abort_status():
    abort(405)
    return 'hello abort', 999


# errorhandler捕获状态码
@app.errorhandler(405)
def hello_errorhandler(e):
    return "请求方法不允许%s" % e


# redirect 重定向：当项目文件或目录不存在
# 因为redirect接收到参数为url链接
# 反向解析
@app.route('/redir')
def hello_redirect_handler():
    # url_for接受参数为视图函数名
    return redirect('http://www.baidu.com')


# 状态保持
# http协议无状态，减少服务器压力
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('set_cookie')
    resp.set_cookie('key1', 'value1')
    return resp


# 获取用户cookie信息
@app.route('/get_cookie')
def get_cookies():
    resp = request.cookies.get('key1')
    return resp


if __name__ == '__main__':
    print app.url_map
    # app.run(debug=True)
    manager.run()
