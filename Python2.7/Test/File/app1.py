# -*- encoding:utf-8 -*-
# #1.打开文件
# f=open('empty.txt','w')
# #2.写入数据
# #f.write('hello!')
# #3.关闭文件
# f.close()

# #1.打开文件
# f2=open('empty.txt','r')
# #2.读取数据并打印
# content=f2.readlines()
# print content
# #3.关闭文件
# f2.close()

#1.打开两个文件
old_filename="empty.txt"
post=old_filename.rfind('.')
new_filename=old_filename[:post]+"(复制)"+old_filename[post:]
f3=open(old_filename,'r')
f4=open(new_filename.decode('utf-8'),'w')
#2.读取数据并写入另一个文件
content=f3.readlines()
f4.writelines(content)
#3.关闭两个文件
f3.close()
f4.close()

#1.打开两个文件
old_filename="empty.txt"
post=old_filename.rfind('.')
new_filename=old_filename[:post]+"(大文件)"+old_filename[post:]
f5=open(old_filename,'r')
f6=open(new_filename.decode('utf-8'),'a+')
#2.读取数据并写入另一个文件
while True:
    content=f5.read(5)
    if len(content)>0:
        f6.writelines(content)
    else:
        break
#3.关闭两个文件
f5.close()
f6.close()
