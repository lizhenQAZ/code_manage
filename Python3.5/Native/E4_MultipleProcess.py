# -*- coding: utf-8 -*-
from multiprocessing import Process
import time


def func1():
    for i in range(5):
        time.sleep(2)
        print('study' + str(i))


def func2():
    for i in range(5):
        time.sleep(2)
        print('sleep' + str(i))
if __name__ == '__main__':
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p1.start()
    p2.start()
    while True:
        time.sleep(1)
        print('--main--')
