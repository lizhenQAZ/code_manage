#!usr/bin/python
# -*- coding:utf-8 -*-

#multiprocessing.Process
'''
import multiprocessing

def do(n):
    name=multiprocessing.current_process().name
    print name,"start"
    print "work",n
    return

if __name__=='__main__':
    num_list=[]
    for i in xrange(0,5):
        p = multiprocessing.Process(target=do,args=(i,))
        num_list.append(p)
        p.start()
        p.join()
    print "Process end."
'''

'''
#pool
import time
from multiprocessing import Pool

def run(fn):
    time.sleep(1)
    print fn
    return fn*fn

if __name__=='__main__':
    test_list=[1,2,3,4,5]
    print "execute in order"
    t1=time.time()
    for i in test_list:
        run(i)
    t2=time.time()
    print "order time is ",int(t2-t1)

    print "execute simultaneously"
    pool=Pool(5)
    output=pool.map(run,test_list)
    pool.close()
    pool.join()
    t3=time.time()
    print "simultaneous time is ",int(t3-t2)
    print output
'''

#read files' data
import os
import time
from multiprocessing import Pool

def getfile(path):
    filelist=[]
    for root,dirs,file in list(os.walk(path)):
        print root,dirs,file,'\n'
        for i in file:
             if i.endswith(".txt"):
                 filelist.append(root+"\\"+i)
    return filelist

def opendir(path):
    filepath=path
    fp=open(path)
    content=fp.readlines()
    fp.close()
    lines=len(content)
    alphaNum=0
    for i in content:
        alphaNum+=len(i.strip('\n'))
    return lines,alphaNum,filepath

def out(file,writepath):
    fileLines=0
    charNum=0
    fp=open(writepath,'a')
    for list in file:
        fp.writelines(list[2]+" 行数："+str(list[0])+" 字母："+str(list[1]))
        fileLines+=list[0]
        charNum+=list[1]
    fp.close()
    print fileLines,charNum

if __name__=='__main__':
    filepath="F:\\"
    filelist=getfile(filepath)
    pool=Pool(5)
    filecontent=pool.map(opendir,filelist)
    pool.close()
    pool.join()
    out(filecontent,"F:\\copy.txt")
