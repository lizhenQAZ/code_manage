from flask import Flask, request, current_app


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


if __name__ == '__main__':
    app.run(debug=True)
