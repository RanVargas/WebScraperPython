# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/linux/Desktop/Python/Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(377, 128)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTriggerBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SearchTriggerBtn.setGeometry(QtCore.QRect(70, 30, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SearchTriggerBtn.setFont(font)
        self.SearchTriggerBtn.setObjectName("SearchTriggerBtn")
        self.DownloadedBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadedBtn.setGeometry(QtCore.QRect(200, 30, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DownloadedBtn.setFont(font)
        self.DownloadedBtn.setObjectName("DownloadedBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchTriggerBtn.setText(_translate("MainWindow", "Buscar"))
        self.DownloadedBtn.setText(_translate("MainWindow", "Descargados"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
