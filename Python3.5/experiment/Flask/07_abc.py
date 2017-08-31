from flask import Flask, session, redirect, url_for, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, RadioField, BooleanField
from wtforms.validators import Required


class NameForm(FlaskForm):
    # 文本字段
    name = StringField('what is your name?', validators=[Required()])
    # 提交字段
    submit = SubmitField('submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index1'))
    return render_template('index1.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    app.run()
