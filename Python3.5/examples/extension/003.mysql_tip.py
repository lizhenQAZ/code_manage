# coding: utf-8
from pymysql import connect
conn = connect('localhost', 'root', 'mysql', 'test', 3306, charset='utf8')
cs = conn.cursor()

# 1. mysql增删改查
# 1.1 增加数据
sql = "insert into goods values(0, 'r510vc 15.6英寸笔记本', '笔记本', '华硕', '3399', default, default)"
cs.execute(sql)
conn.commit()
sql = "select * from goods"
cs.execute(sql)
for items in cs.fetchall():
    print(items)
print('*'*100, 1.1, '*'*100)

# 1.2 修改数据
sql = "update goods set name='0' where id between 23 and 24"
cs.execute(sql)
conn.commit()
sql = "select * from goods"
cs.execute(sql)
for items in cs.fetchall():
    print(items)
print('*'*100, 1.2, '*'*100)

# 1.3 删除数据
sql = "delete from goods"
cs.execute(sql)
conn.commit()
sql = "select * from goods"
cs.execute(sql)
for items in cs.fetchall():
    print(items)
print('*'*100, 1.3, '*'*100)

cs.close()
conn.close()
