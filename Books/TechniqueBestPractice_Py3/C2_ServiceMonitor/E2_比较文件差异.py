import difflib
import sys


"""Warning, 请以下面方式运行程序： python3 02_比较文件差异.py nginx.conf.v1 nginx.conf.v2 > diff.html"""
print(">"*20, " 比较文件差异 ", "<"*20)
try:
    textfile1 = sys.argv[1]  # 第一个配置文件路径参数
    textfile2 = sys.argv[2]  # 第二个配置文件路径参数
except Exception as e:
    print("获取系统参数出错: ", str(e))
    sys.exit()


def readfile(filename):  # 文件读取分隔函数
    try:
        fd = open(filename)
        text = fd.read().splitlines()  # 读取后以行进行分隔
        fd.close()
        return text
    except IOError as e:
        print("读取文件出错: ", str(e))


if textfile1 == '' or textfile2 == '':
    print("获取文件名出错")
    sys.exit()
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
print(d.make_file(text1_lines, text2_lines))
