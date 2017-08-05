#!usr/bin/python
# -*- coding:utf8 -*-
import os , shutil

#os.mkdir
os.mkdir("test201705291855")
print os.listdir(".")

#os.rename
os.rename("test201705291855","test201705291856")
print os.listdir(".")

#os.rmdir
os.rmdir("test201705291856")
print os.listdir(".")

"""
#os.chdir
os.chdir("C:/")
print os.listdir(".")
"""

"""
#shutil.copyfile shutil.copy shutil.copytree
path=os.getcwd()
print path,type(path)
src_dir=os.path.join(path,"test2017052801.py")
tar_dir=os.path.join(path,"test2017052801_new.py")
shutil.copyfile(src_dir,tar_dir)
print os.listdir(".")
tar_dir1=path+"new_directory1"
shutil.copy(path,tar_dir1)
print os.listdir(".")
tar_dir2=path+"\new_directory2"
shutil.copytree(path,tar_dir2)
print os.listdir(".")
"""

#shutil.move
path=os.getcwd()
path=os.path.join(path,"print_function")
shutil.move(path,"D:\Python\Learn")
os.listdir(".")
shutil.move("D:\Python\Learn\print_function",path)

"""
#shutil.rmtree
shutil.rmtree("D:\Python\Test_Empty")
"""

#os.mknod
"""
os.mknod("text_dump.txt")
"""

"""
fp=open("text_dump.txt","w")
fp.write("nihao!")
fp.writelines(["python\n","hello"])
fp.flush()
fp.tell()
fp.close()

fp=open("text_dump.txt","r")
str1=fp.read(2)
print str1
str2=fp.readline(4)
print str2
str3=fp.readlines()
print str3
print fp.fileno()
print fp.isatty()
fp.close()
"""

#os.getcwd os.sep os.getenv os.putenv os.path.isfile os.path.isdir os.path.isabs os.path.exists os.path.split os.path.splitext os.path.basename os.path.dirname os.path.abspath
print os.getcwd()
print os.curdir
print os.sep
#print os.getenv()
#print os.putenv()
print os.path.isfile("C:/")
print os.path.isdir("C:/")
print os.path.isabs("C:/")
print os.path.exists("C:/")
print os.path.split("D:/Python/text_dump.txt")
print os.path.splitext("D:/Python/text_dump.txt")
print os.path.basename("D:/Python/text_dump.txt")
print os.path.dirname("D:/Python/text_dump.txt")
print os.path.abspath("D:/Python/text_dump.txt")