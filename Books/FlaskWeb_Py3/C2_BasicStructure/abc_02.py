from flask import Flask


# 实例化Flask对象
app = Flask(__name__)


# 添加首页路由
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 添加路由并传入参数
@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)
