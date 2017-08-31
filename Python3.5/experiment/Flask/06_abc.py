from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, RadioField, BooleanField
from wtforms.validators import Required


class NameForm(Form):
    # 文本字段
    name = StringField('what is your name?', validators=[Required()])
    # 提交字段
    submit = SubmitField('submit')
    # 密码表单字段
    pwd1 = PasswordField('请输入你的密码：', validators=[Required()])
    pwd2 = PasswordField('确认密码：', validators=[Required(), EqualTo('pwd1', message='密码不匹配')])
    # 单选按钮字段
    radio = RadioField('sex', choices=[(1, 'one'), (2, 'two')])
    # 多选框字段
    checkbox = BooleanField('one', default=True)
