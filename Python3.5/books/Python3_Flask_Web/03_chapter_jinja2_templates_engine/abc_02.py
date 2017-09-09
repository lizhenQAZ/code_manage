from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from flask_script import Manager
from datetime import datetime


# 实例化Flask对象
app = Flask(__name__)
# manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


# 添加首页路由
# 加入时间
@app.route('/')
def index():
    print(datetime.utcnow())
    return render_template('index.html', current_time=datetime.utcnow())


# 添加用户访问路由
@app.route('/user/<name>')
def user(name):
    # 模板占位符
    return render_template('user.html', name=name)


# 自定义404错误
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 自定义500错误
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
