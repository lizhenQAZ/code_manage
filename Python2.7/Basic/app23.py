for i  in range (8):
    if 0<=i<3:
        print ' '*(3-i),'*'*(2*i+1)
    elif 3==i:
        print '','*'*(2*i+1)
    else:
        print ' '*(i-3),'*'*(13-2*i)