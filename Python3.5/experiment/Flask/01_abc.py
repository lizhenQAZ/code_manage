from flask import Flask  # 处理flask对象
from flask import request  # 处理请求
from flask import current_app  # 处理应用
from flask import make_response  # 处理响应
from flask import redirect  # 处理重定向
from flask import abort  # 处理异常


# flask实例化
app = Flask(__name__)

# 程序和请求上下文
# print(current_app.name)
# app_ctx = app.app_context()
# app_ctx.push()
# print('01', current_app.name)
# app_ctx.pop()
# 请求调度
# print('02', app.url_map)


# flask路由
@app.route('/')
# 视图函数
def index():
    return 'hello world'


@app.route('/user', methods=['POST'])
def user():
    return 'hello user'


# 动态路由
@app.route('/user/<name>')
def name(name):
    return '<h1>hello, %s!</h1>' % name


# 请求上下文
@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return "hello, %s" % user_agent


# 处理响应
# @app.route('/response')
# def response():
#     resp = make_response('<h1>hello, make response!</h1>')
#     resp.set_cookie('answer', '42')
#     return response


# 处理重定向
@app.route('/redirect')
def red():
    return redirect("https://www.baidu.com")


# 处理异常
@app.route('/abort/<user_id>')
def abort(user_id):
    if not user_id:
        abort(404)
    return '<h1>hello, %s</h1>' % user_id


if __name__ == '__main__':
    # 开启调试模式
    app.run(debug=True)
    # app.run()
