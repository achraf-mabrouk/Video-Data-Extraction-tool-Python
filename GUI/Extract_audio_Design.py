# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Extract_audio_Design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogExtract(object):
    def setupUi(self, DialogExtract):
        DialogExtract.setObjectName("DialogExtract")
        DialogExtract.resize(424, 201)
        DialogExtract.setStyleSheet(open("style.qss", "r").read())
        DialogExtract.setAutoFillBackground(True)
        self.Extract_btn = QtWidgets.QPushButton(DialogExtract)
        self.Extract_btn.setGeometry(QtCore.QRect(150, 130, 111, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Extract_btn.setFont(font)
        self.Extract_btn.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(DialogExtract)
        self.splitter.setGeometry(QtCore.QRect(50, 50, 291, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_format = QtWidgets.QComboBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_format.setFont(font)
        self.comboBox_format.setObjectName("comboBox_format")
        self.comboBox_format.addItem("")
        self.comboBox_format.addItem("")

        self.retranslateUi(DialogExtract)
        QtCore.QMetaObject.connectSlotsByName(DialogExtract)

    def retranslateUi(self, DialogExtract):
        _translate = QtCore.QCoreApplication.translate
        DialogExtract.setWindowTitle(_translate("DialogExtract", "Extract Audio"))
        self.Extract_btn.setText(_translate("DialogExtract", "Extract"))
        self.label.setText(_translate("DialogExtract", "Choose the audio format :"))
        self.comboBox_format.setItemText(0, _translate("DialogExtract", "MP3"))
        self.comboBox_format.setItemText(1, _translate("DialogExtract", "WAV"))
