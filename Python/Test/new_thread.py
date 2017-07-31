#!usr/bin/python
# -*- coding:utf-8 -*-

#threading.thread
"""
import threading,time
count=0
lock=threading.Lock()
def doAdd():
    global count,lock
    lock.acquire()
    for i in xrange(10000):
        count+=1
    lock.release()
for j in xrange(5):
    threading.Thread(target = doAdd,args = (),name="thread-"+str(j)).start()
time.sleep(2)
print count
"""

#threading.join
"""
import threading,time
def doWaiting():
    print "start time；",time.strftime('%H:%M:%S')
    time.sleep(3)
    print "start time；",time.strftime('%H:%M:%S')
thread1=threading.Thread(target=doWaiting)
thread1.start()
time.sleep(1)
print "join start"
thread1.join()
print "join end"
"""

#threading.Lock
"""
import threading
lock=threading.Lock()
lock.acquire()
lock.acquire()
lock.release()
lock.release()
"""

#threading.RLock
"""
import threading
rlock=threading.RLock()
rlock.acquire()
rlock.acquire()
rlock.release()
rlock.release()
"""

#threading.Timer
import threading
def hello():
    print "hello,world"
t=threading.Timer(3,hello)
t.start()
