from tkinter import Tk
import win32com.client as win32
import os


pwd = os.getcwd()
sheetname = 'worksheet1'
exclname = 'Excel.xlsx'


def excel():
    # 1.打开Excel应用
    app = 'Excel'
    xl = win32.Dispatch('%s.Application' % app)

    # 2.新建工作空间
    wb = xl.Workbooks.Add()

    # 3.新建sheet
    xl.Worksheets.Add().name = sheetname
    sh = xl.Worksheets(sheetname)
    xl.Visible = True

    # 4.往sheet中写入内容
    sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app

    for i in range(3, 8):
        sh.Cells(i, 1).Value = 'Line %d' % i
    sh.Cells(i+2, 1).Value = '''that's all folks'''

    # 5.关闭工作空间
    wb.SaveAs(pwd + '\\' + '%s' % exclname)
    wb.Close(False)

    # 6.关闭应用
    xl.Application.Quit()


if __name__ == "__main__":
    Tk().withdraw()
    excel()
