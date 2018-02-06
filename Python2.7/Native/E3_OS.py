#!usr/bin/python
# -*- coding:utf8 -*-
import os
import shutil
import time

cur_time = repr(time.time())
origin_dir = os.getcwd()
# os.mkdir
mkdir_name = "03_mkdir" + cur_time
os.mkdir(mkdir_name)
print '*'*100
print os.listdir(".")

# os.rename
rendir_name = "03_rename" + cur_time
os.rename(mkdir_name, rendir_name)
print '*'*100
print os.listdir(".")

# os.rmdir
rmdir_name = rendir_name
os.rmdir(rmdir_name)
print '*'*100
print os.listdir(".")

# os.chdir
os.chdir(origin_dir.split(os.sep)[0] + os.sep)
print '*'*100
print os.listdir(".")
os.chdir(origin_dir)
print os.listdir(".")

# # shutil.copyfile
# shutil.copyfile(src_file,tar_file)
# print '*'*100
# print os.listdir(".")
#
# # shutil.copy
# shutil.copy(src_dir, tar_dir)
# print '*'*100
# print os.listdir(".")
#
# # shutil.copytree
# shutil.copytree(src_dir, tar_dir)
# print '*'*100
# print os.listdir(".")
#
# # shutil.move
# shutil.move(src_dir, tar_dir)
# print '*'*100
# print os.listdir(".")
#
# # shutil.rmtree
# shutil.rmtree(src_dir)
# print '*'*100
# print os.listdir(".")
#
# # os.getcwd()
# print '*'*100
# print os.getcwd()
#
# # os.curdir
# print '*'*100
# print os.curdir
#
# # os.sep
# print '*'*100
# print os.sep
#
# os.getenv()
# print '*'*100
# print os.getenv('pythonpath')
#
# # os.putenv()
# print '*'*100
# print os.putenv()
#
# # os.path.isfile()
# print '*'*100
# print os.path.isfile("C:/")
#
# # os.path.isdir()
# print '*'*100
# print os.path.isdir("C:/")
#
# # os.path.isabs()
# print '*'*100
# print os.path.isabs("C:/")
#
# # os.path.exists()
# print '*'*100
# print os.path.exists("C:/")
#
# # os.path.split()
# print '*'*100
# print os.path.split("D:/Python/text_dump.txt")
#
# # os.path.splitext()
# print '*'*100
# print os.path.splitext("D:/Python/text_dump.txt")
#
# # os.path.basename()
# print '*'*100
# print os.path.basename("D:/Python/text_dump.txt")
#
# # os.path.dirname()
# print '*'*100
# print os.path.dirname("D:/Python/text_dump.txt")
#
# # os.path.abspath()
# print '*'*100
# print os.path.abspath("D:/Python/text_dump.txt")
