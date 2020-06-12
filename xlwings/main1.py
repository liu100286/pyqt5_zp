import xlwings  as xw
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

wb = xw.Book('example.xlsx')
sht = wb.sheets[0]
sht.range('a1').value = 'Hello'
sht.range('a1').value = [1,2,3,4]
sht.range('a2').options(transpose=True).value = [5,6,7,8]
sht.range('a6').expand('table').value = [['a','b','c'],['d','e','f'],['g','h','i']]
a = sht.range('a1:d1').value
print(a)
for i in a:
  print(i)
  print(type(i))
a = sht.range('a:a').value
print(len(a))
rng = sht.range('a1').expand('table')
nrows = rng.rows.count
print(nrows)
a = sht.range(f'a1:a{nrows}').value
print(a)
# 选取一行
ncols = rng.columns.count
#用切片
fst_col = sht[0,:ncols].value
# wb.save('example.xlsx') #保存
# wb.close() #退出工作簿
