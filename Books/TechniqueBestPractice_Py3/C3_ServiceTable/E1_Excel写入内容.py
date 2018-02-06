import xlsxwriter


workbook = xlsxwriter.Workbook("E1_Demo.xlsx")  # 创建Excel文件
worksheet = workbook.add_worksheet()  # 创建工作表对象

worksheet.set_column("A:A", 20)  # 设定第一列(A)宽度为20像素
bold = workbook.add_format({'bold': True})  # 方式一定义一个加粗的格式对象
# bold = workbook.add_format()  # 方式二定义一个加粗的格式对象
# bold.set_bold()
worksheet.set_row(0, None, None, {'hidden': True})  # 操作第一行格式
worksheet.set_column(0, 1, 10)  # 操作第0,1列格式, 宽度为10像素
worksheet.set_column("E:G", None, None, {"hidden": 1})  # 操作E,G列格式, 隐藏单元格

worksheet.write('A1', "Hello")
worksheet.write('A2', "World", bold)  # 对文档内容加粗
worksheet.write("B2", u"中文测试", bold)

worksheet.write(2, 0, 32)  # 行列表示法操作单元格
worksheet.write(3, 0, 35.5)
worksheet.write(4, 0, "=SUM(A3:A4)")

worksheet.insert_image('B5', "E1_Pic.png", {'url': 'http://python.org'})  # 插入图片并设立超链接


chart = workbook.add_chart({'type': 'column'})
chart.set_size({'width': 577, 'height': 287})
chart.set_title({'name': u"业务流量周报图表"})
chart.set_y_axis({'name': u"Mb/s"})
worksheet.insert_chart('A80', chart)
workbook.close()  # 关闭Excel表格
