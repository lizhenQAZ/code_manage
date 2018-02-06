# coding: utf-8
# 指向不同引用的列表
board = [['_'] * 3 for i in range(3)]
print(board)
print()
board[1][2] = 'X'
print(board)
print()
