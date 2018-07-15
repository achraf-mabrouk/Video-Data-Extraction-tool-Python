# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_with_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget, QHBoxLayout


class CheckBoxWidget(QWidget):

    def __init__(self, video, parent=None):
        super(CheckBoxWidget, self).__init__(parent)
        self.video = video

        layout = QHBoxLayout()

        # adjust spacings to your needs
        layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(5)

        # Create checkBox
        self.CheckBox_select = QtWidgets.QCheckBox()
        self.CheckBox_select.setObjectName("row_CheckBox")

        # add your buttons to the layout
        layout.addWidget(self.CheckBox_select, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(layout)
        # event listener
