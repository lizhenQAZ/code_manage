def operate_2_num(a,b,func):
    return func(a,b)
sum = operate_2_num(11 , 15 ,lambda x,y:x+y)
print "sum is:",sum
diff= operate_2_num(15,10,lambda x,y:x-y)
print "diff is:",diff
