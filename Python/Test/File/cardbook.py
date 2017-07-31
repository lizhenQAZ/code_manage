#-*- encoding:utf-8 -*-
cardlist=[]

def print_menu():
    print "====================="
    print "1-增加用户信息"
    print "2-删除用户信息"
    print "3-修改用户信息"
    print "4-查找用户信息"
    print "5-查找所有用户信息"
    print "6-备份用户信息"
    print "0-退出系统"
    print "====================="

def add_info():
    global cardlist
    name=raw_input('请输入用户名：')
    addr=raw_input('请输入地址：')
    tel=raw_input('请输入电话号码：')
    card={}
    card['name']=name
    card['addr']=addr
    card['tel']=tel
    cardlist.append(card)

def del_info(name):
    global cardlist
    for card in cardlist:
        if name==card['name']:
            cardlist.remove(card)
            break

def update_info(name,key,value):
    global cardlist
    new_card={}
    flag=0
    for card in cardlist:
        if name==card['name']:
            flag=1
            cardlist.remove(card)
            new_card['name']=card['name']
            new_card['addr']=card['addr']
            new_card['tel']=card['tel']
            new_card[key]=value
            cardlist.append(new_card)
            break
    if 0==flag:
        print "没有此姓名"
    print flag

def query_info(name):
    global cardlist
    card={}
    flag=0
    print "姓名".ljust(15),"地址".ljust(15),"联系方式".ljust(15)
    for card in cardlist:
        if name==card['name']:
            flag=1
            addr=card['addr']
            tel=card['tel']
            print name.ljust(15),addr.ljust(15),tel.ljust(15)
            break
    if 0==flag:
        print "没有此姓名"

def print_messege():
    global cardlist
    card={}
    print "姓名".ljust(15),"地址".ljust(15),"联系方式".ljust(15)
    for card in cardlist:
        name=card['name']
        addr=card['addr']
        tel=card['tel']
        print name.ljust(15),addr.ljust(15),tel.ljust(15)

def save_info():
    global cardlist
    f=open('user.data','w')
    f.writelines(str(cardlist))
    f.close()

def load_info():
    global cardlist
    f=open('user.data')
    cardlist=eval(f.read())
    f.close()

def main():
    load_info()
    while True:
        print_menu()
        cmd=input('请输入要执行程序的序号：')
    #1.增加用户信息
        if cmd==1:
            add_info()
            continue
    #2.删除用户信息
        elif cmd==2:
            name=raw_input("请输入要删除数据的姓名：")
            del_info(name)
            continue
    #3.修改用户信息
        elif cmd==3:
            name=raw_input("请输入要修改数据的姓名：")
            key=raw_input("请输入要修改的属性：")
            value=raw_input("请输入修改后的值：")
            update_info(name,key,value)
            continue
    #4.查找用户信息
        elif cmd==4:
            name=raw_input("请输入要修改数据的姓名：")
            query_info(name)
            continue
    #5.查找所有用户信息
        elif cmd==5:
            print_messege()
            continue
    #6.备份用户信息
        elif cmd==6:
            save_info()
            continue
    #0.退出系统
        elif cmd==0:
            exit(0)
            break
        else:
            print "parameter is not suitable"

if __name__=="__main__":
    main()