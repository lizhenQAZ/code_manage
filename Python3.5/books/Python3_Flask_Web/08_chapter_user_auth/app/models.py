from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


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
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
        return '<User %r>' % self.username

    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # 必须实现的方法
    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return True

    def is_active(self):
        return False

    def get_id(self):
        return str(self.id)

    # confirmed = db.Column(db.Boolean, default=False)
    #
    # def generate_confirmation_token(self, expiration=3600):
    #     s = Serializer(current_app.config["SECRET_KEY"], expiration)
    #     return s.dumps({"confirm": self.id})
    #
    # def confirm(self, token):
    #     s = Serializer(current_app.config["SECRET_KEY"])
    #     try:
    #         data = s.loads(token)
    #     except:
    #         return False
    #     if data.get('confirm') != self.id:
    #         return False
    #     self.confirmed = True
    #     db.session.add(self)
    #     return True


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    u = User()
    u.password = 'cat'
    print(u.password_hash)
    print(u.verify_password('cat'))
    print(u.verify_password('dog'))
    u2 = User()
    u2.password = 'cat'
    print(u2.password_hash)
