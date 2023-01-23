# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiHXGJGj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 20px;\n"
"	padding-right: 20px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, "
                        "77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
""
                        "    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height"
                        ": 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractI"
                        "temView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}"
                        "\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setFocusPolicy(Qt.NoFocus)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet(u"\n"
"color: rgb(169, 170, 172);\n"
"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setFocusPolicy(Qt.NoFocus)
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setFocusPolicy(Qt.NoFocus)
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setFocusPolicy(Qt.NoFocus)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(230, 0, 0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font1)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_top_info_2.setFont(font2)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_user_icon.setFont(font3)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	color: rgb(169, 170, 172);\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/logo/Users/ATARALK/Desktop/QT_Tutorials/Tutorial_10/icons/logo/xylem-logo-transparent.png"))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(40)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.label_6)

        self.label_5 = QLabel(self.page_home)
        self.label_5.setObjectName(u"label_5")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(14)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(169, 170, 172);")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_10.addWidget(self.label_5)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(169, 170, 172);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(0)

        self.verticalLayout_10.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_home)
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.horizontalLayout_15 = QHBoxLayout(self.page_login)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.bgwidget = QWidget(self.page_login)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.bgwidget)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.bgwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setMinimumSize(QSize(400, 500))
        self.frame_5.setMaximumSize(QSize(500, 500))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(341, 70))
        self.label_2.setMaximumSize(QSize(341, 70))
        self.label_2.setStyleSheet(u"font: 34pt \"MS Shell Dlg 2\"; \n"
"color: rgb(169, 178, 200);\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(341, 30))
        self.label_3.setMaximumSize(QSize(341, 30))
        self.label_3.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(169, 178, 200);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(341, 30))
        self.label_4.setMaximumSize(QSize(341, 30))
        font6 = QFont()
        font6.setFamily(u"MS Shell Dlg 2")
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setItalic(False)
        font6.setWeight(50)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 170, 255);")

        self.verticalLayout_13.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.emailfield = QLineEdit(self.frame_5)
        self.emailfield.setObjectName(u"emailfield")
        self.emailfield.setMinimumSize(QSize(341, 51))
        self.emailfield.setMaximumSize(QSize(341, 51))
        self.emailfield.setFocusPolicy(Qt.StrongFocus)
        self.emailfield.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}")
        self.emailfield.setFrame(False)

        self.verticalLayout_13.addWidget(self.emailfield, 0, Qt.AlignHCenter)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(341, 30))
        self.label_9.setMaximumSize(QSize(341, 30))
        self.label_9.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 170, 255);")

        self.verticalLayout_13.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.passwordfield = QLineEdit(self.frame_5)
        self.passwordfield.setObjectName(u"passwordfield")
        self.passwordfield.setMinimumSize(QSize(341, 51))
        self.passwordfield.setMaximumSize(QSize(341, 51))
        self.passwordfield.setFocusPolicy(Qt.StrongFocus)
        self.passwordfield.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}\n"
"")
        self.passwordfield.setFrame(False)
        self.passwordfield.setEchoMode(QLineEdit.Password)

        self.verticalLayout_13.addWidget(self.passwordfield, 0, Qt.AlignHCenter)

        self.error = QLabel(self.frame_5)
        self.error.setObjectName(u"error")
        self.error.setMinimumSize(QSize(341, 40))
        self.error.setMaximumSize(QSize(341, 40))
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(50)
        self.error.setFont(font7)
        self.error.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\"; color:red;")

        self.verticalLayout_13.addWidget(self.error, 0, Qt.AlignHCenter)

        self.login = QPushButton(self.frame_5)
        self.login.setObjectName(u"login")
        self.login.setMinimumSize(QSize(341, 51))
        self.login.setMaximumSize(QSize(341, 51))
        self.login.setFocusPolicy(Qt.NoFocus)
        self.login.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"background-color: rgb(72, 145, 217);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 127);\n"
