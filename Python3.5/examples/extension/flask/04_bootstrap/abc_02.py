from flask import Flask, render_template, url_for, redirect, session, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_script import Manager

app = Flask(__name__)
# 使用session时需要加密
app.config['SECRET_KEY'] = 'you will never forget'
# 通过修改CDN路径，可以指定bootstrap的样式
bootstrap = Bootstrap(app)
manager = Manager(app)


class Form1(FlaskForm):
    username = StringField('Username', validators=[DataRequired("请输入用户名")])
    password = PasswordField('Password', validators=[DataRequired("请输入密码")])
    submit1 = SubmitField('Submit', validators=[DataRequired("请点击")])


class Form2(FlaskForm):
    username = StringField('Username', validators=[DataRequired("请输入用户名")])
    password = PasswordField('Password', validators=[DataRequired("请输入密码")])
    remember = BooleanField('Remember Me')
    submit2 = SubmitField('Submit', validators=[DataRequired("请点击")])


@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = Form1()
    form2 = Form2()
    session['times'] = 10
    # 一张页面、两张表单分别执行不同功能
    if form1.submit1.data and form1.validate():
        return "注册成功"
    if form2.submit2.data and form2.validate():
        return "登陆成功"
    return render_template('index1.html', form1=form1, form2=form2)


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
        # flash样式选择：success, info, warning, danger
        flash("第%s次" % time, 'success')
        flash("第%s次" % time, 'info')
        flash("第%s次" % time, 'warning')
        flash("第%s次" % time, 'danger')
        time -= 1
    return render_template('success1.html')


if __name__ == '__main__':
    manager.run()
