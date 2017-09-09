from flask import Flask, request, current_app, make_response, redirect, abort
# from flask.ext.script import Manager  # depreciated
from flask_script import Manager

# 实例化Flask对象
app = Flask(__name__)
# 程序上下文
app_ctx = app.app_context()
app_ctx.push()
# 显示当前运行的程序名
print(current_app.name)
# 显示请求调度
print(app.url_map)
app_ctx.pop()
# 实例化Manager对象
manager = Manager(app)


# 添加首页路由
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 添加路由并传入参数
@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!</h1>' % name


# 请求上下文，封装请求内容
@app.route('/1')
def index1():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


# 自定义响应
@app.route('/2')
def index2():
    return '<h1>bad request!</h1>', 400


# 库函数实现响应
@app.route('/3')
def index3():
    resp = make_response('<h1>this html has a cookie!</h1>')
    # 设置cookie
    resp.set_cookie('answer', '42')
    return resp


# 重定向
@app.route('/4')
def index4():
    return redirect('https://www.baidu.com')


# 处理错误
@app.route('/user1/<name>')
def user1(name):
    if not user:
        abort(404)
    return '<h1>hello, %s</h1>' % name


if __name__ == '__main__':
    manager.run()
    # 执行方式：
    # python3 abc_06.py runserver --host 0.0.0.0
    # 访问方式：
    # 网卡IP访问
