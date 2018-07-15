from Actions.Extract_audio import Extract_Audio
from GUI.Extract_audio_Design import *


class ExtractAudioWindow(QtWidgets.QMainWindow, Ui_DialogExtract):
    def __init__(self, video):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.video = video
        self.Extract_btn.setStyleSheet("background-color: green;")
        self.Extract_btn.clicked.connect(lambda: self.Extract_Action())

    def Extract_Action(self):
        Extract_Audio(self.video, self.comboBox_format.currentText())
        self.close()
