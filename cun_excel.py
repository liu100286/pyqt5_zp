from bs4 import BeautifulSoup,sys
import requests
import xlwt
if __name__ == "__main__":
     wb = xlwt.Workbook()
     ws = wb.add_sheet('test')
     ws.write(0, 0, '第1列')
     ws.write(0, 1, '第2列')
     ws.write(0, 2, '第3列')
     style = xlwt.XFStyle()
     font = xlwt.Font()
     font.bold = True
     font.underline = True
     style.font = font
     # 然后应用
     # 单元格对齐
     alignment = xlwt.Alignment()

     # 水平对齐方式和垂直对齐方式
     alignment.horz = xlwt.Alignment.HORZ_CENTER
     alignment.vert = xlwt.Alignment.VERT_CENTER
     # 自动换行
     alignment.wrap = 1
     style.alignment = alignment
     ws.col(0).width = 6666

     # 背景色
     pattern = xlwt.Pattern()
     pattern.pattern = xlwt.Pattern.SOLID_PATTERN

     # 背景色为黄色
     # 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,
     # 7 = Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = Dark Yellow ,
     # almost brown), 20 = Dark Magenta, 21 = Teal, 22 = Light Gray, 23 = Dark Gray
     # ...
     pattern.pattern_fore_colour = 5
     style.pattern = pattern

     # 边框
     borders = xlwt.Borders()

     # 边框可以分别设置top、bottom、left、right
     # 每个边框又可以分别设置颜色和线样式：实线、虚线、无
     # 颜色设置，其他类似
     borders.left_colour = 0x40
     # 设置虚线，其他类似
     borders.bottom = xlwt.Borders.DASHED
     style.borders = borders

     # 然后应用
     ws.write(2, 1, 'test', style)
     # 超链接
     link = 'HYPERLINK("http://www.baidu.com";"Baidu")'
     formula = xlwt.Formula(link)
     ws.write(2, 0, formula)

     # 公式也是类似
     ws.write(1, 1, xlwt.Formula('SUM(A1,B1)'))

     # 时间
     # style.num_format_str = 'M/D/YY'
     # ws.write(2, 1, datetime.datetime.now(), style)
     # 保存excel文件
     wb.save('./test.xls')