lp_2020_path = 'C:\\Users\\Administrator\\Desktop\\lz_git\\\lp_2020'
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from natsort import natsorted
class get_landpageChange_move(object):
    # ----------------------落地页换户
    def landpageChane(self):
        oldLandpageUrl = self.lineEdit_5.text()
        newLandpageUrl = self.lineEdit_6.text()
        if oldLandpageUrl == '' or newLandpageUrl == '':
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
                    k = k + 1
                    if k == 1:
                        files = natsorted(files)
                        self.tableWidget_2.setRowCount(len(files))
                        for index, data in enumerate(files):
                            item = QtWidgets.QTableWidgetItem()
                            self.tableWidget_2.setItem(index, 0, item)
                            item = self.tableWidget_2.item(index, 0)
                            item.setText(_translate("Form", data))

        if isExists_2020_old:
            k = 0;
            for root, dirs, files in href_2020_old:
                k = k + 1
                if k == 1:
                    files = natsorted(files)
                    self.tableWidget.setRowCount(len(files))
                    for index, data in enumerate(files):
                        item = QtWidgets.QTableWidgetItem()
                        item.setCheckState(QtCore.Qt.Checked)
                        self.tableWidget.setItem(index, 0, item)
                        item = self.tableWidget.item(index, 0)

                        item = QtWidgets.QTableWidgetItem()
                        self.tableWidget.setItem(index, 1, item)
                        item = self.tableWidget.item(index, 1)
                        item.setText(_translate("Form", data))