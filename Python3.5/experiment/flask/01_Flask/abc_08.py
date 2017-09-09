from flask import Flask, render_template, url_for, redirect, session, flash

app = Flask(__name__)
# 使用session时需要加密
app.config['SECRET_KEY'] = 'you will never forget'


@app.route('/')
def index():
    session['times'] = 10
    return render_template('index2.html')


@app.route('/guess')
def guess():
    # url_for用法：url_for('函数名')
    return redirect(url_for('success'))


@app.route('/success')
def success():
    # session用法：保存全局的字典, 无需传入
    time = session.get('times')
    while time > 0:
        # flash用法：向前端页面发送信息
        # get_flashed_messages():接收信息, 无需传入
        flash("第%s次" % time, 'info')
        time -= 1
    return render_template('success4.html')

# 当前路径下找脚本文件
# from message import message
# msg = app.register_blueprint(message)
# 指定路径下找脚本文件, 路由也加上该路径
from message import message
msg = app.register_blueprint(message, url_prefix='/message')


if __name__ == '__main__':
    app.run()
