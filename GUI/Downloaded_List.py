import sys
from PyQt5.QtWidgets import QApplication
import GUI.downloaded_ListDesign as Design
from PyQt5 import QtWidgets
from Database.DbAccess import DBConnection
from GUI.ActionButtonsWidget import ActionButtonsWidget


class Downloaded_List(QtWidgets.QMainWindow, Design.Ui_DownloadWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in MainMenuDesign.py file automatically
        # Load Data from the Database
        self.LoadData()

    def LoadData(self):
        conn = DBConnection()
        results = conn.get_all_videos()

        self.tableWidget_downloaded_list.setRowCount(0)
        row_number = 0
        for video in results:
            # Insert Row
            self.tableWidget_downloaded_list.insertRow(row_number)
            self.tableWidget_downloaded_list.setItem(row_number, 0,
                                                     QtWidgets.QTableWidgetItem(video.get_search_keywords()))
            self.tableWidget_downloaded_list.setItem(row_number, 1, QtWidgets.QTableWidgetItem(video.get_title()))
            self.tableWidget_downloaded_list.setItem(row_number, 2, QtWidgets.QTableWidgetItem(video.get_link()))
            self.tableWidget_downloaded_list.setCellWidget(row_number, 3, ActionButtonsWidget(video))
            row_number += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    menu = Downloaded_List()
    menu.move(QApplication.desktop().screen().rect().center() - menu.rect().center())
    menu.show()
    app.exec_()


if __name__ == '__main__':
    main()
