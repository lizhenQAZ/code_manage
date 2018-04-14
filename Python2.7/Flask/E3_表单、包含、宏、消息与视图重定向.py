# coding=utf-8
"""
功能：
1.form表单、验证器与SECRET_KEY保护
2.jinja2语法：
    include函数：不能重复wtf表单对象的复用，只能实现html静态页面的内容
    macro函数：自定义函数
    flash函数：传递消息
3.redirect+url_for视图函数响应
"""
from flask import Flask, render_template, request, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


app = Flask(__name__)
# 设置secret_key
app.config['SECRET_KEY'] = 'python'


# 自定义表单类型
class Form(FlaskForm):
    # 自定义字段类型，加入验证函数，必须有数据存在
    user = StringField(validators=[DataRequired()])
    pswd = PasswordField(validators=[DataRequired(), EqualTo('pswd2')])
    pswd2 = PasswordField(validators=[DataRequired()])
    submit = SubmitField(label=u'注册')


@app.route('/', methods=['GET', 'POST'])
def wtf_forms():
    # 实例化表单对象
    form = Form()
    # validate_on_submit方法的返回值为布尔类型
    # 调用验证函数，验证页面中是否设置csrf_token
    if form.validate_on_submit():
        # 获取wtf表单数据
        us = form.user.data
        ps = form.pswd.data
        ps2 = form.pswd2.data
        print us, ps, ps2
    else:
        flash(u"请输入用户信息！")
    print form.validate_on_submit()
    return render_template('001forms.html', form=form)


# 指定请求方法
@app.route('/req', methods=['GET', 'POST'])
def req_form():
    # 获取post请求的表单数据
    # us = request.form.get('user')
    # ps = request.form.get('pswd')
    if request.method == 'POST':
        us = request.form['user']
        ps = request.form['pswd']
        print us, ps
    return render_template('001forms.html')


# include包含的使用，不能重复wtf表单对象的复用，只能实现html静态页面的内容
@app.route('/include')
def get_html():
    return render_template('001includes.html')


@app.route('/login')
def login_html():
    return render_template('001login.html')


# url_for根据视图函数找到具体url
@app.route('/redirect')
def redirect_html():
    print 'login_info run'
    return redirect(url_for('login_html'))


if __name__ == '__main__':
    print app.url_map
    app.run(debug=True)
