from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QTimer
import requests
import json
from threading import Timer
class landPage_info(object):
    def get_landpage_Info(self):
        self.landpage_num_old = 0;
        self.landpage_num_new = 0;
        url_ = 'http://sso.lzad.cc/api/login'
        data={
            'email':'930056380@qq.com',
            'password':'13466862612'
        }
        r = requests.post(url=url_,data=data)
        self.token = r.json()['token']
        self.list_info  =[];
        self.MonitorSystem()

    def getLandpage_data(self):
        _translate = QtCore.QCoreApplication.translate
        # # 获取接口
        url_landpage = 'http://sucai.lzad.cc/tasklist?state=2&page=1&per-page=999&search ='
        header = {
            'Authorization':self.token ,
        }
        tasklist = requests.get(url=url_landpage, headers=header)
        list_info = tasklist.json()['list']
        self.tableWidget_3.setRowCount(len(list_info))
        self.landpage_num_new = len(list_info)
        for index, data in enumerate(list_info):
            url = data['url']
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(index, 0, item)
            item = self.tableWidget_3.item(index, 0)
            item.setText(_translate("Form", url))
            yushan_name = data['yushan_name']
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget_3.setItem(index, 1, item)
            item = self.tableWidget_3.item(index, 1)
            item.setText(_translate("Form", yushan_name))
            # searchBtn = QPushButton("领取")
            # searchBtn.index = [{
            #     'index':index,
            #     'data':data
            # }]
            # searchBtn.clicked.connect(self.tableClick)  # 表格加点击事件
            # self.tableWidget_3.setCellWidget(index, 2, searchBtn)

        self.window2 = MyWindow2()  # 自定义窗口
        self.window2.before_close_signal.connect(self.echo)  # 接收自定义窗口关闭时发送过来的信号，交给 echo 函数显示


    def echo(self, value):
        '''显示对话框返回值'''
        QMessageBox.information(self, "返回值", "得到：{}\n\ntype: {}".format(value, type(value)),
                                QMessageBox.Yes | QMessageBox.No)

    # pass
    def MonitorSystem(self):
        self.getLandpage_data()
        Timer(300, self.MonitorSystem).start()

    def tableClick(self, event):  # 输入：文本
        self.window2.show()
        # value, ok = QInputDialog.getText(self, "输入完成落地页", "输入完成落地页:", QLineEdit.Normal, "")
        # if value and ok:
        #     value = value.split(',')
        #     new_value = [];
        #     for n in value:
        #         z = "%s%s%s" % ('/',n,'.html')
        #         new_value.append(z)
        #     if value == '':
        #         return
        #     else:
        #         print(new_value)
        #         data_ = self.sender().index[0]['data'];
        #         landPage_info.ajaxPush(self,data_,new_value)

    def ajaxPush(self,data,new_value):
        self.window2.show()
            # 获取接口
            # id = data['id']
            # appid = data['appid']
            # domain = data['url']
            # submituser = data['submituser']
            #
            # print(setPageData)
            # url_landpage = "%s%s" % ('http://sucai.lzad.cc/api/tasks/', id)
            # header = {
            #     'Authorization': self.token,
            # }
            # data = {
            #     'progress': "3",
            #     'webid': submituser
            # }
            # putInfo = requests.put(url=url_landpage, headers=header,data=data)
            # a = putInfo.json()
            # if a[0] == 1:
            #     QtWidgets.QMessageBox.about(self, '提示', "领取成功")
            # setPageData = {
            #     'appid': appid,
            #     'domain': domain,
            #     'pages': ['/lp2.html']
            # }
            #     setPage = 'http://www.moushiapp.com/landpageManager/setPage'
            #     putInfoOk = requests.post(url=setPage, headers=header, data=setPageData)
            #     b = putInfoOk.json()
            #     print(b)
                # if b['data'] == 'ok':
                #     self.getLandpage_data()
                #     QtWidgets.QMessageBox.about(self, '提示', "提交完成")
                # else:
                #     QtWidgets.QMessageBox.about(self, '提示', "提交失败")
class MyWindow2(QWidget):
    '''自定义窗口'''
    # 知识点：
    # 1.为了得到返回值用到了自定义的信号/槽
    # 2.为了显示动态数字，使用了计时器

    before_close_signal = pyqtSignal(int)  # 自定义信号（int类型）

    def __init__(self):
        super().__init__()

        self.sec = 0
        self.setWindowTitle('自定义窗口')
        self.resize(200, 150)

        self.lcd = QLCDNumber(18, self)
        btn1 = QPushButton(self, text="测试")
        btn2 = QPushButton(self, text="关闭")

        layout = QVBoxLayout(self)
        layout.addWidget(self.lcd)
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        self.timer = QTimer()

        self.timer.timeout.connect(self.update)  # 每次计时结束，触发update
        btn1.clicked.connect(self.startTimer)
        btn2.clicked.connect(self.stopTimer)  # 去到关闭前的处理

    def update(self):
        self.sec += 1
        self.lcd.display(self.sec)  # LED显示数字+1

    def startTimer(self):
        self.timer.start(1000)  # 计时器每秒计数

    def stopTimer(self):
        self.timer.stop()
        self.sec = 0
        self.before_close_signal.emit(self.lcd.value())  # 发送信号，带参数 888
      