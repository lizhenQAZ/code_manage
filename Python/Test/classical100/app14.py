factor=[]

def handle(num):
    for i in range(2,num+1):
        global factor
        if num%i==0 and num==i:
            factor.append(i)
        elif num%i==0 and i<num:
            factor.append(i)
            num=num/i
            return handle(num)

num=input("please enter a integer num:")
handle(num)
print num,'=',
for i in range(0,len(factor)):
    print factor[i],
    if i!=len(factor)-1:
        print '*',
print ''