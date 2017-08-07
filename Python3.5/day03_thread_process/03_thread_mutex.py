import threading
import time


def work1(num):
    global g_num
    for i in range(num):
        flag = mutex.acquire(True)
        if flag:
            g_num += 1
            mutex.release()
    print('---work1---, g_num is %d' % g_num)


def work2(num):
    global g_num
    for i in range(num):
        flag = mutex.acquire(True)
        if flag:
            g_num += 1
            mutex.release()
    print('---work2---, g_num is %d' % g_num)


g_num = 0
mutex = threading.Lock()
t1 = threading.Thread(target=work1, args=(10000000,))
t1.start()
t2 = threading.Thread(target=work2, args=(10000000,))  # 互斥锁解决资源竞争问题
t2.start()
while len(threading.enumerate()) != 1:
    time.sleep(1)
print('the final num is %d' % g_num)