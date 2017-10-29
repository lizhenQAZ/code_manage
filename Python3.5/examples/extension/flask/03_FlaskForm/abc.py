from flask import Flask, render_template
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "you will never forget"
manager = Manager(app)


class Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit', validators=[DataRequired()])


@app.route('/')
def index():
    form = Form()
    return render_template('index.html', form=form)


if __name__ == '__main__':
    manager.run()
