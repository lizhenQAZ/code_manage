import threading
import time


def work1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print('---work1---, g_num is %d' % g_num)


def work2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print('---work2---, g_num is %d' % g_num)


g_num = 0
t1 = threading.Thread(target=work1, args=(10000000,))
t1.start()
t2 = threading.Thread(target=work2, args=(10000000,))  # 资源竞争导致运算丢失
t2.start()
while len(threading.enumerate()) != 1:
    time.sleep(1)
print('the final num is %d' % g_num)