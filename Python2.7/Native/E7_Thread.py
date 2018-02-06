#!usr/bin/python
# -*- coding:utf-8 -*-
import threading
import time
# # threading.thread
# count = 0
# lock = threading.Lock()
#
#
# def circle_add():
#     global count, lock
#     for i in xrange(10000):
#         if lock.acquire():
#             count += 1
#             lock.release()
#
# for j in xrange(5):
#     threading.Thread(target=circle_add, args=(), name="thread-"+str(j)).start()
# time.sleep(2)
# print count


# # threading.join
# def wait():
#     print "start time: ", time.strftime('%H:%M:%S')
#     time.sleep(3)
#     print "end time: ", time.strftime('%H:%M:%S')
# thread1 = threading.Thread(target=wait)
# thread1.start()
# time.sleep(1)
# print "join start time: ", time.strftime('%H:%M:%S')
# thread1.join()
# print "join end"

# # threading.Lock 死锁
# lock = threading.Lock()
# lock.acquire()
# lock.acquire()
# lock.release()
# lock.release()

# # threading.RLock 不死锁
# rlock = threading.RLock()
# rlock.acquire()
# rlock.acquire()
# rlock.release()
# rlock.release()


# # threading.Timer
# def hello():
#     print "hello,world!"
# t = threading.Timer(3, hello)
# t.start()
