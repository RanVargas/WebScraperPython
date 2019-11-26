# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/linux/Desktop/Python/Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from moretest import GetLinksOfEditorial

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
        self.ElHoyLabel.toggled.connect(lambda:self.RadioButtonElections(self.ElHoyLabel))
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

    def RadioButtonElections(self, election):
        #ElHoy
        if election.isChecked() == True:
            Result = GetLinksOfEditorial()
            for item in Result:
                self.ResultOfSearchListBox.addItem(item[1])
        
        #ListinDiario
        if election.isChecked() == True:
            pass
        
        #DiarioLibre
        if election.isChecked() == True:
            pass


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
        DownloadedWindow.setWindowTitle(_translate("DownloadedWindow", "Articulos Descargados"))
        self.OpenBtn.setText(_translate("DownloadedWindow", "Abrir"))
        self.DeleteBtn.setText(_translate("DownloadedWindow", "Borrar"))
        self.GoBackBtn.setText(_translate("DownloadedWindow", "Salir"))



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
        #self.DownloadedBtn.clicked.connect(self.OpenDownloadedSearchWindow)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def OpenDownloadedSearchWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DownloadedWindow()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        #self.Ui_DownloadedWindow = DownloadedSearchWindow()
        #self.Ui_DownloadedWindow.show()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchTriggerBtn.setText(_translate("MainWindow", "Buscar"))
        self.DownloadedBtn.setText(_translate("MainWindow", "Descargados"))


def ChangeWindow(presentW, futureW):
    presentW.hide()
    futureW.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    DownloadedWindow = QtWidgets.QMainWindow()
    SearchWindow = QtWidgets.QMainWindow()
    
    MainUi = Ui_MainWindow()
    MainUi.setupUi(MainWindow)
    DownloadedSUi = Ui_DownloadedWindow()
    DownloadedSUi.setupUi(DownloadedWindow)
    SearchUi = Ui_SearchWindow()
    SearchUi.setupUi(SearchWindow)
    DownloadedSUi.GoBackBtn.clicked.connect(lambda: ChangeWindow(DownloadedWindow, MainWindow))
    SearchUi.GoBackBtn.clicked.connect(lambda: ChangeWindow(SearchWindow, MainWindow))
    MainUi.DownloadedBtn.clicked.connect(lambda: ChangeWindow(MainWindow, DownloadedWindow))
    MainUi.SearchTriggerBtn.clicked.connect(lambda: ChangeWindow(MainWindow, SearchWindow))
    
    MainWindow.show()
    sys.exit(app.exec_())

