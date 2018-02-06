# -*- coding: utf-8 -*-
from multiprocessing import Process
from threading import Thread
import gevent
from gevent import monkey
import time


# 打补丁
monkey.patch_all()


def gfunc1(num1, num2):
    for i in range(5):
        print('study threading-no' + str(num1) + ' concurrent-no' + str(num2) + ' task-no' + str(i))
        time.sleep(2)


def gfunc2(num1, num2):
    for i in range(5):
        print('sleep threading-no' + str(num1) + ' concurrent-no' + str(num2) + ' task-no' + str(i))
        time.sleep(2)


def tfunc1(num):
    g1_list = []
    for i in range(5):
        g1 = gevent.spawn(gfunc1, num, i)
        g1_list.append(g1)
    gevent.joinall(g1_list)


def tfunc2(num):
    g2_list = []
    for i in range(5):
        g2 = gevent.spawn(gfunc2, num, i)
        g2_list.append(g2)
    gevent.joinall(g2_list)


def func1():
    t1_list = []
    for i in range(5):
        t1 = Thread(target=tfunc1, args=(i,))
        t1_list.append(t1)
    for t in t1_list:
        t.start()


def func2():
    t2_list = []
    for i in range(5):
        t2 = Thread(target=tfunc2, args=(i,))
        t2_list.append(t2)
    for t in t2_list:
        t.start()
if __name__ == '__main__':
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p1.start()
    p2.start()
    while True:
        time.sleep(0.5)
        print('--main--')
