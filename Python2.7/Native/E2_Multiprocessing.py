#!usr/bin/python
# -*- coding:utf-8 -*-
import time
import os
import multiprocessing
from multiprocessing import Pool


# multiprocessing.Process
# def do(n):
#     name = multiprocessing.current_process().name
#     print name, "start"
#     print "work", n
#     return
#
# if __name__ == '__main__':
#     num_list = []
#     for i in xrange(0, 5):
#         p = multiprocessing.Process(target=do, args=(i,))
#         num_list.append(p)
#         p.start()
#         p.join()
#     print "Process end."

# pool
# def run(fn):
#     time.sleep(1)
#     print fn
#     return fn * fn
#
# if __name__ == '__main__':
#     test_list = [1, 2, 3, 4, 5]
#     print '*'*100
#     print "execute in order"
#     t1 = time.time()
#     for i in test_list:
#         run(i)
#     t2 = time.time()
#     print "order time is {}".format(int(t2-t1))
#
#     print '*'*100
#     print "execute simultaneously"
#     pool = Pool(5)
#     output = pool.map(run, test_list)
#     pool.close()
#     pool.join()
#     t3 = time.time()
#     print "simultaneous time is ",int(t3-t2)
#     print output


# read files' data
