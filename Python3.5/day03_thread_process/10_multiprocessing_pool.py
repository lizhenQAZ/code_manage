from multiprocessing import Pool
import time,os


def work1(n):
    print('current work is %d, pid = %d' % (n, os.getpid()))
    time.sleep(0.5)

if __name__ == '__main__':
    po = Pool(3)
    for i in range(10):
        po.apply_async(work1, (i,))
    po.close()
    po.join()
    print('---main_thread is over---')