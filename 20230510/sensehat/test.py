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


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(385, 598)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 30, 301, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(self.verticalLayoutWidget)
        if (self.table.columnCount() < 8):
            self.table.setColumnCount(8)
        if (self.table.rowCount() < 8):
            self.table.setRowCount(8)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setRowCount(8)
        self.table.setColumnCount(8)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setDefaultSectionSize(36)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.table)

        self.sliderR = QSlider(self.verticalLayoutWidget)
        self.sliderR.setObjectName(u"sliderR")
        self.sliderR.setMaximum(255)
        self.sliderR.setValue(100)
        self.sliderR.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.sliderR)

        self.sliderG = QSlider(self.verticalLayoutWidget)
        self.sliderG.setObjectName(u"sliderG")
        self.sliderG.setMaximum(255)
        self.sliderG.setValue(100)
        self.sliderG.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.sliderG)

        self.sliderB = QSlider(self.verticalLayoutWidget)
        self.sliderB.setObjectName(u"sliderB")
        self.sliderB.setMaximum(255)
        self.sliderB.setValue(100)
        self.sliderB.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.sliderB)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.flash)
        self.pushButton_2.clicked.connect(Form.clear)
        self.table.cellPressed.connect(Form.click)
        self.table.cellEntered.connect(Form.click)
        self.sliderR.valueChanged.connect(Form.rslide)
        self.sliderG.valueChanged.connect(Form.gslide)
        self.sliderB.valueChanged.connect(Form.bslide)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Flash", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

