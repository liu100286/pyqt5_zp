# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableView_test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
import datetime
class Ui_dataBaseForm(object):
    def setupUi(self, dataBaseForm):
        dataBaseForm.setObjectName("dataBaseForm")
        dataBaseForm.resize(1127, 754)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        dataBaseForm.setFont(font)
        dataBaseForm.setAutoFillBackground(False)
        self.groupBox = QtWidgets.QGroupBox(dataBaseForm)
        self.groupBox.setGeometry(QtCore.QRect(870, 80, 231, 141))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 211, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.db_create = QtWidgets.QPushButton(self.layoutWidget)
        self.db_create.setObjectName("db_create")
        self.gridLayout.addWidget(self.db_create, 0, 1, 1, 1)
        self.db_delete_edit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.db_delete_edit.setFont(font)
        self.db_delete_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.db_delete_edit.setStyleSheet("")
        self.db_delete_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.db_delete_edit.setObjectName("db_delete_edit")
        self.gridLayout.addWidget(self.db_delete_edit, 1, 0, 1, 1)
        self.db_delete = QtWidgets.QPushButton(self.layoutWidget)
        self.db_delete.setObjectName("db_delete")
        self.gridLayout.addWidget(self.db_delete, 1, 1, 1, 1)
        self.db_create_edit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.db_create_edit.setFont(font)
        self.db_create_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.db_create_edit.setStyleSheet("")
        self.db_create_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.db_create_edit.setObjectName("db_create_edit")
        self.gridLayout.addWidget(self.db_create_edit, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(dataBaseForm)
        self.groupBox_2.setGeometry(QtCore.QRect(870, 270, 231, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 211, 141))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.A_title_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.A_title_3.setFont(font)
        self.A_title_3.setObjectName("A_title_3")
        self.gridLayout_2.addWidget(self.A_title_3, 3, 0, 1, 1)
        self.date_select = QtWidgets.QPushButton(self.layoutWidget1)
        self.date_select.setObjectName("date_select")
        self.gridLayout_2.addWidget(self.date_select, 5, 0, 1, 1)
        self.A_title_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.A_title_2.setFont(font)
        self.A_title_2.setObjectName("A_title_2")
        self.gridLayout_2.addWidget(self.A_title_2, 0, 0, 1, 1)
        self.date_start = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_start.setFont(font)
        year = int(datetime.datetime.now().strftime('%Y'))
        month = int(datetime.datetime.now().strftime('%m'))
        day_ = int(datetime.datetime.now().strftime('%d'))
        self.date_start.setDate(QDate.currentDate())
        self.date_start.setCalendarPopup(True)
        self.date_start.setObjectName("date_start")
        self.gridLayout_2.addWidget(self.date_start, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)

        self.groupBox_3 = QtWidgets.QGroupBox(dataBaseForm)
        self.groupBox_3.setGeometry(QtCore.QRect(870, 450, 231, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 211, 111))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.db_print = QtWidgets.QPushButton(self.layoutWidget2)
        self.db_print.setObjectName("db_print")
        self.gridLayout_3.addWidget(self.db_print, 1, 0, 1, 1)
        self.db_export = QtWidgets.QPushButton(self.layoutWidget2)
        self.db_export.setObjectName("db_export")
        self.gridLayout_3.addWidget(self.db_export, 0, 0, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(dataBaseForm)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 630, 851, 33))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.A_title = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.A_title.setFont(font)
        self.A_title.setObjectName("A_title")
        self.horizontalLayout_2.addWidget(self.A_title)
        self.db_writ = QtWidgets.QLineEdit(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.db_writ.setFont(font)
        self.db_writ.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.db_writ.setStyleSheet("")
        self.db_writ.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.db_writ.setObjectName("db_writ")
        self.horizontalLayout_2.addWidget(self.db_writ)
        self.db_insert = QtWidgets.QPushButton(self.layoutWidget3)
        self.db_insert.setObjectName("db_insert")
        self.horizontalLayout_2.addWidget(self.db_insert)
        self.db_delete_row = QtWidgets.QPushButton(self.layoutWidget3)
        self.db_delete_row.setObjectName("db_delete_row")
        self.horizontalLayout_2.addWidget(self.db_delete_row)
        self.dataView = QtWidgets.QTableWidget(dataBaseForm)
        self.dataView.setGeometry(QtCore.QRect(10, 80, 851, 541))
        self.dataView.setObjectName("dataView")
        #self.dataView.setColumnCount(0)
        #self.dataView.setRowCount(0)

        self.retranslateUi(dataBaseForm)
        QtCore.QMetaObject.connectSlotsByName(dataBaseForm)

    def retranslateUi(self, dataBaseForm):
        _translate = QtCore.QCoreApplication.translate
        dataBaseForm.setWindowTitle(_translate("dataBaseForm", "TableView数据库视图-liangfu"))
        self.groupBox.setTitle(_translate("dataBaseForm", "基本操作"))
        self.db_create.setText(_translate("dataBaseForm", "创建表格"))
        self.db_delete_edit.setText(_translate("dataBaseForm", "dataBase"))
        self.db_delete.setText(_translate("dataBaseForm", "删除表格"))
        self.db_create_edit.setText(_translate("dataBaseForm", "dataBase"))
        self.groupBox_2.setTitle(_translate("dataBaseForm", "查找数据"))
        self.date_select.setText(_translate("dataBaseForm", "查询"))
        self.A_title_2.setText(_translate("dataBaseForm", "查询时间："))
        self.date_start.setDisplayFormat(_translate("dataBaseForm", "yyyy-MM-dd"))
        self.groupBox_3.setTitle(_translate("dataBaseForm", "导出保存"))
        self.db_print.setText(_translate("dataBaseForm", "打印"))
        self.db_export.setText(_translate("dataBaseForm", "导出为Excel文档"))
        self.A_title.setText(_translate("dataBaseForm", "输入数值（空格隔开）："))
        self.db_writ.setText(_translate("dataBaseForm", "0.1023 0.1233 0.1214"))
        self.db_insert.setText(_translate("dataBaseForm", "插入一行"))
        self.db_delete_row.setText(_translate("dataBaseForm", "删除一行"))