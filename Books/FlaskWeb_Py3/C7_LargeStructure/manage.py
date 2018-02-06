import os
from flask_script import Manager, Shell  #
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Role


app = create_app(os.getenv("FLASK_CONFIG") or 'default')
manager = Manager(app)  # 管理应用对象
migrate = Migrate(app, db)  # 迁移数据库


# 记录app, db, User, Role四个对象的引用
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
