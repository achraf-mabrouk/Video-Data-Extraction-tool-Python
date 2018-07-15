# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadMenu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DownloadWindow(object):

    def setupUi(self, DownloadWindow):
        DownloadWindow.setObjectName("DownloadWindow")
        DownloadWindow.resize(1215, 584)
        self.tableWidget_downloaded_list = QtWidgets.QTableWidget(DownloadWindow)
        DownloadWindow.setStyleSheet(open("style.qss", "r").read())
        DownloadWindow.setAutoFillBackground(True)
        self.tableWidget_downloaded_list.setGeometry(QtCore.QRect(35, 150, 1146, 341))
        self.tableWidget_downloaded_list.setRowCount(10)
        self.tableWidget_downloaded_list.setColumnCount(4)
        self.tableWidget_downloaded_list.setObjectName("tableWidget_downloaded_list")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_downloaded_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_downloaded_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_downloaded_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_downloaded_list.setHorizontalHeaderItem(3, item)
        self.tableWidget_downloaded_list.resizeColumnsToContents()
        self.tableWidget_downloaded_list.horizontalHeader().setDefaultSectionSize(230)
        self.tableWidget_downloaded_list.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget_downloaded_list.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_downloaded_list.horizontalHeader().setStretchLastSection(True)
        self.Title = QtWidgets.QLabel(DownloadWindow)
        self.Title.setGeometry(QtCore.QRect(435, 35, 340, 31))
        font = QtGui.QFont()
        font.setFamily("gargi")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Choose = QtWidgets.QLabel(DownloadWindow)
        self.Choose.setGeometry(QtCore.QRect(90, 110, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Choose.setFont(font)
        self.Choose.setObjectName("Choose")
        self.retranslateUi(DownloadWindow)
        QtCore.QMetaObject.connectSlotsByName(DownloadWindow)

    def retranslateUi(self, DownloadWindow):
        _translate = QtCore.QCoreApplication.translate
        DownloadWindow.setWindowTitle(_translate("DownloadWindow", "Downloaded video List"))
        item = self.tableWidget_downloaded_list.horizontalHeaderItem(0)
        item.setText(_translate("DownloadWindow", "Search Keywords"))
        item = self.tableWidget_downloaded_list.horizontalHeaderItem(1)
        item.setText(_translate("DownloadWindow", "Title"))
        item = self.tableWidget_downloaded_list.horizontalHeaderItem(2)
        item.setText(_translate("DownloadWindow", "Link"))
        item = self.tableWidget_downloaded_list.horizontalHeaderItem(3)
        item.setText(_translate("DownloadWindow", "Action"))
        self.Title.setText(_translate("DownloadWindow", "List of Downloaded Videos"))
        self.Choose.setText(_translate("DownloadWindow", "Choose Action :"))
        self.Title.setStyleSheet("color : #0097e6;")
