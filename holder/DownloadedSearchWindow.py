# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/linux/Desktop/Python/DownloadedSearchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_DownloadedWindow(object):
    def setupUi(self, DownloadedWindow):
        DownloadedWindow.setObjectName("DownloadedWindow")
        DownloadedWindow.resize(630, 514)
        self.centralwidget = QtWidgets.QWidget(DownloadedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DownloadedArticlesListView = QtWidgets.QListView(self.centralwidget)
        self.DownloadedArticlesListView.setGeometry(QtCore.QRect(10, 20, 521, 461))
        self.DownloadedArticlesListView.setObjectName("DownloadedArticlesListView")
        self.OpenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OpenBtn.setGeometry(QtCore.QRect(540, 160, 80, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OpenBtn.setFont(font)
        self.OpenBtn.setObjectName("OpenBtn")
        self.DeleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBtn.setGeometry(QtCore.QRect(540, 280, 80, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteBtn.setFont(font)
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.GoBackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn.setGeometry(QtCore.QRect(540, 442, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GoBackBtn.setFont(font)
        self.GoBackBtn.setObjectName("GoBackBtn")
        DownloadedWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DownloadedWindow)
        self.statusbar.setObjectName("statusbar")
        DownloadedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DownloadedWindow)
        QtCore.QMetaObject.connectSlotsByName(DownloadedWindow)

    def retranslateUi(self, DownloadedWindow):
        _translate = QtCore.QCoreApplication.translate
        DownloadedWindow.setWindowTitle(_translate("DownloadedWindow", "MainWindow"))
        self.OpenBtn.setText(_translate("DownloadedWindow", "Abrir"))
        self.DeleteBtn.setText(_translate("DownloadedWindow", "Borrar"))
        self.GoBackBtn.setText(_translate("DownloadedWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadedWindow = QtWidgets.QMainWindow()
    ui = Ui_DownloadedWindow()
    ui.setupUi(DownloadedWindow)
    DownloadedWindow.show()
    sys.exit(app.exec_())
