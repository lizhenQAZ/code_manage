list=[]
for i in range(100,1000):
    hun=i/100
    ten=i/10%10
    num=i%10
    if i==hun**3+ten**3+num**3:
        list.append(i)
print list