"}")

        self.verticalLayout_13.addWidget(self.login, 0, Qt.AlignHCenter)

        self.create = QPushButton(self.frame_5)
        self.create.setObjectName(u"create")
        self.create.setMinimumSize(QSize(341, 51))
        self.create.setMaximumSize(QSize(22222, 51))
        self.create.setFocusPolicy(Qt.NoFocus)
        self.create.setStyleSheet(u"QPushButton \n"
"{ background-color: transparent;\n"
" border: 0px; \n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(169, 178, 200);}\n"
"QPushButton:hover \n"
"{ background-color: transparent;\n"
" border: 0px; \n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 255, 127);}")

        self.verticalLayout_13.addWidget(self.create, 0, Qt.AlignHCenter)


        self.horizontalLayout_14.addWidget(self.frame_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.frame_4)


        self.horizontalLayout_15.addWidget(self.bgwidget)

        self.stackedWidget.addWidget(self.page_login)
        self.page_conn = QWidget()
        self.page_conn.setObjectName(u"page_conn")
        self.verticalLayout_14 = QVBoxLayout(self.page_conn)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_6 = QFrame(self.page_conn)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy7)
        self.frame_7.setMinimumSize(QSize(550, 200))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.DataBase = QLineEdit(self.frame_7)
        self.DataBase.setObjectName(u"DataBase")
        self.DataBase.setGeometry(QRect(196, 57, 341, 51))
        sizePolicy8 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.DataBase.sizePolicy().hasHeightForWidth())
        self.DataBase.setSizePolicy(sizePolicy8)
        self.DataBase.setMinimumSize(QSize(341, 0))
        self.DataBase.setMaximumSize(QSize(341, 51))
        self.DataBase.setFont(font6)
        self.DataBase.setFocusPolicy(Qt.StrongFocus)
        self.DataBase.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}")
        self.DataBase.setFrame(False)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 190, 51))
        self.label_12.setMinimumSize(QSize(190, 51))
        font8 = QFont()
        font8.setPointSize(14)
        self.label_12.setFont(font8)
        self.label_12.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 57, 190, 51))
        self.label_13.setMinimumSize(QSize(190, 51))
        self.label_13.setFont(font8)
        self.label_13.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.ServerName = QLineEdit(self.frame_7)
        self.ServerName.setObjectName(u"ServerName")
        self.ServerName.setGeometry(QRect(196, 0, 341, 51))
        self.ServerName.setMinimumSize(QSize(341, 51))
        self.ServerName.setMaximumSize(QSize(341, 51))
        self.ServerName.setFont(font6)
        self.ServerName.setFocusPolicy(Qt.StrongFocus)
        self.ServerName.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}")
        self.ServerName.setFrame(False)
        self.clear_PB = QPushButton(self.frame_7)
        self.clear_PB.setObjectName(u"clear_PB")
        self.clear_PB.setGeometry(QRect(200, 140, 150, 50))
        self.clear_PB.setMinimumSize(QSize(150, 50))
        self.clear_PB.setMaximumSize(QSize(150, 50))
        self.clear_PB.setFont(font6)
        self.clear_PB.setFocusPolicy(Qt.NoFocus)
        self.clear_PB.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: rgb(72, 145, 217);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 127);\n"
"}")
        self.Connect_PB = QPushButton(self.frame_7)
        self.Connect_PB.setObjectName(u"Connect_PB")
        self.Connect_PB.setGeometry(QRect(390, 140, 150, 50))
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.Connect_PB.sizePolicy().hasHeightForWidth())
        self.Connect_PB.setSizePolicy(sizePolicy9)
        self.Connect_PB.setMinimumSize(QSize(150, 50))
        self.Connect_PB.setMaximumSize(QSize(150, 50))
        self.Connect_PB.setFont(font6)
        self.Connect_PB.setFocusPolicy(Qt.NoFocus)
        self.Connect_PB.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"background-color: rgb(72, 145, 217);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 127);\n"
