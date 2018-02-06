from flask import Flask, render_template, session, redirect, url_for
from abc_03 import NameForm
from flask_bootstrap import Bootstrap
from abc_02 import Role, User, db
import abc_04 as email


app = Flask(__name__)
#
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
# 创建数据库
db.drop_all()
db.create_all()
admin_role = Role(name='Admin')
user_john = User(username='john', role=admin_role)
db.session.add(admin_role)
db.session.add(user_john)
db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        # 数据库中没有记录，存入数据库
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            # 新用户
            session['known'] = False
            print("------threading-----", email.send_email(str(user)))
        # 数据库中已经有记录
        else:
            # 老用户
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))


if __name__ == '__main__':
    app.run()
