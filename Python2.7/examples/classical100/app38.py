str_2d=[[1,2,3],[5,6,7],[6,5,4]]
row=len(str_2d)
sum=0
for i in range(row):
    sum+=str_2d[i][i]
print sum