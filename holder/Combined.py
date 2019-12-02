# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/linux/Desktop/Python/Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from HoyRefined import GetLinksOfElHoy
from ListinDiarioRefined import GetListinDiarioLinks
from DiarioLibreRefined import GetDiarioLibreLinks
from downloadArticles import mainDownloader, DeleteHtmlFile
from DbHandler import WriteDownload, ReadDownload, DeleteDownload, Closer
from invocateBrowser import invoke

class Ui_SearchWindow(object):
    SearchListResult = []
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
        self.DiarioLibreLabel.toggled.connect(lambda:self.RadioButtonElections(self.DiarioLibreLabel))
        self.ListinDiarioLabel = QtWidgets.QRadioButton(self.centralwidget)
        self.ListinDiarioLabel.setGeometry(QtCore.QRect(50, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ListinDiarioLabel.setFont(font)
        self.ListinDiarioLabel.setObjectName("ListinDiarioLabel")
        self.ListinDiarioLabel.toggled.connect(lambda:self.RadioButtonElections(self.ListinDiarioLabel))
        self.CategoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.CategoryComboBox.setGeometry(QtCore.QRect(210, 50, 121, 23))
        self.CategoryComboBox.setObjectName("CategoryComboBox")
        self.CategoryComboBox.currentIndexChanged.connect(self.ComboOptionsChanged)
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
        #self.C connect(self.ResultListBoxClearer)
        self.SearchBtn = QtWidgets.QPushButton(self.centralwidget)
        self.SearchBtn.setGeometry(QtCore.QRect(180, 120, 80, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SearchBtn.setFont(font)
        self.SearchBtn.setObjectName("SearchBtn")
        self.SearchBtn.clicked.connect(self.TrigeredSearch)
        self.DownloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadBtn.setGeometry(QtCore.QRect(180, 560, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DownloadBtn.setFont(font)
        self.DownloadBtn.setObjectName("DownloadBtn")
        self.DownloadBtn.clicked.connect(self.DownloadTriggered)
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
        if self.ElHoyLabel == election:
           if election.isChecked() == True:
                self.CategoryComboBox.clear()
                self.ResultOfSearchListBox.clear()
                CategoryOptions = ["Opinion", "El Pais", "Economia", "Deportes", "EL Mundo", "Vivir", "Alegria"]
                self.CategoryComboBox.addItems(CategoryOptions)
        
        #ListinDiario
        if self.ListinDiarioLabel == election:
            if election.isChecked() == True:
                self.CategoryComboBox.clear()
                self.ResultOfSearchListBox.clear()
                CategoryOptions = ["Republica", "Opinion", "Deportes", "Mundiales", "Entretenimiento", "Vida", "Economia"]
                self.CategoryComboBox.addItems(CategoryOptions)
        
        #DiarioLibre
        if self.DiarioLibreLabel == election:
            if election.isChecked() == True:
                self.CategoryComboBox.clear()
                self.ResultOfSearchListBox.clear()
                CategoryOptions = ["Actualidad", "Economia", "Revista", "Deportes", "Estilos", "Opinion"]
                self.CategoryComboBox.addItems(CategoryOptions)

    def ComboOptionsChanged(self):
        self.ResultOfSearchListBox.clear()

    def ResultListBoxClearer(self):
        self.ResultOfSearchListBox.clear()

    def TrigeredSearch(self):
        if self.ElHoyLabel.isChecked() == True:
                CategoryOptions = ["Opinion", "El Pais", "Economia", "Deportes", "EL Mundo", "Vivir", "Alegria"]
                #Opiniones
                if self.CategoryComboBox.currentText() == CategoryOptions[0]:
                    ResultN = []
                    ResultS = GetLinksOfElHoy(0)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                        ResultN.append(name[1])
                    self.ResultOfSearchListBox.clear()
                    self.ResultOfSearchListBox.addItems(ResultN)
                
                #El Pais
                if self.CategoryComboBox.currentText() == CategoryOptions[1]:
                      ResultN = []
                      ResultS = GetLinksOfElHoy(1)
                      self.SearchListResult = ResultS
                      for name in ResultS:
                          ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Economia
                if self.CategoryComboBox.currentText() == CategoryOptions[2]:
                      ResultN = []
                      ResultS = GetLinksOfElHoy(2)
                      self.SearchListResult = ResultS
                      for name in ResultS:
                          ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Deportes
                if self.CategoryComboBox.currentText() == CategoryOptions[3]:
                      ResultN = []
                      ResultS = GetLinksOfElHoy(3)
                      self.SearchListResult = ResultS
                      for name in ResultS:
                          ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #El Mundo
                if self.CategoryComboBox.currentText() == CategoryOptions[4]:
                      ResultN = []
                      ResultS = GetLinksOfElHoy(4)
                      self.SearchListResult = ResultS
                      for name in ResultS:
                          ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Vivir
                if self.CategoryComboBox.currentText() == CategoryOptions[5]:
                      ResultN = []
                      ResultS = GetLinksOfElHoy(5)
                      self.SearchListResult = ResultS
                      for name in ResultS:
                          ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Alegria
                if self.CategoryComboBox.currentText() == CategoryOptions[6]:
                      ResultN = []
                      ResultS = GetLinksOfElHoy(6)
                      for name in ResultS:
                          ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                       
        if self.DiarioLibreLabel.isChecked() == True:
                CategoryOptions = ["Actualidad", "Economia", "Revista", "Deportes", "Estilos", "Opinion"]
                
                #Actualiad
                if self.CategoryComboBox.currentText() == CategoryOptions[0]:
                    ResultN = []
                    ResultS = GetDiarioLibreLinks(0)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                    
                #Economia
                if self.CategoryComboBox.currentText() == CategoryOptions[1]:
                    ResultN = []
                    ResultS = GetDiarioLibreLinks(1)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Revista
                if self.CategoryComboBox.currentText() == CategoryOptions[2]:
                    ResultN = []
                    ResultS = GetDiarioLibreLinks(2)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Deportes
                if self.CategoryComboBox.currentText() == CategoryOptions[3]:
                    ResultN = []
                    ResultS = GetDiarioLibreLinks(3)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Estilos
                if self.CategoryComboBox.currentText() == CategoryOptions[4]:
                    ResultN = []
                    ResultS = GetDiarioLibreLinks(4)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                #Opinion
                if self.CategoryComboBox.currentText() == CategoryOptions[5]:
                    ResultN = []
                    ResultS = GetDiarioLibreLinks(5)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
        if self.ListinDiarioLabel.isChecked() == True:
                CategoryOptions = ["Republica", "Opinion", "Deportes", "Mundiales", "Entretenimiento", "Vida", "Economia"]
                
                    #Republica
                if self.CategoryComboBox.currentText() == CategoryOptions[0]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(0)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                    #Openion
                elif self.CategoryComboBox.currentText() == CategoryOptions[1]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(1)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)

                    #Deportes
                elif self.CategoryComboBox.currentText() == CategoryOptions[2]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(2)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)

                    #Mundiales
                elif self.CategoryComboBox.currentText() == CategoryOptions[3]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(3)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                    #Entretenimiento
                elif self.CategoryComboBox.currentText() == CategoryOptions[4]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(3)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)
                
                    #Vida
                elif self.CategoryComboBox.currentText() == CategoryOptions[5]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(4)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)

                    #Economia
                elif self.CategoryComboBox.currentText() == CategoryOptions[6]:
                    ResultN = []
                    ResultS = GetListinDiarioLinks(5)
                    self.SearchListResult = ResultS
                    for name in ResultS:
                      ResultN.append(name[1])
                      self.ResultOfSearchListBox.clear()
                      self.ResultOfSearchListBox.addItems(ResultN)

    def DownloadTriggered(self):
        if len(self.ResultOfSearchListBox.selectedIndexes()) > 0:
            listOfItems = self.ResultOfSearchListBox.selectedItems()
            #self.CategoryComboBox.clear()
            for item in listOfItems:
                #holdingIndex = self.ResultOfSearchListBox.currentRow()
                #holdingText = self.ResultOfSearchListBox.currentItem().text()
                #self.CategoryComboBox.addItem(item.text())
                for link in self.SearchListResult:
                    if link[1] == item.text():
                        #self.CategoryComboBox.addItem(item.text())
                        if self.ElHoyLabel.isChecked():
                            downloadedPath = mainDownloader(link[0])
                            WriteDownload( link[1], downloadedPath)
                        
                        elif self.ListinDiarioLabel.isChecked():
                            downloadedPath = mainDownloader(link[0])
                            WriteDownload(link[1], downloadedPath)
                        
                        elif self.DiarioLibreLabel.isChecked():
                            downloadedPath = mainDownloader(link[0])
                            WriteDownload(link[1], downloadedPath)
        
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
        #QtWidgets.QListWidget
        self.DownloadedArticlesListView = QtWidgets.QListWidget(self.centralwidget)
        self.DownloadedArticlesListView.setGeometry(QtCore.QRect(10, 20, 521, 461))
        self.DownloadedArticlesListView.setObjectName("DownloadedArticlesListView")
        
        self.OpenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.OpenBtn.setGeometry(QtCore.QRect(540, 160, 80, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.OpenBtn.setFont(font)
        self.OpenBtn.setObjectName("OpenBtn")
        self.OpenBtn.clicked.connect(self.OpenArtile)
        self.DeleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteBtn.setGeometry(QtCore.QRect(540, 280, 80, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteBtn.setFont(font)
        self.DeleteBtn.setObjectName("DeleteBtn")
        self.DeleteBtn.clicked.connect(self.DeleteArticle)
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

    def OpenArtile(self):
        ListData = ReadDownload()
        
        if len(self.DownloadedArticlesListView.selectedIndexes()) <= 0:
            for item in ListData:
                self.DownloadedArticlesListView.addItem(item[1])
            Closer()
        if len(self.DownloadedArticlesListView.selectedIndexes()) > 0:
            listOfItems = self.DownloadedArticlesListView.selectedItems()
            for item in listOfItems:
                for row in ListData:
                    if item.text() == row[1]:
                        invoke(row[2])

    def DeleteArticle(self):
        ListData = ReadDownload()
        Closer()
        if len(self.DownloadedArticlesListView.selectedIndexes()) > 0:
            listOfItems = self.DownloadedArticlesListView.selectedItems()
            for item in listOfItems:
                for row in ListData:
                    if item.text() == row[1]:
                        #Aqui va una funcion que tome como argumento el path del archivo. Preferiblemente que sea lo mismo de la db. Para borrarlo de la db y de el directorio
                        DeleteHtmlFile(row[2])
                        DeleteDownload(row[2])
                        newListData = ReadDownload()
                        for newItem in newListData:
                            self.DownloadedArticlesListView.addItem(newItem[1])
            Closer()

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

