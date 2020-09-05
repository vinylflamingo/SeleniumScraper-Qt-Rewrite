# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UIiFVBBF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys
sys.path.insert(0, "/Users/frankie/Desktop/SeleniumScraper")
from SeleniumScraperServices import scrapeService
from SeleniumScraperServices import textService
from SeleniumScraperUI import appEvents


#from ...SeleniumScraperServices import ScrapeService, TextService

print(sys.path)


class Ui_MainWindow(object):
    def addEvents(self, MainWindow):
       self.textService = textService.TextService()
       self.scrapeService = scrapeService.ScrapeService()
       self.appEvents = appEvents.AppEvents(MainWindow, self.textService, self.scrapeService)
       self.pushButtonStart.clicked.connect(self.appEvents.startButtonClick)
   

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(321, 353)
        #appEvents = AppEvents.AppEvents
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 295, 294))
        self.MainBox = QVBoxLayout(self.widget)
        self.MainBox.setObjectName(u"MainBox")
        self.MainBox.setContentsMargins(0, 0, 0, 0)
        self.PhoneBox = QHBoxLayout()
        self.PhoneBox.setObjectName(u"PhoneBox")
        self.labelPhoneNumber = QLabel(self.widget)
        self.labelPhoneNumber.setObjectName(u"labelPhoneNumber")

        self.PhoneBox.addWidget(self.labelPhoneNumber)

        self.lineEditPhoneNumber = QLineEdit(self.widget)
        self.lineEditPhoneNumber.setObjectName(u"lineEditPhoneNumber")

        self.PhoneBox.addWidget(self.lineEditPhoneNumber)


        self.MainBox.addLayout(self.PhoneBox)

        self.KeyWordsBox = QVBoxLayout()
        self.KeyWordsBox.setObjectName(u"KeyWordsBox")
        self.labelKeyWords = QLabel(self.widget)
        self.labelKeyWords.setObjectName(u"labelKeyWords")

        self.KeyWordsBox.addWidget(self.labelKeyWords)

        self.textEditKeyWords = QTextEdit(self.widget)
        self.textEditKeyWords.setObjectName(u"textEditKeyWords")

        self.KeyWordsBox.addWidget(self.textEditKeyWords)

        self.pushButtonStart = QPushButton(self.widget)
        self.pushButtonStart.setObjectName(u"pushButtonStart")

        self.KeyWordsBox.addWidget(self.pushButtonStart)


        self.MainBox.addLayout(self.KeyWordsBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 321, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Search Hirebridge", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.labelPhoneNumber.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.labelKeyWords.setText(QCoreApplication.translate("MainWindow", u"Keywords: (Seperate multiple using a comma ,)", None))
        self.pushButtonStart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    from PySide2 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.addEvents(ui)
    MainWindow.show()
    sys.exit(app.exec_())