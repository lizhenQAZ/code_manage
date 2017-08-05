#-*- encoding:utf-8 -*-
class SweetPotato:
    def __init__(self):
        self.cooked_string ='生的'
        self.cooked_time =0
        self.items = []

    def __str__(self):
        return "地瓜的状态：%s,地瓜的佐料：%s" % (self.cooked_string,str(self.items))

    def cook(self, new_cooked_time):
        self.cooked_time+=new_cooked_time
        if  0<=self.cooked_time<=3:
            self.cooked_string='生的'
        elif 3<self.cooked_time<=5:
            self.cooked_string='半生不熟'
        elif 5<self.cooked_time<=8:
            self.cooked_string='熟了'
        else:
            self.cooked_string='烤糊了...'

    def add_items(self, new_items):
            self.items.append(new_items)

# 创建一个地瓜对象
di_gua=SweetPotato()

# 烤地瓜
di_gua.cook(2)
di_gua.add_items("番茄酱")
print di_gua
di_gua.cook(2)
di_gua.add_items("奶酪")
print di_gua
