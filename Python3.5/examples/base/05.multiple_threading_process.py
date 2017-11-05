# -*- coding: utf-8 -*-
from multiprocessing import Process
from threading import Thread
import time


def tfunc1(num):
    time.sleep(2)
    print('study' + str(num))


def tfunc2(num):
    time.sleep(2)
    print('sleep' + str(num))


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
        time.sleep(1)
        print('--main--')
