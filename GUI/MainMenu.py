import urllib

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

import GUI.MainMenuDesign as Design
from Download_Process import *
from GUI.Downloaded_List import Downloaded_List
import SearchAPIs.Bing_Search_API as bing
import SearchAPIs.Google_Search_API as google
from Filter_Process.Filter import *
from GUI.Alert_window import *


def check_connectivity():
    # we need an ip address of the server not a Domain name to avoid DNS Resolution
    # because When the machine does not have a working internet connection,
    # the DNS lookup itself may block the call to urllib_request.urlopen for more than a second
    try:
        # this is a google ip address
        urllib.request.urlopen("http://216.58.205.174", timeout=1)

        return True
    except urllib.request.URLError:
        return False


class MainMenuApp(QtWidgets.QMainWindow, Design.Ui_mainMenuWidget):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in MainMenuDesign.py file automatically
        self.search_results = []
        # create Listener
        self.search_btn.clicked.connect(lambda: self.Search_Process())
        self.youtube_checkBox.stateChanged.connect(lambda: self.youtube_only())
        self.dailymotion_checkBox.stateChanged.connect(lambda: self.dailymotion_only())
        self.DownloadAll_btn.clicked.connect(lambda: download_all_videos(self.search_results))
        self.ShowDownloadedVideos_btn.clicked.connect(lambda: self.OpenWindow())
        self.DownloadSelected_btn.clicked.connect(lambda: self.download_selection())
        # Enter key pressed Listener for search
        self.keyword_input.returnPressed.connect(lambda: self.search_btn.click())

    def loadData(self):
        self.tableWidget.setRowCount(0)
        row_number = 0
        for link in self.search_results:
            self.tableWidget.insertRow(row_number)
            # self.tableWidget.setCellWidget(row_number, 0, CheckBoxWidget(link))
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(link.get_title()))
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(link.get_link()))
            row_number += 1

    def Search_Process(self):
        search_keyword = self.keyword_input.text()
        if search_keyword:
            if check_connectivity():
                self.search_results = bing.search(search_keyword)
                self.search_results += google.search(search_keyword)
                self.search_results = remove_duplications(remove_none_videos_links(self.search_results))
                self.loadData()
            else:
                # alert window if connection is failed
                critical_alert_window("Connection Problem", "Connection Failed, please Check your network connection !")
        else:
            # alert window if the search_keyword is empty
            critical_alert_window("Search Bar is empty", "Please Enter the Search Keywords !")

    def youtube_only(self):
        if self.search_results:
            if self.youtube_checkBox.isChecked():
                row_number = 0
                self.tableWidget.setRowCount(0)
                for link in self.search_results:
                    if "youtube.com" in link.get_link():
                        self.tableWidget.insertRow(row_number)
                        self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(link.get_title()))
                        self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(link.get_link()))
                        row_number += 1
            else:
                self.loadData()

    def dailymotion_only(self):
        if self.search_results:
            if self.dailymotion_checkBox.isChecked():
                row_number = 0
                self.tableWidget.setRowCount(0)
                for link in self.search_results:
                    if "dailymotion.com" in link.get_link():
                        self.tableWidget.insertRow(row_number)
                        self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(link.get_title()))
                        self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(link.get_link()))
                        row_number += 1
            else:
                self.loadData()

    def OpenWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.window = Downloaded_List()
        self.window.move(QApplication.desktop().screen().rect().center() - self.window.rect().center())
        self.window.show()

    def download_selection(self):
        selected_List = []
        if self.search_results:
            for row in self.tableWidget.selectedItems():
                selected_List.append(self.search_results[row.row()])

            info_alert_window("Download information", "download may take a few minutes or hours!")
            download_all_videos(selected_List)


def main():
    app = QtWidgets.QApplication(sys.argv)
    menu = MainMenuApp()
    menu.move(QApplication.desktop().screen().rect().center() - menu.rect().center())
    menu.show()
    app.exec_()


if __name__ == '__main__':
    main()
