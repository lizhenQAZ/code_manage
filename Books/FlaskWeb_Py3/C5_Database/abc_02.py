from abc_01 import db, Role, User

if __name__ == "__main__":
    # 删除数据库
    db.drop_all()
    # 创建数据库
    db.create_all()
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)
    print('===================>创建之前<=======================')
    print(Role.query.all())
    print(User.query.all())
    # 加入数据库
    user_list = [admin_role, mod_role, user_role, user_john, user_susan, user_david]
    db.session.add_all(user_list)
    db.session.commit()
    print('===================>创建之后<=======================')
    print(admin_role.id)
    print(Role.query.all())
    print(User.query.all())
    # 修改行
    admin_role.name = 'Administrator'
    db.session.add(admin_role)
    db.session.commit()
    print('===================>修改行<========================')
    print(Role.query.all())
    print(User.query.all())
    # 删除行
    print('===================>删除行<========================')
    db.session.delete(mod_role)
    db.session.commit()
    print(Role.query.all())
    print(User.query.all())
    # 查询所有行
    print('===================>查询所有行<=====================')
    print(Role.query.all())
    print(User.query.all())
    # 查询指定行一个结果
    print('===================>查询指定行一个结果<=====================')
    print(User.query.filter_by(role=user_role).first())
    # 查询指定行所有结果
    print('===================>查询指定行所有结果<=====================')
    print(User.query.filter_by(role=user_role).all())
    # 将查询对象转化为字符串
    print('=================>将对象转化为字符串<================')
    print(str(User.query.filter_by(role=user_role)))
    # 查询角色和用户的对应关系
    print('=============>查询角色和用户的对应关系<===============')
    print(user_role.users)
    print(admin_role.users)
    # print(mod_role.uesrs)
    print(user_role.users[0].role)
    print(admin_role.users[0].role)
    # print(mod_role.uesrs)
    # 查询过滤
    print('====================>查询过滤<======================')
    print(user_role.users.order_by(User.username).all())
    print(user_role.users.count())
