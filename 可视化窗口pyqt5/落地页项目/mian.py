import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QDialog,QMdiArea, QMdiSubWindow, QLabel
from PyQt5.QtCore import Qt
from lxml import etree
from untitled import Ui_Form
from iframe import get_iframe
from muban import get_muban
from banquan import get_banquan
from landpageChange import get_landpageChane
from landpageChange_move import get_landpageChange_move
from button_class import get_button_class
from html_muban import get_html_muban
from add_html import get_add_html
from add_down_js import get_add_down_js
from landpage_info import landPage_info

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWebEngineWidgets import *

import psutil
import time
import datetime
import socket


class MyMain(QMainWindow, Ui_Form,get_iframe,get_muban,get_banquan,get_landpageChane,get_button_class,get_html_muban,get_add_html,get_landpageChange_move,get_add_down_js,landPage_info):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # # ------定义QMdiArea,用来放置子窗口------
        # self.area = QMdiArea()
        # self.verticalLayout_2.addWidget(self.area)
        # MyMain.showWindow(self)
        self.socketIp = socket.gethostbyname(socket.gethostname())
        self.pushButton.clicked.connect(self.getstr)  # 查询输出
        self.pushButton_6.clicked.connect(self.copy_href)  # 复制域名
        self.radio_name = ''
        self.radioButton.toggled.connect(lambda: self.banquan_info(self.radioButton))  # 单选按钮
        self.radioButton_2.toggled.connect(lambda: self.banquan_info(self.radioButton_2))  #  单选按钮
        self.radioButton_3.toggled.connect(lambda: self.banquan_info(self.radioButton_3))  #  单选按钮
        self.comboText = '下载按钮悬浮';
        self.comboBox.activated[str].connect(self.muban_info) #下拉菜单
        self.buttonType = '无';
        self.comboBox_2.activated[str].connect(self.button_type) #下拉菜单 选择按钮类型
        self.lineEdit_3.setText('')
        self.textEdit_2.setPlainText("""{
"background":[
"图片地址",
],
"xuanfu":[
"按钮悬浮图片地址"
],
"no_xuanfu":[
"按钮不悬浮图片地址"
],
'video_img':[
"视屏背景"
],
'video_icon':[
'http://img.zntec.mobi/0.42546545550013803.png'
],
'video':[
"视屏地址"
],
'popUp':'弹窗背景',
'popUpDown':'弹窗背景下载',
'zhezhao_pop':0,
'zhezhao_down':0,
}""")
        self.pushButton_2.clicked.connect(self.settingHtml)  # 映射html
        self.pushButton_5.clicked.connect(self.getHtml)  # 新建html
        self.pushButton_7.clicked.connect(self.getCopyHtml)  # 新建html，复制线上地址
        self.iframe = False
        # 落地页项目迁移换户
        self.pushButton_4.clicked.connect(self.landpageChane)  # 查询输出
        self.pushButton_3.clicked.connect(self.newlandpageChane)  # 移动
        # 下拉框是否是iframe，隐藏显示输入框
        self.iframe_info(self)
        # ----web
        self.browser = QWebEngineView()
        self.browser.setObjectName("browser")
        self.verticalLayout.addWidget(self.browser)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
    # 获取落地页项目优化师提交内容
        self.get_landpage_Info()
    # 打开新窗口--未用
    def showWindow(self):
        # 创建一个新的窗口
        subwindow = QMdiSubWindow()

        # 为子窗口添加组件
        self.browser = QWebEngineView()
        subwindow.setGeometry(0, 0, 1200, 600)
        # 加载外部的web界面
        self.browser.load(QUrl('http://sso.lzad.cc/#/'))


        subwindow.setWindowTitle('落地页')
        subwindow.setWidget(  self.browser)
        # 将字窗口添加到区域QmdiArea
        self.area.addSubWindow(subwindow)
        # 子窗口显示
        subwindow.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    A1 = MyMain()
    A1.show()
    sys.exit(app.exec_())

#from PyQt5.QtWebEngineWidgets import *
# self.browser = QWebEngineView()
# self.browser.setObjectName("browser")
# self.verticalLayout.addWidget(self.browser)