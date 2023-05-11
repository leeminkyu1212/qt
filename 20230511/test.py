# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 20, 968, 434))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pic1 = QLabel(self.gridLayoutWidget)
        self.pic1.setObjectName(u"pic1")
        self.pic1.setMinimumSize(QSize(480, 320))
        self.pic1.setMaximumSize(QSize(480, 320))

        self.gridLayout.addWidget(self.pic1, 0, 0, 1, 1)

        self.pic2 = QLabel(self.gridLayoutWidget)
        self.pic2.setObjectName(u"pic2")
        self.pic2.setMinimumSize(QSize(480, 320))
        self.pic2.setMaximumSize(QSize(480, 320))

        self.gridLayout.addWidget(self.pic2, 0, 1, 1, 1)

        self.playBtn = QPushButton(self.gridLayoutWidget)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setMinimumSize(QSize(960, 50))
        self.playBtn.setMaximumSize(QSize(960, 50))

        self.gridLayout.addWidget(self.playBtn, 1, 0, 1, 2)

        self.modeBtn = QPushButton(self.gridLayoutWidget)
        self.modeBtn.setObjectName(u"modeBtn")
        self.modeBtn.setMinimumSize(QSize(960, 50))
        self.modeBtn.setMaximumSize(QSize(960, 50))

        self.gridLayout.addWidget(self.modeBtn, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1005, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.playBtn.clicked.connect(MainWindow.play)
        self.modeBtn.clicked.connect(MainWindow.mode)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pic1.setText("")
        self.pic2.setText("")
        self.playBtn.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.modeBtn.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
    # retranslateUi

