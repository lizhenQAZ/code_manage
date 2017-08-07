import threading
import time


def work1():
    if mutex1.acquire():
        print('----work1---start---')
        time.sleep(1)
        if mutex2.acquire():
            print('---work1---finish---')
            mutex2.release()
        mutex1.release()


def work2():
    if mutex2.acquire():
        print('---work2---start---')
        time.sleep(1)
        if mutex1.acquire():
            print('---work2----finish---')
            mutex1.release()
        mutex2.release()


mutex1 = threading.Lock()
mutex2 = threading.Lock()
t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)  # 时间不满足导致死锁
t1.start()
t2.start()