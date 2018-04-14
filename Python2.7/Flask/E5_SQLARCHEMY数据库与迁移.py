# coding=utf-8
"""
功能：
1.SQLALCHEMY使用：
    设置SQLALCHEMY_DATABASE_URI与SQLALCHEMY_TRACK_MODIFICATIONS
2.模型类定义：
    设置表名、反向引用、外键、主键与唯一
3.数据库迁移：
    # 1.实例化管理器对象
    manager = Manager(app)
    # 2.使用迁移扩展
    Migrate(app, db)
    # 3.使用迁移命令
    manager.add_command('db', MigrateCommand)
    # 4.执行迁移
    manager.run()
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# 导入扩展命令行
from flask_script import Manager
# 导入迁移扩展包
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

# 迁移第一步：实例化管理器对象
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://guest:guest@localhost/user'
# 动态追踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 构造数据库实例
db = SQLAlchemy(app)

# 迁移第二步：使用迁移扩展
Migrate(app, db)

# 迁移第三步：使用迁移命令
manager.add_command('db', MigrateCommand)


# 自定义模型类
class Role(db.Model):
    # 未定义时，使用同类名的表名
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 反向引用，定义在一的一方
    us = db.relationship("User", backref="role")

    def __repr__(self):
        return 'role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(32))
    # 定义在外键指向
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'user:%s' % self.name

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # 添加数据
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    # 提交数据到数据库会话对象,add_all([])一次添加多条数据
    # add()一次添加一条数据
    db.session.add_all([ro1, ro2])
    # 提交数据到数据库中
    db.session.commit()
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
    # app.run(debug=True)
    manager.run()
