#-*- encoding:utf-8 -*-
import os
#1.提示并获取要批量重命名的文件夹
folder_name=raw_input("请输入重命名的文件夹:\n")
#2.获取需要重新命名的文件
fileslist=os.listdir(folder_name)
#3.修改当前路径为操作文件的路径
os.chdir(folder_name)
#4.批量修改文件名
# for filename in fileslist:
#     os.rename(filename,'lizhen'+filename)
for filename in fileslist:
    os.rename(filename,filename[6:])