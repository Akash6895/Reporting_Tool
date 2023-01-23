# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CalendarZmgyPK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.calendar = QCalendarWidget(Dialog)
        self.calendar.setObjectName(u"calendar")
        self.calendar.setStyleSheet(u"background-color: rgb(73, 81, 99);\n"
"alternate-background-color: rgb(44, 49, 60);\n"
"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";")

        self.gridLayout.addWidget(self.calendar, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

