X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

dest_list = []

for i in range(len(X)):
    row_dest_list = []
    for j in range(len(X[0])):
        sum = X[i][j] + Y[i][j]
        row_dest_list.append(sum)
    dest_list.append(row_dest_list)
print(dest_list)