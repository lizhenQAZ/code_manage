dest_list = []
for i in range(10):
    # print('i=%d', i)
    row_list = []
    if i == 0:
        row_list = [1]
    elif i == 1:
        row_list = [1, 1]
    else:
        for j in range(i):
            if j == 0:
                row_list.append(1)
            elif j == i-1:
                row_list.append(1)
            else:
                row_list.append(dest_list[i-1][j-1] + dest_list[i-1][j])
    dest_list.append(row_list)
    print(str(row_list)[1:-1])
print dest_list