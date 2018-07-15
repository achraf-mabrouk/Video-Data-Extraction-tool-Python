from PyQt5.QtWidgets import QWidget, QMessageBox


def critical_alert_window(windowTitle, AlertMessage):
    alert_window = QWidget()
    alert_window.resize(500, 250)
    alert_window.move(500, 150)
    QMessageBox.critical(alert_window, windowTitle, AlertMessage, QMessageBox.Ok)


def info_alert_window(windowTitle, AlertMessage):
    alert_window = QWidget()
    alert_window.resize(500, 250)
    alert_window.move(500, 150)
    QMessageBox.information(alert_window, windowTitle, AlertMessage, QMessageBox.Ok)


def warning_alert_window(windowTitle, AlertMessage):
    alert_window = QWidget()
    alert_window.resize(500, 250)
    alert_window.move(500, 150)
    QMessageBox.warning(alert_window, windowTitle, AlertMessage, QMessageBox.Ok)
