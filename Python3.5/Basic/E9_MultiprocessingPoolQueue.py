from multiprocessing import Pool, Manager
import os
import time


def write(q):
    for i in range(10):
        q.put_nowait(i)
        print('write %d' % i)


def read(q):
    while not q.empty():
        print('read %d' % q.get_nowait())


if __name__ == '__main__':
    print('---%s---start---' % os.getpid())
    q = Manager().Queue()
    po = Pool(10)
    po.apply_async(write, (q,))
    time.sleep(1)
    po.apply_async(read, (q,))
    po.close()
    po.join()
    print('---%s---end---' % os.getpid())