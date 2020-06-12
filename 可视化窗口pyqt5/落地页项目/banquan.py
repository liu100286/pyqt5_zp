from PyQt5 import QtCore, QtGui, QtWidgets
import re
class get_banquan(object):
    def banquan_info(self,btn):
        url = self.lineEdit.text()
        url = url.strip()
        urlIndex = []
        self.zdwl = []
        comboText = self.comboText
        if url == '':
            return
        for m in re.finditer('\.', url):
            urlIndex.append(m.end())
        self.ej_ym = url[urlIndex[0]:urlIndex[1] - 1]
        if btn.text() == "智道未来":
            if btn.isChecked() == True:
                self.radio_name = '智道未来'
                self.zdwl = ['zdzhushou', 'zhidaozhushou', 'zhidzhushou']
                self.isZdzs = False;
                get_banquan.hedui(self)
        if btn.text() == "智鸟":
            if btn.isChecked() == True:
                self.radio_name = '智鸟'
                self.zdwl =  ['zhiniaotec']
                self.isZdzs = False;
                get_banquan.hedui(self)
        if btn.text() == "无版权":
            if btn.isChecked() == True:
                self.radio_name = '无版权'
                self.zdwl = [];
                self.isZdzs = True;
                get_banquan.hedui(self)
    def hedui(self):
        self.isZdzs = False;
        for s in self.zdwl:
            if s == self.ej_ym:
                self.isZdzs = True

        if not self.isZdzs:
            QtWidgets.QMessageBox.about(self, '提示', "核对版权")
    # ----------------------------------判断文件夹是否存在，创建文件夹