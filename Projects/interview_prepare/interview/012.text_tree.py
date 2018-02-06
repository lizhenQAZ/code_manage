# coding: utf-8
import os

# os.walk
t = os.walk(".")
for root, dirs, files in t:
    for file in files:
        # print(os.path.join(root, file))
        pass


# os.listdir
def walk_dir(dirs):
    try:
        t = os.listdir(dirs)
    except Exception as e:
        print("access deny!")
    else:
        for l in t:
            temp = os.path.join(dirs, l)
            if (os.path.isdir(temp)):
                walk_dir(temp)
            else:
                print(temp)
if __name__ == '__main__':
    walk_dir(".")
