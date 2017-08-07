import multiprocessing


def write(q):
    i = 0
    while not q.full():
        q.put_nowait(i)
        print('write %d' % i)
        i +=1


def read(q):
    while not q.empty():
        print('read %s' % q.get_nowait())

if __name__  == '__main__':
    q = multiprocessing.Queue(10)
    p1 = multiprocessing.Process(target=write, args=(q,))
    p2 = multiprocessing.Process(target=read, args=(q,))
    p1.start()
    p1.join()
    p2.start()