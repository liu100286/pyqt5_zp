import requests
import xlrd
import xlwt
if __name__ == "__main__":
     wb = xlrd.open_workbook('./zp.xls')
     sheet1 = wb.sheet_by_index(0)
     # 获取行中所有数据，返回结果是一个列表
     tabs = sheet1.row_values(rowx=0, start_colx=0, end_colx=None)
     # print(tabs)
     # 返回一行一共有多少数据
     len_value = sheet1.row_len(rowx=0)
     # print(len_value)
     # 总行数
     nrows = sheet1.nrows
     # 总列数
     ncols = sheet1.ncols
     # 后面就通过循环即可遍历数据了
     # 取数据
     member = []
     k = ''
     z = ''
     for i in range(nrows):
          data = []
          for j in range(ncols):
               # cell_value方法取出第i行j列的数据
               value = sheet1.cell_value(i, j)
               if j == 0:
                    if value != '':
                         k = value
                    else:
                         value = k
               if j == 1:
                    if value != '':
                         z = value
                    else:
                         value = z
               data.append(value)
          member.append(data)
     print(member)
     wb = xlwt.Workbook()
     ws = wb.add_sheet('test')
     for index,value in enumerate(member):
          for index1,value1 in enumerate(value):
               ws.write(index, index1, h)
     wb.save('./test.xls')


