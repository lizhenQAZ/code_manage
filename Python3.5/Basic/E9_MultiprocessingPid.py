import multiprocessing
import os
import time


def sub_proc():
    print('sub pid id %d' % os.getpid())
    while True:
        print('---sub_proc---')
        time.sleep(0.5)


if __name__ == '__main__':
    print('current pid is %d' % os.getpid())
    p1 = multiprocessing.Process(target=sub_proc)
    p1.start()
    while True:
        print('---main_proc---')
        time.sleep(1)