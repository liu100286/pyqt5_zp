#
import requests
from pyquery import PyQuery as pq
import xlwt

from fake_useragent import UserAgent
import time
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys
from jinja2 import Environment, FileSystemLoader

class MyTest(QWidget):
    def __init__(self, parent=None):
        super(MyTest, self).__init__(parent)
        self.label = QLabel(self)
        # 搜索文件夹并展示文件、创建
        self.label.setText("排序方式")
        self.lineEdit = QLineEdit()
        self.button = QPushButton("开始")
        self.text = QTextEdit()
        self.button.clicked.connect(self.min1)
        grid = QGridLayout()
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.lineEdit, 0, 1)
        grid.addWidget(self.button, 0, 2)
        # 添加标题
        self.setLayout(grid)
        # 添加图标
        self.setWindowIcon(QIcon('1.ico'))

    def min1(self):
        name_ = self.lineEdit.text()
        a = 0
        arry = [];
        while a < 200:
            time.sleep(5)
            a += 1
            print(a)
            url_ = "%s%s%s%s%s" % ('https://b.faloo.com/y/0/0/0/0/0/',name_ ,'/', a, '.html')
            print(url_)
            proxies = {}
            ua = UserAgent()
            headers = {'User-Agent': ua.random}
            req = requests.get(url=url_, headers=headers)
            html = req.text
            doc = pq(html)
            # print(html)
            items = doc('.TwoBox02_02 .TwoBox02_04').items()
            for each in items:
                print(each.find('.TwoBox02_05').eq(0).find('.TwoBox02_08').text())
                arry.append(each.find('.TwoBox02_05').eq(0).find('.TwoBox02_08').text())
        wb = xlwt.Workbook()
        ws = wb.add_sheet('test')
        for index, value in enumerate(arry):
            ws.write(index, 0, value)
        wb.save('./test.xls')
if __name__ =="__main__":
    app = QApplication(sys.argv)
    demo = MyTest()
    demo.show()
    sys.exit(app.exec())