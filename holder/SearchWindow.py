# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/linux/Desktop/Python/SearchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ElHoyLabel = QtWidgets.QRadioButton(self.centralwidget)
        self.ElHoyLabel.setGeometry(QtCore.QRect(50, 60, 100, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ElHoyLabel.setFont(font)
        self.ElHoyLabel.setObjectName("ElHoyLabel")
        self.DiarioLibreLabel = QtWidgets.QRadioButton(self.centralwidget)
        self.DiarioLibreLabel.setGeometry(QtCore.QRect(50, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DiarioLibreLabel.setFont(font)
        self.DiarioLibreLabel.setObjectName("DiarioLibreLabel")
        self.ListinDiarioLabel = QtWidgets.QRadioButton(self.centralwidget)
        self.ListinDiarioLabel.setGeometry(QtCore.QRect(50, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ListinDiarioLabel.setFont(font)
        self.ListinDiarioLabel.setObjectName("ListinDiarioLabel")
        self.CategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.CategoryComboBox.setGeometry(QtCore.QRect(210, 50, 121, 23))
        self.CategoryComboBox.setObjectName("CategoryComboBox")
        self.PeriodicoLabel = QtWidgets.QLabel(self.centralwidget)
        self.PeriodicoLabel.setGeometry(QtCore.QRect(50, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.PeriodicoLabel.setFont(font)
        self.PeriodicoLabel.setObjectName("PeriodicoLabel")
        self.CategoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.CategoryLabel.setGeometry(QtCore.QRect(210, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.CategoryLabel.setFont(font)
        self.CategoryLabel.setObjectName("CategoryLabel")
        self.ResultOfSearchListBox = QtWidgets.QListWidget(self.centralwidget)
        self.ResultOfSearchListBox.setGeometry(QtCore.QRect(5, 160, 461, 391))
        self.ResultOfSearchListBox.setObjectName("ResultOfSearchListBox")
        self.SearchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SearchBtn.setGeometry(QtCore.QRect(180, 120, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SearchBtn.setFont(font)
        self.SearchBtn.setObjectName("SearchBtn")
        self.DownloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadBtn.setGeometry(QtCore.QRect(180, 560, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DownloadBtn.setFont(font)
        self.DownloadBtn.setObjectName("DownloadBtn")
        self.GoBackBtn = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn.setGeometry(QtCore.QRect(380, 570, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.GoBackBtn.setFont(font)
        self.GoBackBtn.setObjectName("GoBackBtn")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.ElHoyLabel.setText(_translate("SearchWindow", "El Hoy"))
        self.DiarioLibreLabel.setText(_translate("SearchWindow", "Diario Libre"))
        self.ListinDiarioLabel.setText(_translate("SearchWindow", "Listin Diario"))
        self.PeriodicoLabel.setText(_translate("SearchWindow", "Periodico"))
        self.CategoryLabel.setText(_translate("SearchWindow", "Categoria"))
        self.SearchBtn.setText(_translate("SearchWindow", "Buscar"))
        self.DownloadBtn.setText(_translate("SearchWindow", "Descargar"))
        self.GoBackBtn.setText(_translate("SearchWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())