"}")

        self.horizontalLayout_17.addWidget(self.frame_7)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page_conn)
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.verticalLayout_18 = QVBoxLayout(self.page_data)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.table_frame = QFrame(self.page_data)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.table_frame)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.table_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.From_Date_frame = QFrame(self.frame_8)
        self.From_Date_frame.setObjectName(u"From_Date_frame")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.From_Date_frame.sizePolicy().hasHeightForWidth())
        self.From_Date_frame.setSizePolicy(sizePolicy10)
        self.From_Date_frame.setMaximumSize(QSize(320, 150))
        self.From_Date_frame.setStyleSheet(u"")
        self.From_Date_frame.setFrameShape(QFrame.StyledPanel)
        self.From_Date_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.From_Date_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_14 = QLabel(self.From_Date_frame)
        self.label_14.setObjectName(u"label_14")
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy11)
        self.label_14.setMinimumSize(QSize(150, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(False)
        font9.setWeight(50)
        self.label_14.setFont(font9)
        self.label_14.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_14, 1, 0, 1, 1)

        self.From_Time = QTimeEdit(self.From_Date_frame)
        self.From_Time.setObjectName(u"From_Time")
        sizePolicy.setHeightForWidth(self.From_Time.sizePolicy().hasHeightForWidth())
        self.From_Time.setSizePolicy(sizePolicy)
        self.From_Time.setMinimumSize(QSize(130, 25))
        self.From_Time.setMaximumSize(QSize(16777215, 25))
        self.From_Time.setFont(font6)
        self.From_Time.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.From_Time.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.From_Time, 3, 0, 1, 1)

        self.From_Date = QDateEdit(self.From_Date_frame)
        self.From_Date.setObjectName(u"From_Date")
        sizePolicy9.setHeightForWidth(self.From_Date.sizePolicy().hasHeightForWidth())
        self.From_Date.setSizePolicy(sizePolicy9)
        self.From_Date.setMinimumSize(QSize(130, 25))
        self.From_Date.setMaximumSize(QSize(16777215, 16777215))
        self.From_Date.setFont(font6)
        self.From_Date.setAcceptDrops(False)
        self.From_Date.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.From_Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.From_Date, 2, 0, 1, 1)

        self.From_Date_PB = QPushButton(self.From_Date_frame)
        self.From_Date_PB.setObjectName(u"From_Date_PB")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.From_Date_PB.sizePolicy().hasHeightForWidth())
        self.From_Date_PB.setSizePolicy(sizePolicy12)
        self.From_Date_PB.setMaximumSize(QSize(30, 25))
        self.From_Date_PB.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(73, 81, 99);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/24x24/icons/24x24/cil-calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.From_Date_PB.setIcon(icon3)
        self.From_Date_PB.setIconSize(QSize(25, 25))

        self.gridLayout_7.addWidget(self.From_Date_PB, 2, 1, 1, 1)


        self.horizontalLayout_18.addWidget(self.From_Date_frame)

        self.To_Date_frame = QFrame(self.frame_8)
        self.To_Date_frame.setObjectName(u"To_Date_frame")
        sizePolicy10.setHeightForWidth(self.To_Date_frame.sizePolicy().hasHeightForWidth())
        self.To_Date_frame.setSizePolicy(sizePolicy10)
        self.To_Date_frame.setMaximumSize(QSize(320, 150))
        self.To_Date_frame.setStyleSheet(u"")
        self.To_Date_frame.setFrameShape(QFrame.StyledPanel)
        self.To_Date_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.To_Date_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.To_Date = QDateEdit(self.To_Date_frame)
        self.To_Date.setObjectName(u"To_Date")
        sizePolicy9.setHeightForWidth(self.To_Date.sizePolicy().hasHeightForWidth())
        self.To_Date.setSizePolicy(sizePolicy9)
        self.To_Date.setMinimumSize(QSize(130, 25))
        self.To_Date.setMaximumSize(QSize(16777215, 16777215))
        self.To_Date.setFont(font6)
        self.To_Date.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.To_Date.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.To_Date, 1, 0, 1, 1)

        self.To_Date_PB = QPushButton(self.To_Date_frame)
        self.To_Date_PB.setObjectName(u"To_Date_PB")
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.To_Date_PB.sizePolicy().hasHeightForWidth())
        self.To_Date_PB.setSizePolicy(sizePolicy13)
        self.To_Date_PB.setMaximumSize(QSize(30, 25))
        self.To_Date_PB.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(73, 81, 99);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.To_Date_PB.setIcon(icon3)
        self.To_Date_PB.setIconSize(QSize(24, 24))

        self.gridLayout_6.addWidget(self.To_Date_PB, 1, 1, 1, 1)

        self.To_Time = QTimeEdit(self.To_Date_frame)
        self.To_Time.setObjectName(u"To_Time")
        sizePolicy.setHeightForWidth(self.To_Time.sizePolicy().hasHeightForWidth())
        self.To_Time.setSizePolicy(sizePolicy)
        self.To_Time.setMinimumSize(QSize(130, 25))
        self.To_Time.setMaximumSize(QSize(16777215, 25))
        self.To_Time.setFont(font6)
        self.To_Time.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.To_Time.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.To_Time, 2, 0, 1, 1)

        self.label_15 = QLabel(self.To_Date_frame)
        self.label_15.setObjectName(u"label_15")
        sizePolicy11.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy11)
        self.label_15.setMinimumSize(QSize(150, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setFont(font9)
        self.label_15.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.To_Date_frame)

        self.col_filter_frame = QFrame(self.frame_8)
        self.col_filter_frame.setObjectName(u"col_filter_frame")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy14.setHorizontalStretch(1)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.col_filter_frame.sizePolicy().hasHeightForWidth())
        self.col_filter_frame.setSizePolicy(sizePolicy14)
        self.col_filter_frame.setMaximumSize(QSize(300, 150))
        self.col_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.col_filter_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.col_filter_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(9, 9, -1, 9)
        self.colom_name = QComboBox(self.col_filter_frame)
        self.colom_name.addItem("")
        self.colom_name.setObjectName(u"colom_name")
        sizePolicy14.setHeightForWidth(self.colom_name.sizePolicy().hasHeightForWidth())
        self.colom_name.setSizePolicy(sizePolicy14)
        self.colom_name.setMinimumSize(QSize(150, 30))
        self.colom_name.setMaximumSize(QSize(16777215, 25))
        font10 = QFont()
        font10.setPointSize(12)
        self.colom_name.setFont(font10)
        self.colom_name.setLayoutDirection(Qt.LeftToRight)
        self.colom_name.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"border-color: rgb(50, 56, 68);\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.colom_name, 3, 0, 1, 1)

        self.label_16 = QLabel(self.col_filter_frame)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMinimumSize(QSize(150, 20))
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setFont(font10)
        self.label_16.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.horizontalLayout_18.addWidget(self.col_filter_frame)

        self.btn_frame = QFrame(self.frame_8)
        self.btn_frame.setObjectName(u"btn_frame")
        sizePolicy.setHeightForWidth(self.btn_frame.sizePolicy().hasHeightForWidth())
        self.btn_frame.setSizePolicy(sizePolicy)
        self.btn_frame.setMinimumSize(QSize(200, 0))
        self.btn_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.btn_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.Filter_PB = QPushButton(self.btn_frame)
        self.Filter_PB.setObjectName(u"Filter_PB")
        self.Filter_PB.setMinimumSize(QSize(150, 30))
        self.Filter_PB.setMaximumSize(QSize(200, 16777215))
        self.Filter_PB.setFont(font10)
        self.Filter_PB.setFocusPolicy(Qt.NoFocus)
        self.Filter_PB.setStyleSheet(u"QPushButton {\n"
"        background-image:url(:/20x20/icons/20x20/cil-filter.png);\n"
"        background-position: left center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 25px solid rgb(50, 56, 68);\n"
"        background-color: rgb(50, 56, 68);\n"
"        text-align: left;\n"
"        padding-left: 30px;\n"
"        color: rgb(169, 170, 172);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(33, 37, 43);\n"
"        border-left: 25px solid rgb(33, 37, 43);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(85, 170, 255);\n"
"        border-left: 25px solid rgb(85, 170, 255);\n"
"    }")
        self.Filter_PB.setIconSize(QSize(20, 20))

        self.verticalLayout_17.addWidget(self.Filter_PB)

        self.LoadAll_PB = QPushButton(self.btn_frame)
        self.LoadAll_PB.setObjectName(u"LoadAll_PB")
        self.LoadAll_PB.setMinimumSize(QSize(150, 30))
        self.LoadAll_PB.setMaximumSize(QSize(200, 16777215))
        self.LoadAll_PB.setFont(font10)
        self.LoadAll_PB.setFocusPolicy(Qt.NoFocus)
        self.LoadAll_PB.setStyleSheet(u"QPushButton {\n"
"        background-image: url(:/20x20/icons/20x20/cil-loop-circular.png);\n"
"        background-position: left center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 25px solid rgb(50, 56, 68);\n"
"        background-color: rgb(50, 56, 68);\n"
"        text-align: left;\n"
"        padding-left: 30px;\n"
"        color: rgb(169, 170, 172);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(33, 37, 43);\n"
"        border-left: 25px solid rgb(33, 37, 43);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(85, 170, 255);\n"
"        border-left: 25px solid rgb(85, 170, 255);\n"
"    }")
        self.LoadAll_PB.setIconSize(QSize(20, 20))

        self.verticalLayout_17.addWidget(self.LoadAll_PB)

        self.Export_PB = QPushButton(self.btn_frame)
        self.Export_PB.setObjectName(u"Export_PB")
        self.Export_PB.setMinimumSize(QSize(150, 30))
        self.Export_PB.setMaximumSize(QSize(200, 16777215))
        self.Export_PB.setFont(font10)
        self.Export_PB.setFocusPolicy(Qt.NoFocus)
        self.Export_PB.setStyleSheet(u"QPushButton {\n"
"        background-image: url(:/20x20/icons/20x20/cil-external-link.png);\n"
"        background-position: left center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 25px solid rgb(50, 56, 68);\n"
"        background-color: rgb(50, 56, 68);\n"
"        text-align: left;\n"
"        padding-left: 30px;\n"
"        color: rgb(169, 170, 172);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(33, 37, 43);\n"
"        border-left: 25px solid rgb(33, 37, 43);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(85, 170, 255);\n"
"        border-left: 25px solid rgb(85, 170, 255);\n"
"    }")
        self.Export_PB.setAutoRepeatDelay(298)

        self.verticalLayout_17.addWidget(self.Export_PB)


        self.horizontalLayout_18.addWidget(self.btn_frame, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.frame_8)

        self.Data_Table = QTableWidget(self.table_frame)
        if (self.Data_Table.columnCount() < 50):
            self.Data_Table.setColumnCount(50)
        if (self.Data_Table.rowCount() < 50):
            self.Data_Table.setRowCount(50)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.NoBrush)
        font11 = QFont()
        font11.setFamily(u"MS Shell Dlg 2")
        font11.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font11);
        __qtablewidgetitem.setBackground(brush1);
        __qtablewidgetitem.setForeground(brush);
        self.Data_Table.setItem(0, 0, __qtablewidgetitem)
        self.Data_Table.setObjectName(u"Data_Table")
        sizePolicy15 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy15.setHorizontalStretch(1)
        sizePolicy15.setVerticalStretch(1)
        sizePolicy15.setHeightForWidth(self.Data_Table.sizePolicy().hasHeightForWidth())
        self.Data_Table.setSizePolicy(sizePolicy15)
        self.Data_Table.setMaximumSize(QSize(16777215, 16777215))
        self.Data_Table.setLayoutDirection(Qt.LeftToRight)
        self.Data_Table.setStyleSheet(u"QHeaderView::section {\n"
"    background-color:rgb(73, 81, 99);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(73, 81, 99);\n"
"	color: rgb(255, 255, 255);\n"
"	gridline-color: rgb(169, 178, 200);\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.Data_Table.setFrameShape(QFrame.Box)
        self.Data_Table.setFrameShadow(QFrame.Sunken)
        self.Data_Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.Data_Table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.Data_Table.setSortingEnabled(True)
        self.Data_Table.setRowCount(50)
        self.Data_Table.setColumnCount(50)
        self.Data_Table.horizontalHeader().setCascadingSectionResizes(False)
        self.Data_Table.verticalHeader().setMinimumSectionSize(35)

        self.verticalLayout_16.addWidget(self.Data_Table)


        self.verticalLayout_18.addWidget(self.table_frame)

        self.stackedWidget.addWidget(self.page_data)
        self.page_graph = QWidget()
        self.page_graph.setObjectName(u"page_graph")
        self.verticalLayout_6 = QVBoxLayout(self.page_graph)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.graph_frame = QFrame(self.page_graph)
        self.graph_frame.setObjectName(u"graph_frame")
        self.graph_frame.setMinimumSize(QSize(0, 150))
        self.graph_frame.setFrameShape(QFrame.StyledPanel)
        self.graph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.graph_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.graph_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setStyleSheet(u"background-color: rgb(27, 29, 35);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.From_Date_frame_2 = QFrame(self.frame_3)
        self.From_Date_frame_2.setObjectName(u"From_Date_frame_2")
        sizePolicy10.setHeightForWidth(self.From_Date_frame_2.sizePolicy().hasHeightForWidth())
        self.From_Date_frame_2.setSizePolicy(sizePolicy10)
        self.From_Date_frame_2.setMaximumSize(QSize(320, 150))
        self.From_Date_frame_2.setStyleSheet(u"")
        self.From_Date_frame_2.setFrameShape(QFrame.StyledPanel)
        self.From_Date_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.From_Date_frame_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.From_Date_PB_G = QPushButton(self.From_Date_frame_2)
        self.From_Date_PB_G.setObjectName(u"From_Date_PB_G")
        sizePolicy12.setHeightForWidth(self.From_Date_PB_G.sizePolicy().hasHeightForWidth())
        self.From_Date_PB_G.setSizePolicy(sizePolicy12)
        self.From_Date_PB_G.setMaximumSize(QSize(30, 25))
        self.From_Date_PB_G.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(73, 81, 99);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.From_Date_PB_G.setIcon(icon3)
        self.From_Date_PB_G.setIconSize(QSize(25, 25))

        self.gridLayout_8.addWidget(self.From_Date_PB_G, 2, 1, 1, 1)

        self.From_Date_G = QDateEdit(self.From_Date_frame_2)
        self.From_Date_G.setObjectName(u"From_Date_G")
        sizePolicy9.setHeightForWidth(self.From_Date_G.sizePolicy().hasHeightForWidth())
        self.From_Date_G.setSizePolicy(sizePolicy9)
        self.From_Date_G.setMinimumSize(QSize(130, 25))
        self.From_Date_G.setMaximumSize(QSize(16777215, 16777215))
        self.From_Date_G.setFont(font6)
        self.From_Date_G.setAcceptDrops(False)
        self.From_Date_G.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.From_Date_G.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.From_Date_G, 2, 0, 1, 1)

        self.label_17 = QLabel(self.From_Date_frame_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy11.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy11)
        self.label_17.setMinimumSize(QSize(150, 20))
        self.label_17.setMaximumSize(QSize(16777215, 20))
        self.label_17.setFont(font9)
        self.label_17.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_17, 1, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.From_Date_frame_2)

        self.To_Date_frame_2 = QFrame(self.frame_3)
        self.To_Date_frame_2.setObjectName(u"To_Date_frame_2")
        sizePolicy10.setHeightForWidth(self.To_Date_frame_2.sizePolicy().hasHeightForWidth())
        self.To_Date_frame_2.setSizePolicy(sizePolicy10)
        self.To_Date_frame_2.setMaximumSize(QSize(320, 150))
        self.To_Date_frame_2.setStyleSheet(u"")
        self.To_Date_frame_2.setFrameShape(QFrame.StyledPanel)
        self.To_Date_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.To_Date_frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_18 = QLabel(self.To_Date_frame_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy11.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy11)
        self.label_18.setMinimumSize(QSize(150, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font9)
        self.label_18.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_18, 0, 0, 1, 1)

        self.To_Date_G = QDateEdit(self.To_Date_frame_2)
        self.To_Date_G.setObjectName(u"To_Date_G")
        sizePolicy9.setHeightForWidth(self.To_Date_G.sizePolicy().hasHeightForWidth())
        self.To_Date_G.setSizePolicy(sizePolicy9)
        self.To_Date_G.setMinimumSize(QSize(130, 25))
        self.To_Date_G.setMaximumSize(QSize(16777215, 16777215))
        self.To_Date_G.setFont(font6)
        self.To_Date_G.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.To_Date_G.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.To_Date_G, 1, 0, 1, 1)

        self.To_Date_PB_G = QPushButton(self.To_Date_frame_2)
        self.To_Date_PB_G.setObjectName(u"To_Date_PB_G")
        sizePolicy13.setHeightForWidth(self.To_Date_PB_G.sizePolicy().hasHeightForWidth())
        self.To_Date_PB_G.setSizePolicy(sizePolicy13)
        self.To_Date_PB_G.setMaximumSize(QSize(30, 25))
        self.To_Date_PB_G.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(73, 81, 99);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        self.To_Date_PB_G.setIcon(icon3)
        self.To_Date_PB_G.setIconSize(QSize(24, 24))

        self.gridLayout_9.addWidget(self.To_Date_PB_G, 1, 1, 1, 1)


        self.horizontalLayout_13.addWidget(self.To_Date_frame_2)

        self.col_filter_frame_2 = QFrame(self.frame_3)
        self.col_filter_frame_2.setObjectName(u"col_filter_frame_2")
        sizePolicy14.setHeightForWidth(self.col_filter_frame_2.sizePolicy().hasHeightForWidth())
        self.col_filter_frame_2.setSizePolicy(sizePolicy14)
        self.col_filter_frame_2.setMaximumSize(QSize(300, 150))
        self.col_filter_frame_2.setFrameShape(QFrame.StyledPanel)
        self.col_filter_frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.col_filter_frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setContentsMargins(9, 9, -1, 9)
        self.label_19 = QLabel(self.col_filter_frame_2)
        self.label_19.setObjectName(u"label_19")
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setMinimumSize(QSize(150, 20))
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setFont(font10)
        self.label_19.setStyleSheet(u"color: rgb(85, 170, 255);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.colom_name_G = QComboBox(self.col_filter_frame_2)
        self.colom_name_G.addItem("")
        self.colom_name_G.setObjectName(u"colom_name_G")
        sizePolicy14.setHeightForWidth(self.colom_name_G.sizePolicy().hasHeightForWidth())
        self.colom_name_G.setSizePolicy(sizePolicy14)
        self.colom_name_G.setMinimumSize(QSize(150, 30))
        self.colom_name_G.setMaximumSize(QSize(16777215, 25))
        self.colom_name_G.setFont(font10)
        self.colom_name_G.setLayoutDirection(Qt.LeftToRight)
        self.colom_name_G.setStyleSheet(u"color: rgb(169, 178, 200);\n"
"border-color: rgb(50, 56, 68);\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.colom_name_G, 2, 0, 1, 1)


        self.horizontalLayout_13.addWidget(self.col_filter_frame_2)

        self.btn_frame_2 = QFrame(self.frame_3)
        self.btn_frame_2.setObjectName(u"btn_frame_2")
        sizePolicy.setHeightForWidth(self.btn_frame_2.sizePolicy().hasHeightForWidth())
        self.btn_frame_2.setSizePolicy(sizePolicy)
        self.btn_frame_2.setMinimumSize(QSize(200, 0))
        self.btn_frame_2.setFrameShape(QFrame.StyledPanel)
        self.btn_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.btn_frame_2)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(1, 1, 1, 1)
        self.Filter_PB_G = QPushButton(self.btn_frame_2)
        self.Filter_PB_G.setObjectName(u"Filter_PB_G")
        self.Filter_PB_G.setMinimumSize(QSize(150, 22))
        self.Filter_PB_G.setMaximumSize(QSize(200, 16777215))
        self.Filter_PB_G.setFont(font10)
        self.Filter_PB_G.setFocusPolicy(Qt.NoFocus)
        self.Filter_PB_G.setStyleSheet(u"QPushButton {\n"
"        background-image:url(:/20x20/icons/20x20/cil-filter.png);\n"
"        background-position: left center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 25px solid rgb(50, 56, 68);\n"
"        background-color: rgb(50, 56, 68);\n"
"        text-align: left;\n"
"        padding-left: 30px;\n"
"        color: rgb(169, 170, 172);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(33, 37, 43);\n"
"        border-left: 25px solid rgb(33, 37, 43);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(85, 170, 255);\n"
"        border-left: 25px solid rgb(85, 170, 255);\n"
"    }")
        self.Filter_PB_G.setIconSize(QSize(20, 20))

        self.verticalLayout_19.addWidget(self.Filter_PB_G)

        self.LoadAll_PB_G = QPushButton(self.btn_frame_2)
        self.LoadAll_PB_G.setObjectName(u"LoadAll_PB_G")
        self.LoadAll_PB_G.setMinimumSize(QSize(150, 22))
        self.LoadAll_PB_G.setMaximumSize(QSize(200, 16777215))
        self.LoadAll_PB_G.setFont(font10)
        self.LoadAll_PB_G.setFocusPolicy(Qt.NoFocus)
        self.LoadAll_PB_G.setStyleSheet(u"QPushButton {\n"
"        background-image: url(:/20x20/icons/20x20/cil-loop-circular.png);\n"
"        background-position: left center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 25px solid rgb(50, 56, 68);\n"
"        background-color: rgb(50, 56, 68);\n"
"        text-align: left;\n"
"        padding-left: 30px;\n"
"        color: rgb(169, 170, 172);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(33, 37, 43);\n"
"        border-left: 25px solid rgb(33, 37, 43);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(85, 170, 255);\n"
"        border-left: 25px solid rgb(85, 170, 255);\n"
"    }")
        self.LoadAll_PB_G.setIconSize(QSize(20, 20))

        self.verticalLayout_19.addWidget(self.LoadAll_PB_G)

        self.email_pb = QPushButton(self.btn_frame_2)
        self.email_pb.setObjectName(u"email_pb")
        self.email_pb.setMinimumSize(QSize(0, 22))
        self.email_pb.setFont(font10)
        self.email_pb.setStyleSheet(u"QPushButton {\n"
"        background-image: url(:/20x20/icons/20x20/cil-cursor.png);\n"
"        background-position: left center;\n"
"        background-repeat: no-repeat;\n"
"        border: none;\n"
"        border-left: 25px solid rgb(50, 56, 68);\n"
"        background-color: rgb(50, 56, 68);\n"
"        text-align: left;\n"
"        padding-left: 30px;\n"
"        color: rgb(169, 170, 172);\n"
"    }\n"
"    QPushButton:hover {\n"
"        background-color: rgb(33, 37, 43);\n"
"        border-left: 25px solid rgb(33, 37, 43);\n"
"    }\n"
"    QPushButton:pressed {\n"
"        background-color: rgb(85, 170, 255);\n"
"        border-left: 25px solid rgb(85, 170, 255);\n"
"    }")

        self.verticalLayout_19.addWidget(self.email_pb)


        self.horizontalLayout_13.addWidget(self.btn_frame_2, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.graph_view = QWidget(self.graph_frame)
        self.graph_view.setObjectName(u"graph_view")
        self.verticalLayout_15 = QVBoxLayout(self.graph_view)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, -1, 0, -1)
        self.horizontalFrame = QFrame(self.graph_view)
        self.horizontalFrame.setObjectName(u"horizontalFrame")
        self.horizontalFrame.setMinimumSize(QSize(0, 50))
        self.horizontalFrame.setMaximumSize(QSize(16777215, 50))
        self.horizontalFrame.setStyleSheet(u"QDialog{\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"	border-radius: 0px;\n"
"	font: 10pt \"MS Shell Dlg 2\";   \n"
"}\n"
"QLineEdit:hover{\n"
"	border: 1px solid  rgb(0, 120, 215);\n"
"}\n"
"QComboBox{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border: 1px solid rgb(204, 204, 204);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	font: 10pt \"MS Shell Dlg 2\";   \n"
"}\n"
"QComboBox:hover{\n"
"	border: 1px solid  rgb(0, 120, 215);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(0, 0, 0);	\n"
"	background-color: rgb(240, 240, 240);\n"
""
                        "	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"QLabel{\n"
"	font: 10pt \"MS Shell Dlg 2\";   \n"
"}\n"
"\n"
"")
        self.graph_tool = QHBoxLayout(self.horizontalFrame)
        self.graph_tool.setObjectName(u"graph_tool")
        self.graph_tool.setContentsMargins(9, -1, 9, -1)

        self.verticalLayout_15.addWidget(self.horizontalFrame)

        self.verticalFrame = QFrame(self.graph_view)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.graph = QVBoxLayout(self.verticalFrame)
        self.graph.setObjectName(u"graph")

        self.verticalLayout_15.addWidget(self.verticalFrame)


        self.verticalLayout_11.addWidget(self.graph_view)


        self.verticalLayout_6.addWidget(self.graph_frame)

        self.stackedWidget.addWidget(self.page_graph)
        self.page_setup = QWidget()
        self.page_setup.setObjectName(u"page_setup")
        self.verticalLayout_8 = QVBoxLayout(self.page_setup)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.page_setup)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy5.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy5)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setMinimumSize(QSize(700, 300))
        self.frame.setMaximumSize(QSize(500, 500))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(500, 70))
        self.label_8.setMaximumSize(QSize(500, 70))
        self.label_8.setStyleSheet(u"font: 34pt \"MS Shell Dlg 2\"; \n"
"color: rgb(169, 178, 200);\n"
"")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(500, 30))
        self.label_10.setMaximumSize(QSize(500, 30))
        self.label_10.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(169, 178, 200);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.browsefile = QLineEdit(self.frame_9)
        self.browsefile.setObjectName(u"browsefile")
        self.browsefile.setMinimumSize(QSize(341, 51))
        self.browsefile.setMaximumSize(QSize(500, 51))
        self.browsefile.setFocusPolicy(Qt.StrongFocus)
        self.browsefile.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}")
        self.browsefile.setFrame(False)

        self.horizontalLayout_11.addWidget(self.browsefile)

        self.btn_browse = QPushButton(self.frame_9)
        self.btn_browse.setObjectName(u"btn_browse")
        self.btn_browse.setMinimumSize(QSize(120, 51))
        self.btn_browse.setMaximumSize(QSize(120, 51))
        self.btn_browse.setFocusPolicy(Qt.NoFocus)
        self.btn_browse.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"background-color: rgb(72, 145, 217);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 127);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_browse)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.btn_save = QPushButton(self.frame)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(150, 50))
        self.btn_save.setFocusPolicy(Qt.NoFocus)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"background-color: rgb(72, 145, 217);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 127);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_save, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_setup)
        self.Email_setup = QWidget()
        self.Email_setup.setObjectName(u"Email_setup")
        self.verticalLayout_20 = QVBoxLayout(self.Email_setup)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_10 = QFrame(self.Email_setup)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 100, 71, 31))
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"color: rgb(169, 170, 172);")
        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(150, 170, 51, 31))
        self.label_20.setFont(font8)
        self.label_20.setStyleSheet(u"color: rgb(169, 170, 172);")
        self.email_send_pb = QPushButton(self.frame_10)
        self.email_send_pb.setObjectName(u"email_send_pb")
        self.email_send_pb.setGeometry(QRect(400, 250, 131, 51))
        self.email_send_pb.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"background-color: rgb(72, 145, 217);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(0, 255, 127);\n"
