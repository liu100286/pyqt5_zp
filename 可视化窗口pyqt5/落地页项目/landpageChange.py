lp_2020_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import shutil
from natsort import natsorted
class get_landpageChane(object):
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
            if count == 2:
                newPage.append(self.tableWidget.item(rows_index, 1).text())
        filesData = [];
        k = 0;
        for root, dirs, files in href_2020_new:
            k = k + 1
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