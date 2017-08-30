import multiprocessing


q = multiprocessing.Queue(3)
i = 0
while not q.full():
    q.put_nowait('message%d' % i)
    i += 1
while not q.empty():
    content = q.get_nowait()
    print('result---%s---' % content)