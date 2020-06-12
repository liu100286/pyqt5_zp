from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QInputDialog,QApplication
from natsort import natsorted
lp_2020_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
landpage_static_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\landpage_static'


class get_add_down_js(object):
    def getstr(self):
        url = self.lineEdit.text()
        if url=='':
            QtWidgets.QMessageBox.about(self, '提示', "请输入域名")
            return
        self.textEdit_3.setPlainText('')
        self.textEdit.setPlainText('')
        if url != '':
            url = url.strip()
            path_landpage = "%s%s%s" % (landpage_static_path, '\\', url)
            path_2020 = "%s%s%s" % (lp_2020_path, '\\', url)
            isExists_2020 = os.path.exists(path_2020)
            isExists_landpage = os.path.exists(path_landpage)
            href_landpage = os.walk(path_landpage)
            href_2020 = os.walk(path_2020)
            k_ = 0;
            for root, dirs, files in href_landpage:
                k_ = k_ + 1
                if k_ == 1:
                    files.insert(0, 'landpage_存在')
                    n = '\n'.join(files)
                    self.textEdit.setPlainText(n)
            if not isExists_landpage:
                if not isExists_2020:
                    get_add_down_js.addJs(self, lp_2020_path, url,path_2020)
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
                            self.textEdit_3.setPlainText(n)
            else:
                # # 链接存在landpage
                if not isExists_2020:
                    get_add_down_js.addJs(self, lp_2020_path, url,path_2020)
                else:
                    filesNewData = []
                    filesNewData_ = []
                    k=0
                    for root, dirs, files in href_2020:
                        k = k + 1
                        if k == 1:
                            filesNewData = files;
                            filesNewData_ = files;
                            p = ','.join(filesNewData)
                            self.lineEdit_3.setText(p)
                            filesNewData.insert(0, 'lp_2020存在')
                            n = '\n'.join(filesNewData)
                            self.textEdit_3.setPlainText(n)
    def copy_href(self):
        url = self.lineEdit.text()
        clipboard = QApplication.clipboard()
        clipboard.setText(url)
    def addJs(self, lp_2020_path, url,path_2020):
        value, ok = QInputDialog.getMultiLineText(self, "输入下载地址", "安卓\nios:", "android\nios")
        android = ''
        ios = ''
        href_data = [];
        if value and ok:
            os.makedirs(path_2020)
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
            get_add_down_js.getstr(self)
            QtWidgets.QMessageBox.about(self, '提示', "已在path_2020文件夹添加成功")
