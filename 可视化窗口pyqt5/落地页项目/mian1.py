from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QRadioButton,QComboBox,QInputDialog
from jinja2 import Environment, FileSystemLoader
import re
import os
import json
from untitled import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets
import shutil
import os
from lxml import etree
from natsort import natsorted
lp_2020_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
landpage_static_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\landpage_static'
class MyMain(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.getstr)  # 查询输出
        self.radio_name = ''
        self.radioButton.toggled.connect(lambda: self.btnstate(self.radioButton))  # 单选按钮
        self.radioButton_2.toggled.connect(lambda: self.btnstate(self.radioButton_2))  #  单选按钮
        self.radioButton_3.toggled.connect(lambda: self.btnstate(self.radioButton_3))  #  单选按钮
        self.comboText = '下载按钮悬浮';
        self.comboBox.activated[str].connect(self.muban) #下拉菜单
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
          'zhezhao':0,
          }""")
        self.pushButton_5.clicked.connect(self.getHtml)  # 新建html
        self.pushButton_2.clicked.connect(self.settingHtml)  # 映射html
        self.iframe = False
        # 落地页项目迁移换户
        self.pushButton_4.clicked.connect(self.landpageChane)  # 查询输出
        self.pushButton_3.clicked.connect(self.newlandpageChane)  # 移动
        MyMain.iframe(self)
    def iframe(self):
        self.label_5.setVisible( self.iframe)
        self.lineEdit_4.setVisible( self.iframe)
    #     # ----------------------------------判断文件夹是否存在，创建文件夹
    def getstr(self):
        url = self.lineEdit.text()
        if url=='':
            QtWidgets.QMessageBox.about(self, '提示', "请输入域名")
            return
        self.textEdit.setPlainText('')
        if url != '':
            url = url.strip()
            path_landpage = "%s%s%s" % (landpage_static_path, '\\', url)
            path_2020 = "%s%s%s" % (lp_2020_path, '\\', url)
            isExists_2020 = os.path.exists(path_2020)
            isExists_landpage = os.path.exists(path_landpage)
            href_landpage = os.walk(path_landpage)
            href_2020 = os.walk(path_2020)
            if not isExists_landpage:
                if not isExists_2020:
                    os.makedirs(path_2020)
                    MyMain.addJs(self, lp_2020_path, url)
                    QtWidgets.QMessageBox.about(self, '提示', "已在path_2020文件夹添加成功！")
                else:
                    filesNewData = []
                    filesNewData_ = []
                    k = 0;
                    for root, dirs, files in href_2020:
                        k=k+1
                        if k == 1:
                            files = natsorted(files)
                            filesNewData = files;
                            filesNewData_ = files;
                            p = ','.join(filesNewData)
                            self.lineEdit_3.setText(p)
                            filesNewData.insert(0, 'lp_2020存在')
                            n = '\n'.join(filesNewData)
                            self.textEdit.setPlainText(n)
            else:
                # # 链接存在landpage
                if not isExists_2020:
                    k = 0;
                    for root, dirs, files in href_landpage:
                        k = k + 1
                        if k == 1:
                            files = natsorted(files)
                            files.insert(0, 'landpage_存在,lp_2020不存在')
                            n = '\n'.join(files)
                            self.textEdit.setPlainText(n)
                    os.makedirs(path_2020)
                    MyMain.addJs(self, lp_2020_path, url)
                    QtWidgets.QMessageBox.about(self, '提示', "已在path_2020文件夹添加成功")
                else:
                    filesNewData = []
                    filesNewData_ = []
                    k=0
                    for root, dirs, files in href_2020:
                        k = k + 1
                        if k == 1:
                            files = natsorted(files)
                            filesNewData = files;
                            filesNewData_ = files;
                            p = ','.join(filesNewData)
                            self.lineEdit_3.setText(p)
                            filesNewData.insert(0, 'lp_2020存在')
                            n = '\n'.join(filesNewData)
                            self.textEdit.setPlainText(n)
    def addJs(self, lp_2020_path, url):
        value, ok = QInputDialog.getMultiLineText(self, "输入下载地址", "安卓\nios:", "android\nios")
        android = ''
        ios = ''
        href_data = [];
        if value and ok:
            data = value.split('\n')
            android = data[0]
            ios = data[1]
            if android == 'android':
                android = ''
            if ios == 'ios':
                ios = ''
            GEN_HTML = "%s%s%s%s%s" % (lp_2020_path, '\\', url, '\\', 'down.js')
            # 打开文件，准备写入
            f = open(GEN_HTML, 'w')
            # 写入HTML界面中
            message = """var down_href={ios:%s%s%s,android:%s%s%s};""" % ("\"", ios, "\"", "\"", android, "\"")
            # 写入文件
            f.write(message)
    # radio
    def btnstate(self,btn):
        if btn.text() == "智道未来":
            if btn.isChecked() == True:
                self.radio_name = '智道未来'


        if btn.text() == "智鸟":
            if btn.isChecked() == True:
                self.radio_name = '智鸟'
        if btn.text() == "无版权":
            if btn.isChecked() == True:
                self.radio_name = '无版权'
    #   下拉
    def muban(self, text):
        self.iframe = False

        self.comboText = text;
        if text == '下载按钮悬浮':
            self.textEdit_2.setVisible(True)
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
              'zhezhao':0,
               }""")
        elif text == '底部下载':
            self.textEdit_2.setPlainText("""{
              "background":[
               "图片地址",
              ],
             "button_background":[
               "按钮图片背景"
              ],
              "button":[
               "按钮图片按钮"
              ],
               "no_xuanfu":[
                "按钮不悬浮图片地址"
              ],
                'zhezhao':0,
             }""")
        elif text == '不需要':
            self.textEdit_2.setPlainText('')
        elif text == '动态落地页模板':
            self.textEdit_2.setPlainText('')
        elif text == 'iframe':
            self.textEdit_2.setPlainText('')
            self.iframe = True
        elif text == '整屏幕横向轮播':
            self.textEdit_2.setPlainText("""{
              "background":[
               "轮播图片",
              ],
             "button_background":[
               "按钮图片背景"
              ],
              "button":[
               "按钮图片按钮"
              ]
             }""")

        # MyMain.iframe(self)
        self.iframe_(self)
    #     选择 按钮类型
    def button_type(self,text):
        self.buttonType = text;
    # -----------------------------------映射html
    def settingHtml(self):
        comboText = self.comboText
        muban_html = 'lp1.html'
        button_data = []
        no_xuanfu = [];
        background_data=[]
        mb_num = []
        button_background=[];
        button_button=[];
        env = Environment(loader=FileSystemLoader('./'))
        if comboText == '':
            QtWidgets.QMessageBox.about(self, '提示', "请输入文件名称")
            return
        imgData = self.textEdit_2.toPlainText()
        if imgData != '':
            new_data = "".join((re.sub("\n", " ", imgData)).split(" "))
            str_to_dict = eval(new_data)
        if comboText == '下载按钮悬浮':
            if str_to_dict['background'][0] == '图片地址':
                return
            for n in str_to_dict['background']:
                background_data.append(n)
            obj = {}
            no_obj = {}
            mb_obj = {}
            for k in str_to_dict['xuanfu']:
                if k != '按钮悬浮图片地址':
                    obj = {
                        'name': 'xuanfu',
                        'img': k
                    }
                    button_data.append(obj)
            for j in str_to_dict['no_xuanfu']:
                if j != '按钮不悬浮图片地址':
                    no_obj = {
                        'name': 'no_xuanfu',
                        'img': j
                    }
                    no_xuanfu.append(no_obj)
            for z in range(str_to_dict['zhezhao']):
                mb_obj = {
                    'name': 'zhezhao',
                    'img': ''
                }
                mb_num.append(mb_obj)
            newButon = [];
            newButon.extend(button_data)
            newButon.extend(no_xuanfu)
            newButon.extend(mb_num)
            template = env.get_template('./muban/lp1.html')
            img1 = background_data
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(img1=img1, newButon=newButon)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        elif  comboText == '底部下载':
            if str_to_dict['background'][0] == '图片地址':
                return
            obj = {}
            no_obj = {}
            mb_obj = {}
            for n in str_to_dict['background']:
                background_data.append(n)
            for k in str_to_dict['button_background']:
                button_background.append(k)
            for j in str_to_dict['button']:
                button_button.append(j)
            for f in str_to_dict['no_xuanfu']:
                if f != '按钮不悬浮图片地址':
                    no_obj = {
                        'name': 'no_xuanfu',
                        'img': f
                    }
                    no_xuanfu.append(no_obj)
            for z in range(str_to_dict['zhezhao']):
                mb_obj = {
                    'name': 'zhezhao',
                    'img': ''
                }
                mb_num.append(mb_obj)
            newButon = [];
            newButon.extend(no_xuanfu)
            newButon.extend(mb_num)
            template = env.get_template('./muban/lp2.html')
            img1 = background_data
            with open(muban_html, 'w+', encoding="utf-8") as fout:
                html_content = template.render(img1=img1, newButon=newButon,button_background=button_background,button_button=button_button)
                fout.write(html_content)
            f = open("lp1.html", "r", encoding="utf-8")  # 读取文件
        f = f.read()
        self.browser.setHtml(f)
    #--------------------------------------创建html
    def getHtml(self):
        comboText = self.comboText
        if comboText == '':
            QtWidgets.QMessageBox.about(self, '提示', "请输入文件名称")
            return
        url = self.lineEdit.text()
        btn1_text = self.radioButton.text()
        btn1_true = self.radioButton.isChecked()
        btn2_text = self.radioButton_2.text()
        btn2_true = self.radioButton_2.isChecked()
        hrml_path = self.lineEdit_2.text()
        url = url.strip()
        hrml_path = hrml_path.strip()
        if hrml_path == '':
            return
        buttonType = self.buttonType
        path_2020_html = "%s%s%s%s%s%s" % (lp_2020_path, '\\',url,'\\',hrml_path,'.html')
        # 判断问价是否存在老的落地页
        path_landpage_html = "%s%s%s%s%s%s" % (landpage_static_path, '\\', url, '\\', hrml_path, '.html')
        is_landpage_true = os.access(path_landpage_html, os.F_OK)
        buttonCss = ''
        if buttonType != '无':
            hrefCss = "%s%s%s" % ('./html/',buttonType,'.css',)
            with open(hrefCss, 'r') as f:
                buttonCss = f.read()
        if   is_landpage_true:
            QtWidgets.QMessageBox.about(self, '提示', "新建改文件已在老落地页项目中存在")
            return
        # 判断新建文件是否存在
        is_true = os.access(path_2020_html, os.F_OK)
        if not is_true:
            banquan = '';
            if  self.radio_name == '':
                QtWidgets.QMessageBox.about(self, '提示', "请选择版权")
                return
            elif  self.radio_name == '智道未来':
                banquan = 'zhidaoweilai'
            elif self.radio_name == '智鸟':
                banquan = 'zhiniao'
            elif self.radio_name == '无版权':
                banquan = '无版权'
            env = Environment(loader=FileSystemLoader('./'))
            background_data = []
            button_background = []
            button_button = []
            button_info = []
            with open('indor.txt', 'r') as f:
                button_info = json.loads(f.read())
            imgData = self.textEdit_2.toPlainText()
            if imgData !='':
                new_data = "".join((re.sub("\n", " ", imgData)).split(" "))
                str_to_dict = eval(new_data)
            if comboText == '下载按钮悬浮':
                if str_to_dict['background'][0] == '图片地址':
                    return

                for n in  str_to_dict['background']:
                    background_data.append(n)

                template = env.get_template('./html/demo1.html')
                img1 = background_data


                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan,img1=img1,button_info=button_info,buttonCss=buttonCss)
                    fout.write(html_content)
                # self.browser.setHtml('')
            elif comboText == '底部下载':
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
                    html_content = template.render(banquan=banquan, img1=img1, img2=img2,img3=img3,button_info=button_info)
                    fout.write(html_content)
            elif comboText == '不需要':
                template = env.get_template('./html/demo3.html')
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan)
                    fout.write(html_content)
            elif comboText == '动态落地页模板':
                template = env.get_template('./html/demo4.html')
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan)
                    fout.write(html_content)
            elif comboText == 'iframe':
                template = env.get_template('./html/demo5.html')
                iframeUrl = self.lineEdit_4.text()
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan,iframeUrl=iframeUrl)
                    fout.write(html_content)
            elif comboText == '整屏幕横向轮播':
                if str_to_dict['background'][0] == '轮播图片':
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
                template = env.get_template('./html/demo6.html')
                img1 = background_data
                img2 = button_background
                img3 = button_button
                with open(path_2020_html, 'w+', encoding="utf-8") as fout:
                    html_content = template.render(banquan=banquan, img1=img1, img2=img2,img3=img3)
                    fout.write(html_content)
            QtWidgets.QMessageBox.about(self, '提示', "创建成功")
            MyMain.muban(self,comboText)
        else:
            QtWidgets.QMessageBox.about(self, '提示', "文件已存在")
    #----------------------落地页换户
    def landpageChane(self):
        oldLandpageUrl = self.lineEdit_5.text()
        newLandpageUrl = self.lineEdit_6.text()
        if oldLandpageUrl==''or newLandpageUrl=='':
            QtWidgets.QMessageBox.about(self, '提示', "请先输入域名")
            return
        path_2020_old = "%s%s%s" % (lp_2020_path, '\\', oldLandpageUrl)
        path_2020_new = "%s%s%s" % (lp_2020_path, '\\', newLandpageUrl)
        isExists_2020_old = os.path.exists(path_2020_old)
        isExists_2020_new = os.path.exists(path_2020_new)
        href_2020_old = os.walk(path_2020_old)
        href_2020_new = os.walk(path_2020_new)
        _translate = QtCore.QCoreApplication.translate
        if newLandpageUrl != '':
            if not isExists_2020_new:
                QtWidgets.QMessageBox.about(self, '提示', "请先新建文件夹")
            else:
                k = 0
                for root, dirs, files in href_2020_new:
                    k=k+1
                    if k==1:
                        files = natsorted(files)
                        self.tableWidget_2.setRowCount(len(files))
                        for index, data in enumerate(files):
                            item = QtWidgets.QTableWidgetItem()
                            self.tableWidget_2.setItem(index, 0, item)
                            item = self.tableWidget_2.item(index, 0)
                            item.setText(_translate("Form", data))

        if  isExists_2020_old:
            k = 0;
            for root, dirs, files in href_2020_old:
                k = k+1
                if k == 1:
                    files = natsorted(files)
                    self.tableWidget.setRowCount(len(files))
                    for index,data in enumerate(files):
                        item = QtWidgets.QTableWidgetItem()
                        item.setCheckState(QtCore.Qt.Checked)
                        self.tableWidget.setItem(index, 0, item)
                        item = self.tableWidget.item(index, 0)
                        item = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(index, 1, item)
                        item = self.tableWidget.item(index, 1)
                        item.setText(_translate("Form", data))

    def newlandpageChane(self):
        newLandpageUrl = self.lineEdit_6.text()
        path_2020_new = "%s%s%s" % (lp_2020_path, '\\', newLandpageUrl)
        href_2020_new = os.walk(path_2020_new)

        newPage = []
        newHref = self.lineEdit_6.text()
        if newHref == '':
            QtWidgets.QMessageBox.about(self, '提示', "请输入域名")
            return
        oldHref = self.lineEdit_5.text()
        rows = self.tableWidget.rowCount()
        for rows_index in range(rows):
            count = self.tableWidget.item(rows_index, 0).checkState()
            if count==2:
                newPage.append( self.tableWidget.item(rows_index, 1).text())
        filesData = [];
        k = 0;
        for root, dirs, files in href_2020_new:
            k=k+1
            if k == 1:
                files = natsorted(files)
                filesData = files

        for data in newPage:
            file = "%s%s%s%s%s" % (lp_2020_path, '\\', oldHref, '\\', data)
            new_path = "%s%s%s" % (lp_2020_path, '\\', newHref)
            if len(filesData) == 0:
                shutil.copy(file, new_path)
            else:
                for item in filesData:
                    if data == item:
                        QtWidgets.QMessageBox.about(self, '提示', "有重复文件")
                        return
                    else:
                        shutil.copy(file, new_path)
        QtWidgets.QMessageBox.about(self, '提示', "添加成功")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    A1 = MyMain()
    A1.show()
    sys.exit(app.exec_())
#
# self.browser = QWebEngineView()
# self.browser.setObjectName("browser")
# self.verticalLayout.addWidget(self.browser)