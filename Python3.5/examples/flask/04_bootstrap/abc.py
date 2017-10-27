from flask import Flask, render_template
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = "you will never forget"
bootstrap = Bootstrap(app)


manager = Manager(app)


class Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired("请输入用户名")])
    password = PasswordField('Password', validators=[DataRequired("请输入密码")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit', validators=[DataRequired("请点击")])


@app.route('/')
def index():
    form = Form()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    manager.run()
