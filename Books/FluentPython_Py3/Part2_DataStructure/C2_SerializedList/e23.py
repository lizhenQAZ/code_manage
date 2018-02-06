# coding: utf-8
import numpy
import random
from array import array
floats = array('d', (random.random() for i in range(10**5)))
print(floats[-1])
print()
with open('floats-10M-lines.txt', 'w') as f:
    for num in floats:
        f.write(str(num) + '\r\n')
floats = numpy.loadtxt('floats-10M-lines.txt')
print(floats[-3:])
print()
floats *= .5
print(floats[-3:])
print()
from time import perf_counter as pc
t0 = pc(); floats /= 3; print(pc() - t0); print()
numpy.save('floats-10M', floats)
floats2 = numpy.load('floats-10M.npy', 'r+')
floats2 *= 6
print(floats2[-3:])
