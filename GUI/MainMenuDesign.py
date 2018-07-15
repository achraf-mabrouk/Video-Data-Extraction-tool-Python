# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainMenuWidget(object):

    def setupUi(self, mainMenuWidget):
        mainMenuWidget.setObjectName("mainMenuWidget")
        mainMenuWidget.resize(915, 650)
        mainMenuWidget.setStyleSheet(open("style.qss", "r").read())
        mainMenuWidget.setAutoFillBackground(True)
        mainMenuWidget.setWindowIcon(QtGui.QIcon("mining.png"))
    # buttons
        self.search_btn = QtWidgets.QPushButton(mainMenuWidget)
        self.search_btn.setGeometry(QtCore.QRect(360, 50, 201, 41))
        self.search_btn.setObjectName("search_btn")
        self.DownloadAll_btn = QtWidgets.QPushButton(mainMenuWidget)
        self.DownloadAll_btn.setGeometry(QtCore.QRect(230, 550, 201, 41))
        self.DownloadAll_btn.setObjectName("DownloadAll_btn")
        self.DownloadSelected_btn = QtWidgets.QPushButton(mainMenuWidget)
        self.DownloadSelected_btn.setGeometry(QtCore.QRect(456, 550, 201, 41))
        self.DownloadSelected_btn.setObjectName("DownloadAll_btn")
        self.ShowDownloadedVideos_btn = QtWidgets.QPushButton(mainMenuWidget)
        self.ShowDownloadedVideos_btn.setGeometry(QtCore.QRect(670, 50, 201, 41))
        self.ShowDownloadedVideos_btn.setObjectName("ShowDownloadedVideos_btn")

        # table
        self.tableWidget = QtWidgets.QTableWidget(mainMenuWidget)
        self.tableWidget.setGeometry(QtCore.QRect(66, 170, 782, 351))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(379)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(34)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        # Input
        self.keyword_input = QtWidgets.QLineEdit(mainMenuWidget)
        self.keyword_input.setGeometry(QtCore.QRect(85, 50, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setKerning(True)
        self.keyword_input.setFont(font)
        self.keyword_input.setObjectName("keyword_input")
        self.splitter = QtWidgets.QSplitter(mainMenuWidget)
        self.splitter.setGeometry(QtCore.QRect(90, 110, 370, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        # label
        self.Filter_label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Filter_label.setFont(font)
        self.Filter_label.setObjectName("Filter_label")
        self.youtube_checkBox = QtWidgets.QCheckBox(self.splitter)
        self.youtube_checkBox.setObjectName("youtube_checkBox")
        self.dailymotion_checkBox = QtWidgets.QCheckBox(self.splitter)
        self.dailymotion_checkBox.setObjectName("dailymotion_checkBox")
        self.retranslateUi(mainMenuWidget)
        QtCore.QMetaObject.connectSlotsByName(mainMenuWidget)

    def retranslateUi(self, mainMenuWidget):
        _translate = QtCore.QCoreApplication.translate
        mainMenuWidget.setWindowTitle(_translate("mainMenuWidget", "Video Content Mining"))
        self.search_btn.setText(_translate("mainMenuWidget", "Search"))
        self.DownloadAll_btn.setText(_translate("mainMenuWidget", "Download All"))
        self.DownloadSelected_btn.setText(_translate("mainMenuWidget", "Download Selection"))
        self.ShowDownloadedVideos_btn.setText(_translate("mainMenuWidget", "Show Downloaded List"))
        # item = self.tableWidget.horizontalHeaderItem(0)
        # item.setText(_translate("mainMenuWidget", "Select"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainMenuWidget", "Titles"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainMenuWidget", "Links"))
        self.keyword_input.setPlaceholderText(_translate("mainMenuWidget", "Search"))
        self.Filter_label.setText(_translate("mainMenuWidget", "Filter search results :"))
        self.youtube_checkBox.setText(_translate("mainMenuWidget", "Youtube"))
        self.dailymotion_checkBox.setText(_translate("mainMenuWidget", "Dailymotion"))
