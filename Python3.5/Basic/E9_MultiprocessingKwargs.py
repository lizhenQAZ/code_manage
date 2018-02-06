import multiprocessing
import os
import time


def sub_proc(name, age, **kwargs):
    print('sub pid id %d' % os.getpid())
    while True:
        print('---sub_proc---name=%s---age=%d---kwargs=%s' % (name, age, kwargs))
        time.sleep(0.5)


if __name__ == '__main__':
    print('current pid is %d' % os.getpid())
    p1 = multiprocessing.Process(target=sub_proc, args=('lizhen', 29), kwargs={'hha': 6})
    p1.start()
    while True:
        print('---main_proc---')
        time.sleep(1)
