# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_with_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QApplication

from Actions.Split_Images import Split_video_to_images
from GUI.Extract_Audio_Window import ExtractAudioWindow
from Actions.PlayVideo import *
from Actions.Delete_video import delete_video


class ActionButtonsWidget(QWidget):

    def __init__(self, video, parent=None):
        super(ActionButtonsWidget, self).__init__(parent)
        self.video = video
        # add your buttons
        layout = QHBoxLayout()

        # adjust spacings to your needs
        layout.setContentsMargins(3, 3, 3, 3)
        layout.setSpacing(5)

        # Create Buttons
        self.PlayVideo = QtWidgets.QPushButton('Play Video')
        self.Extract_Audio_btn = QtWidgets.QPushButton('Extract Audio')
        self.Split_btn = QtWidgets.QPushButton('Split to Images')
        self.Delete_btn = QtWidgets.QPushButton('Delete')
        self.PlayVideo.setStyleSheet("background-color: green;")
        self.Extract_Audio_btn.setStyleSheet("background-color: #1B1464;")
        self.Split_btn.setStyleSheet("background-color: #c23616")
        self.Delete_btn.setStyleSheet("background-color: red")
        self.PlayVideo.setToolTip("click to watch the Video")

        # add your buttons to the layout
        layout.addWidget(self.PlayVideo)
        layout.addWidget(self.Extract_Audio_btn)
        layout.addWidget(self.Split_btn)
        layout.addWidget(self.Delete_btn)

        self.setLayout(layout)
        # event listener
        self.PlayVideo.clicked.connect(lambda: PlayVideo(self.video.get_video_path()))
        self.Extract_Audio_btn.clicked.connect(lambda: self.OpenWindow(self.video))
        self.Split_btn.clicked.connect(lambda: Split_video_to_images(self.video))
        self.Delete_btn.clicked.connect(lambda: delete_video(self.video))

    def OpenWindow(self, video):
        self.window = QtWidgets.QMainWindow()
        self.window = ExtractAudioWindow(video)
        self.window.move(QApplication.desktop().screen().rect().center() - self.window.rect().center())
        self.window.show()