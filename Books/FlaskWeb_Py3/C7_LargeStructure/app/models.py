from . import db


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
