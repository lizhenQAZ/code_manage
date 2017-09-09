from flask import Flask


# 实例化Flask对象
app = Flask(__name__)


# 添加路由
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
