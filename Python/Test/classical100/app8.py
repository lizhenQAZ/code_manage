#!/usr/bin/python
for i in range(1,10):
    for j in range(1,i+1):
        print str(i)+' * '+str(j)+' = '+str(i*j)+'\t',
        #print "%d * %d = %d"%(i,j,i*j),
    print '\n'
