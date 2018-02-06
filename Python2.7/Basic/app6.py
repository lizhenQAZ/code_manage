#!/usr/bin/python
def add(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return add(n-1)+add(n-2)

def excute(add):
        print add

if __name__=="__main__":
    excute(add(5))