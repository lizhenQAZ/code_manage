from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask


# 获取当前的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))
# 获取Flask对象
app = Flask(__name__)
# 配置Flask对象
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 获取数据库对象
db = SQLAlchemy(app)


# 创建职位对象
class Role(db.Model):
    __tablename = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

    users = db.relationship('User', backref='role')
    # 禁止自动执行查询
    # users = db.relationship('User', backref='role', lazy='dynamic')


# 创建用户对象
class User(db.Model):
    __tablename = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))


if __name__ == "__main__":
    # 创建数据库
    db.create_all()
    admin_role = Role(name='Admin')
    user_john = User(username='john', role=admin_role)
    db.session.add(admin_role)
    db.session.add(user_john)
    db.session.commit()
