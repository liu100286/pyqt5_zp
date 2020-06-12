from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QRadioButton,QComboBox,QInputDialog
from jinja2 import Environment, FileSystemLoader
import re
import os
import json
from untitled import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import queue
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import xlwt
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class MyMain(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getUrl)  # 查询输出
    #
    #
    def getUrl(self):
        cookie = self.lineEdit.text()
        # UserAgent = self.lineEdit_2.text()
        cookie = cookie.strip()
        newDate = datetime.datetime.now().strftime("%Y-%m-%d")
        now = datetime.datetime.now()
        delta = datetime.timedelta(days=6)
        n_days = now - delta
        endDate = n_days.strftime('%Y-%m-%d')
        count = 0
        newData = [];
        while (count <= 15):
            time.sleep(8)
            count = count + 1
            url_ = "%s%s%s%s%s%s" % ('https://ds.appgrowing.cn/api/product/rank?site=&startDate=', endDate, '&endDate=',
                                     newDate + '&timeType=range&page=', count,
                                     '&limit=20&sort=-quantitySoldIncr&isNew=false&matchType=product')
            header = {
                'cookie':cookie,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
            }
            r = requests.get(url=url_, headers=header)
            shop = r.text
            start = json.loads(shop).get('data')
            print(shop)
            for n in start:
                firstArray = time.localtime(n['firstTime'] / 1000)
                first = time.strftime("%Y--%m--%d %H:%M:%S", firstArray)
                lastArr = time.localtime(n['lastTime'] / 1000)
                last = time.strftime("%Y--%m--%d %H:%M:%S", lastArr)
                da = {
                    'finalLink': n['finalLink'],
                    'title': n['title']['highlight'],
                    'minPrice': n['minPrice'] / 100,
                    'maxPrice': n['maxPrice'] / 100,
                    'quantitySoldIncr': n['quantitySoldIncr'],
                    'quantitySold24HoursIncr': n['quantitySold24HoursIncr'],
                    'quantitySold24HoursIncrRatio': n['quantitySold24HoursIncrRatio'],
                    'quantitySold12HoursIncr': n['quantitySold12HoursIncr'],
                    'quantitySold6HoursIncr': n['quantitySold6HoursIncr'],
                    'totalQuantitySold': n['totalQuantitySold'],
                    'firstTime': first,
                    'lastTime': last,
                }
                newData.append(da)
        MyMain.xls(newData)

    def xls(val):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('test')
        ws.write(0, 0, '地址')
        ws.write(0, 1, '商品')
        ws.write(0, 2, '最小价格')
        ws.write(0, 3, '最大价格')
        ws.write(0, 4, '新增销量')
        ws.write(0, 5, '24h新增销量')
        ws.write(0, 6, '24h增长率')
        ws.write(0, 7, '12h新增销量')
        ws.write(0, 8, '6h新增销量')
        ws.write(0, 9, '累计销量')
        ws.write(0, 10, '销售开始时间')
        ws.write(0, 11, '销售结束时间')
        index = 0
        while index < len(val):
            key = 0;
            index = index + 1
            keys = list(val[index - 1])
            while key < len(keys):
                key = key + 1
                print(key)
                name = val[index - 1][keys[key - 1]];
                ws.write(index, key - 1, name)
        wb.save('./test.xls')
        print('ok')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    A1 = MyMain()
    A1.show()
    sys.exit(app.exec_())