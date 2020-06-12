from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QRadioButton,QComboBox,QInputDialog
from jinja2 import Environment, FileSystemLoader
import re
import os
import json

class MyTest(QWidget):
    def __init__(self, parent=None):
        super(MyTest, self).__init__(parent)
        self.label = QLabel(self)
        # 搜索文件夹并展示文件、创建
        self.label.setText("搜索域名")
        self.lineEdit = QLineEdit()
        self.button = QPushButton("开始")
        self.text = QTextEdit()
        self.button.clicked.connect(self.getstr)
        # 创建html------------------------------------------------------
        self.label_html = QLabel(self)
        self.label_html.setText("添加html")
        self.lineEdit_add_html = QLineEdit()
        # 搜索文件夹并展示文件、创建
        self.label_banquan = QLabel(self)
        self.label_banquan.setText("版权:")
        # 单选按钮
        self.btn1 = QRadioButton('智道未来')
        self.btn1.toggled.connect(lambda: self.btnstate(self.btn1))  # 绑定点击事件
        self.btn1.setChecked(True)
        self.btn2 = QRadioButton('智鸟')
        self.btn2.toggled.connect(lambda: self.btnstate(self.btn2))  # 绑定点击事件
        self.radio_name = '智道未来';
        # 选择模板

        self.label_muban = QLabel(self)
        self.label_muban.setText("模板:")
        combo = QComboBox(self)
        combo.addItem("下载按钮悬浮")
        combo.addItem("底部下载")
        combo.addItem("不需要")
        self.comboText = '下载按钮悬浮';
        combo.activated[str].connect(self.muban)

        self.lineEdit_add_img = QTextEdit()
        self.button_add_html = QPushButton("创建")
        self.button_add_html.clicked.connect(self.getHtml)
        self.lineEdit_add_img.setPlainText("""{
                   "background":[
                    "图片地址",
                   ],
                  "button":[
                    "按钮图片地址"
                   ]
                  }""")
        grid = QGridLayout()
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.lineEdit, 0, 1)
        grid.addWidget(self.button, 0, 2)
        grid.addWidget(self.text, 1, 1)
        grid.addWidget(self.label_html, 2, 0)
        grid.addWidget(self.lineEdit_add_html, 2, 1)
        grid.addWidget(self.label_banquan, 3, 0)
        grid.addWidget(self.btn1, 3, 1)
        grid.addWidget(self.btn2, 3, 2)
        grid.addWidget(self.label_muban, 4, 0)
        grid.addWidget(combo, 4, 1)
        grid.addWidget(self.lineEdit_add_img,5,1)
        grid.addWidget(self.button_add_html,5,2)
        #添加标题
        self.setLayout(grid)
        self.setWindowTitle("获取本地文件目录")
        #添加图标
        self.setWindowIcon(QIcon('1.ico'))
    def btnstate(self,btn):
        if btn.text() == "智道未来":
            if btn.isChecked() == True:
                self.radio_name = '智道未来'
            else:
                print(btn.text() + " is deselected")

        if btn.text() == "智鸟":
            if btn.isChecked() == True:
                self.radio_name = '智鸟'
            else:
                print(btn.text() + " is deselected")
    def muban(self, text):
        self.comboText = text;
        if text == '下载按钮悬浮':
            self.lineEdit_add_img.setVisible(True)
            self.lineEdit_add_img.setPlainText("""{
                "background":[
                 "图片地址",
                ],
               "button":[
                 "按钮图片地址"
                ]
               }""")
        elif text == '底部下载':
            self.lineEdit_add_img.setPlainText("""{
              "background":[
               "图片地址",
              ],
             "button_background":[
               "按钮图片背景"
              ],
              "button":[
               "按钮图片按钮"
              ]
             }""")
        elif text == '不需要':
            self.lineEdit_add_img.setPlainText('')
    # ----------------------------------判断文件夹是否存在，创建文件夹
    def getstr(self):
        url = self.lineEdit.text()

        if url != '':
            u = 'C:\\Users\\Administrator\\Desktop\\lz_git\\landpage_static'
            u1 = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
            url = url.strip()
            path_landpage = "%s%s%s" % (u, '\\', url)
            path_2020 = "%s%s%s" % (u1, '\\', url)
            isExists_2020 = os.path.exists(path_2020)
            isExists_landpage = os.path.exists(path_landpage)
            href_landpage = os.walk(path_landpage)
            href_2020 = os.walk(path_2020)
            print(path_2020)
            if not isExists_landpage:
                if not isExists_2020:
                    os.makedirs(path_2020)
                    MyTest.addJs(self,u1, url)
                    QtWidgets.QMessageBox.about(self, '提示', "已在path_2020文件夹添加成功！")
                else:
                    for root, dirs, files in href_2020:
                        files.insert(0, 'lp_2020存在')
                        n = '\n'.join(files)
                        self.text.setPlainText(n)
            else:
                # # 链接存在landpage
                if not isExists_2020:
                    for root, dirs, files in href_landpage:
                        files.insert(0, 'landpage_存在,lp_2020不存在')
                        n = '\n'.join(files)
                        self.text.setPlainText(n)
                    os.makedirs(path_2020)
                    MyTest.addJs(self, u1, url)
                    QtWidgets.QMessageBox.about(self, '提示', "已在path_2020文件夹添加成功")
                else:
                    for root, dirs, files in href_2020:
                        files.insert(0, 'lp_2020存在')
                        n = '\n'.join(files)
                        self.text.setPlainText(n)
    def addJs(self, u1, url):
        value, ok = QInputDialog.getMultiLineText(self, "输入下载地址", "安卓\nios:", "android:\nios:")
        android = ''
        ios = ''
        href_data = [];
        if value and ok:
            data = value.split('\n')
            android = data[0]
            ios = data[1]
            if android == 'android:':
                android = ''
            if ios == 'ios:':
                ios = ''
            GEN_HTML = "%s%s%s%s%s" % (u1, '\\', url, '\\', 'down.js')
            # 打开文件，准备写入
            f = open(GEN_HTML, 'w')
            # 写入HTML界面中
            message = """var down_href={ios:%s%s%s,android:%s%s%s};""" % ("\"", ios, "\"", "\"", android, "\"")
            # 写入文件
            f.write(message)
    #--------------------------------------创建html
    def getHtml(self):
        comboText = self.comboText
        url = self.lineEdit.text()
        btn1_text = self.btn1.text()
        btn1_true = self.btn1.isChecked()
        btn2_text = self.btn1.text()
        btn2_true = self.btn1.isChecked()
        hrml_path = self.lineEdit_add_html.text()
        url = url.strip()
        hrml_path = hrml_path.strip()
        if hrml_path == ''  :
            return
        lp_2020 = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
        path_2020_html = "%s%s%s%s%s%s" % (lp_2020, '\\',url,'\\',hrml_path,'.html')
        # 判断新建文件是否存在
        is_true = os.access(path_2020_html, os.F_OK)

        if not is_true:
            banquan = '';
            if  self.radio_name == '智道未来':
                banquan = 'zhidaoweilai'
            elif self.radio_name == '智鸟':
                banquan = 'zhiniao'
            env = Environment(loader=FileSystemLoader('./'))
            imgData = self.lineEdit_add_img.toPlainText()
            new_data = "".join((re.sub("\n", " ", imgData)).split(" "))
            str_to_dict = eval(new_data)
            if comboText == '下载按钮悬浮':
                background_data = []
                button_data = []
                if str_to_dict['background'][0] == '图片地址':
                    return
                if str_to_dict['button'][0] == '按钮图片地址':
                    return
                for n in  str_to_dict['background']:
                    background_data.append(n)
                for k in str_to_dict['button']:
                    button_data.append(k)
                template = env.get_template('./html/demo1.html')
                img1 = background_data
                img2 = button_data
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan,img1=img1,img2=img2)
                    fout.write(html_content)
            elif comboText == '底部下载':
                background_data = []
                button_background = []
                button_button = []
                if str_to_dict['background'][0] == '图片地址':
                    return
                if str_to_dict['button_background'][0] == '按钮图片背景':
                    return
                if str_to_dict['button'][0] == '按钮图片按钮':
                    return
                for n in str_to_dict['background']:
                    background_data.append(n)
                for k in str_to_dict['button_background']:
                    button_background.append(k)
                for j in str_to_dict['button']:
                    button_button.append(j)
                template = env.get_template('./html/demo2.html')
                img1 = background_data
                img2 = button_background
                img3 = button_button
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, img1=img1, img2=img2,img3=img3)
                    fout.write(html_content)
            elif comboText == '不需要':
                template = env.get_template('./html/demo3.html')
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan)
                    fout.write(html_content)
            QtWidgets.QMessageBox.about(self, '提示', "创建成功")
            MyTest.muban(self,comboText)
        else:
            QtWidgets.QMessageBox.about(self, '提示', "文件已存在")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    demo = MyTest()
    demo.show()
    sys.exit(app.exec())