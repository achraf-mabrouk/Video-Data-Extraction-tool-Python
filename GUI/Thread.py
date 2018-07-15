from PyQt5.QtCore import QThread


class SplitImagesThread(QThread):

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        print("Thread is running...")