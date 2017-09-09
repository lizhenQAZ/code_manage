from flask_migrate import Migrate, MigrateCommand
from abc_01 import app, db, Role, User
from flask_script import Manager

manager = Manager(app)
# 迁移仓库
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    general_role = Role(name='hah')
    user_susan = User(username='heheh', role=general_role)
    db.session.add(general_role)
    db.session.add(user_susan)
    db.session.commit()
    manager.run()
    # 迁移数据库操作
    # python3 abc_05.py db init
    # 迁移脚本操作
    # python3 abc_05.py db migrate -m "initial migration"
    # 更新数据库操作
    # python3 abc_05.py db upgrade
