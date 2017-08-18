from tkinter import Tk
import win32com.client as win32
import os
import global_data


def excel():
    # 1.打开Excel应用
    app = global_data.g_app
    xl = win32.Dispatch('%s.Application' % app)

    # 2.新建工作空间
    wb = xl.Workbooks.Add()

    # 3.新建sheet
    sheetname = global_data.g_sheetname
    xl.Worksheets.Add().name = sheetname
    sh = xl.Worksheets(sheetname)
    xl.Visible = True

    # 4.往sheet中写入内容
    sh.Cells(1, 1).Value = 'scrapy websites info'
    sh.Cells(1, 2).Value = 'resource websites info'
    scrapy_websites_list = global_data.g_query_links_list
    resource_websites_set = global_data.g_url_links_set
    for i, website in enumerate(scrapy_websites_list):
        sh.Cells(i+2, 1).Value = website
    for i, resource in enumerate(resource_websites_set):
        sh.Cells(i+2, 2).Value = resource

    # 5.关闭工作空间
    pwd = global_data.g_workspace
    exclname = global_data.g_exclname
    wb.SaveAs(pwd + '\\' + '%s' % exclname)
    wb.Close(False)

    # 6.关闭应用
    xl.Application.Quit()


def __main():
    Tk().withdraw()
    global_data.g_workspace = os.getcwd()
    excel()


if __name__ == "__main__":
    __main()
