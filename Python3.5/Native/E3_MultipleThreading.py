# -*- coding: utf-8 -*-
from threading import Thread
import time


def func1(num):
    time.sleep(2)
    print('study' + str(num))


def func2(num):
    time.sleep(2)
    print('sleep' + str(num))
t_list = []
for i in range(5):
    t1 = Thread(target=func1, args=(i,))
    t_list.append(t1)
for i in range(5):
    t2 = Thread(target=func2, args=(i,))
    t_list.append(t2)
for t in t_list:
    t.start()
