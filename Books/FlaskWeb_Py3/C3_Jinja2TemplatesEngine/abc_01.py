from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment


# 实例化Flask对象
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)


# 添加首页路由
@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


# 添加用户访问路由
@app.route('/user/<name>')
def user(name):
    # 模板占位符
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
