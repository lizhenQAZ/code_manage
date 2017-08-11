from tkinter import Tk
import win32com.client as win32
from time import sleep
from tkinter.messagebox import showwarning


warn = lambda app: showwarning(app, 'Exit?')


def excel():
    # 1.打开Excel应用
    app = 'Excel'
    xl = win32.Dispatch('%s.Application' % app)

    # 2.新建工作空间
    ws = xl.Workbooks.Add()

    # 3.新建sheet
    sh = ws.ActiveSheet
    xl.Visible = True
    sleep(1)

    # 4.往sheet中写入内容
    sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app
    sleep(1)

    for i in range(3, 8):
        sh.Cells(i, 1).Value = 'Line %d' % i
        sleep(1)
    sh.Cells(i+2, 1).Value = '''that's all folks'''
    warn(app)

    # 5.关闭工作空间
    ws.Close(True)

    # 6.关闭应用
    xl.Application.Quit()


if __name__ == "__main__":
    Tk().withdraw()
    excel()