"}")
        self.recivers_email = QLineEdit(self.frame_10)
        self.recivers_email.setObjectName(u"recivers_email")
        self.recivers_email.setGeometry(QRect(230, 90, 500, 51))
        self.recivers_email.setMinimumSize(QSize(341, 51))
        self.recivers_email.setMaximumSize(QSize(500, 51))
        self.recivers_email.setFocusPolicy(Qt.StrongFocus)
        self.recivers_email.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}")
        self.recivers_email.setFrame(False)
        self.sendors_email = QLineEdit(self.frame_10)
        self.sendors_email.setObjectName(u"sendors_email")
        self.sendors_email.setGeometry(QRect(230, 160, 500, 51))
        self.sendors_email.setMinimumSize(QSize(341, 51))
        self.sendors_email.setMaximumSize(QSize(500, 51))
        self.sendors_email.setFocusPolicy(Qt.StrongFocus)
        self.sendors_email.setStyleSheet(u"QLineEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	color: rgb(169, 178, 200);\n"
"}")
        self.sendors_email.setFrame(False)

        self.verticalLayout_20.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.Email_setup)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font1)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.DataBase, self.ServerName)
        QWidget.setTabOrder(self.ServerName, self.emailfield)
        QWidget.setTabOrder(self.emailfield, self.From_Date)
        QWidget.setTabOrder(self.From_Date, self.From_Date_PB)
        QWidget.setTabOrder(self.From_Date_PB, self.From_Time)
        QWidget.setTabOrder(self.From_Time, self.passwordfield)
        QWidget.setTabOrder(self.passwordfield, self.To_Date)
        QWidget.setTabOrder(self.To_Date, self.To_Date_PB)
        QWidget.setTabOrder(self.To_Date_PB, self.To_Time)
        QWidget.setTabOrder(self.To_Time, self.colom_name)
        QWidget.setTabOrder(self.colom_name, self.Data_Table)
        QWidget.setTabOrder(self.Data_Table, self.browsefile)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"AT", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Project Number: xx-xxxx", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reporting Tool- By Xylem ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"User Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Sign in to your existing account", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.emailfield.setText("")
        self.emailfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passwordfield.setText("")
        self.passwordfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.error.setText("")
        self.login.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.create.setText(QCoreApplication.translate("MainWindow", u"Don't have an account? Create a new account", None))
        self.DataBase.setText("")
        self.DataBase.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Database Name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Server Name:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"DataBase:", None))
        self.ServerName.setText("")
        self.ServerName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Server Name", None))
        self.clear_PB.setText(QCoreApplication.translate("MainWindow", u"New Connection", None))
        self.Connect_PB.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"From Date", None))
        self.From_Date_PB.setText("")
        self.To_Date_PB.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"To Date", None))
        self.colom_name.setItemText(0, QCoreApplication.translate("MainWindow", u"All Fields", None))

        self.colom_name.setCurrentText(QCoreApplication.translate("MainWindow", u"All Fields", u"4"))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.Filter_PB.setText(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
        self.LoadAll_PB.setText(QCoreApplication.translate("MainWindow", u" Load All", None))
        self.Export_PB.setText(QCoreApplication.translate("MainWindow", u" Export To CSV", None))

        __sortingEnabled = self.Data_Table.isSortingEnabled()
        self.Data_Table.setSortingEnabled(False)
        self.Data_Table.setSortingEnabled(__sortingEnabled)

        self.From_Date_PB_G.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"From Date", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"To Date", None))
        self.To_Date_PB_G.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Variable", None))
        self.colom_name_G.setItemText(0, QCoreApplication.translate("MainWindow", u"All Fields", None))

        self.colom_name_G.setCurrentText(QCoreApplication.translate("MainWindow", u"All Fields", u"4"))
        self.Filter_PB_G.setText(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
        self.LoadAll_PB_G.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.email_pb.setText(QCoreApplication.translate("MainWindow", u"Send Email", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Browse Mapping File", None))
        self.browsefile.setText("")
        self.browsefile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Browse File", None))
        self.btn_browse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"From ", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.email_send_pb.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.recivers_email.setText("")
        self.recivers_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Recivers Email Id", None))
        self.sendors_email.setText("")
        self.sendors_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senders Email Id", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Xylem Inc.", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

