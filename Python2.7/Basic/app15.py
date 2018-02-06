#-*- encoding:utf-8 -*-
score=input("please enter student score:")
print '此学生的成绩是: ',score,'--对应的等级是：',
if score>=90:
    print 'A'
elif score>=60:
    print 'B'
else:
    print 'C'