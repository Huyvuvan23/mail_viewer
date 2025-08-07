# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'email_viewerDtTycB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject,  QSize, Qt)
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(939, 800)
        MainWindow.setStyleSheet(u"/* Main window style */\n"
"QMainWindow {\n"
"    background-color: #FAFAFA;\n"
"    color: #000;\n"
"}\n"
"\n"
"/* General widget styles */\n"
"QWidget {\n"
"    font-family: 'Meiryo UI', sans-serif;\n"
"    font-size: 10pt;\n"
"    selection-background-color: #6A9EDB;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Group boxes */\n"
"QGroupBox {\n"
"    border: 1px solid #D8D8D8;\n"
"    border-radius: 6px;\n"
"	margin-bottom:8px;\n"
"    padding-top: 15px;\n"
"    padding-bottom: 8px;\n"
"    padding-left: 8px;\n"
"    padding-right: 8px;\n"
"    background-color: #F5F5F5;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 12px;\n"
"    padding: 2px 6px;\n"
"    margin-top: 3px;\n"
"    margin-left: 0px;\n"
"    background-color: transparent;\n"
"    color: #000;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Buttons */\n"
"QPushButton {\n"
"    background-color: #EDEDED;\n"
"    border: 1px solid #D0D0D0;\n"
"    border-radius: 4px;\n"
"    padding: 5px 12px;\n"
"	margin-top:"
                        " 5px;\n"
"    min-width: 80px;\n"
"    color: #444444;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #E5E5E5;\n"
"    border-color: #C0C0C0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #D8D8D8;\n"
"    border-color: #B0B0B0;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #F0F0F0;\n"
"    color: #A0A0A0;\n"
"}\n"
"\n"
"/* List widgets */\n"
"QListWidget {\n"
"    background-color: #F0F0F0;\n"
"    border: 1px solid #D8D8D8;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"	margin-top: 10px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 6px 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #E8E8E8;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #6A9EDB;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Text browsers and editors */\n"
"QTextBrowser, QTextEdit {\n"
"    background-color: #F5F5F5;\n"
"    border: 1px solid #D8D8D8;\n"
"    border-radius: 4px;\n"
"    paddi"
                        "ng: 4px;\n"
"	margin-top:10px;\n"
"    selection-background-color: #6A9EDB;\n"
"    selection-color: white;\n"
"    font-family: 'Meiryo UI', Arial, sans-serif;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"/* Scroll bars */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #F0F0F0;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #C8C8C8;\n"
"    min-height: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #F0F0F0;\n"
"    height: 10px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #C8C8C8;\n"
"    min-width: 20px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    widt"
                        "h: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/* Splitter */\n"
"QSplitter::handle {\n"
"    background-color: #E0E0E0;\n"
"    width: 4px;\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background-color: #D0D0D0;\n"
"}\n"
"\n"
"/* Tooltips */\n"
"QToolTip {\n"
"    background-color: #4A4A4A;\n"
"    color: #F0F0F0;\n"
"    border: 1px solid #5A5A5A;\n"
"    border-radius: 4px;\n"
"    padding: 4px 8px;\n"
"}\n"
"\n"
"/* Header text specific style */\n"
"#headerText {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Content browser specific style */\n"
"#contentBrowser {\n"
"    padding: 8px;\n"
"}\n"
"\n"
"/* Mail list specific style */\n"
"#mailList {\n"
"    background-color: #F0F0F0;\n"
"}\n"
"\n"
"#create_button {\n"
"    background-color: rgb(24, 155, 255);\n"
"	color:rgb(255, 255, 255);\n"
"	font-size:18px;\n"
"	font-weight:bold;\n"
"	min-height:20px;\n"
"}\n"
"\n"
"#create_button::hover {\n"
"    background-color: rgb(17, 112"
                        ", 180);\n"
"}\n"
"\n"
"#create_button::pressed {\n"
"    background-color: rgb(21, 141, 226);\n"
"}\n"
"\n"
"#change_link{\n"
"	min-width:20px;\n"
"	padding: 2px 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.leftPanel = QWidget(self.splitter)
        self.leftPanel.setObjectName(u"leftPanel")
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.folderGroup = QGroupBox(self.leftPanel)
        self.folderGroup.setObjectName(u"folderGroup")
        self.verticalLayout_3 = QVBoxLayout(self.folderGroup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnLoadFolder = QPushButton(self.folderGroup)
        self.btnLoadFolder.setObjectName(u"btnLoadFolder")
        icon = QIcon()
        icon.addFile(u":/icons/folder", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLoadFolder.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.btnLoadFolder)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.change_link = QPushButton(self.folderGroup)
        self.change_link.setObjectName(u"change_link")

        self.horizontalLayout_2.addWidget(self.change_link)

        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 12)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.folderList = QListWidget(self.folderGroup)
        self.folderList.setObjectName(u"folderList")
        self.folderList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_3.addWidget(self.folderList)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 11)

        self.verticalLayout_2.addWidget(self.folderGroup)

        self.mailListGroup = QGroupBox(self.leftPanel)
        self.mailListGroup.setObjectName(u"mailListGroup")
        self.verticalLayout_4 = QVBoxLayout(self.mailListGroup)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mailList = QListWidget(self.mailListGroup)
        self.mailList.setObjectName(u"mailList")
        self.mailList.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_4.addWidget(self.mailList)


        self.verticalLayout_2.addWidget(self.mailListGroup)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.splitter.addWidget(self.leftPanel)
        self.rightPanel = QWidget(self.splitter)
        self.rightPanel.setObjectName(u"rightPanel")
        self.verticalLayout = QVBoxLayout(self.rightPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerGroup = QGroupBox(self.rightPanel)
        self.headerGroup.setObjectName(u"headerGroup")
        self.verticalLayout_5 = QVBoxLayout(self.headerGroup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.headerText = QTextEdit(self.headerGroup)
        self.headerText.setObjectName(u"headerText")
        self.headerText.setReadOnly(True)

        self.verticalLayout_5.addWidget(self.headerText)


        self.verticalLayout.addWidget(self.headerGroup)

        self.contentGroup = QGroupBox(self.rightPanel)
        self.contentGroup.setObjectName(u"contentGroup")
        self.verticalLayout_6 = QVBoxLayout(self.contentGroup)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.contentBrowser = QTextBrowser(self.contentGroup)
        self.contentBrowser.setObjectName(u"contentBrowser")
        self.contentBrowser.setOpenExternalLinks(True)
        self.contentBrowser.setOpenLinks(True)

        self.verticalLayout_6.addWidget(self.contentBrowser)


        self.verticalLayout.addWidget(self.contentGroup)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.create_button = QPushButton(self.rightPanel)
        self.create_button.setObjectName(u"create_button")

        self.horizontalLayout_3.addWidget(self.create_button)

        self.horizontalLayout_3.setStretch(0, 8)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 1)
        self.splitter.addWidget(self.rightPanel)

        self.horizontalLayout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Email Viewer (.MSG)", None))
        self.folderGroup.setTitle(QCoreApplication.translate("MainWindow", u"Mail Folders", None))
        self.btnLoadFolder.setText(QCoreApplication.translate("MainWindow", u"Load Folder", None))
        self.change_link.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.mailListGroup.setTitle(QCoreApplication.translate("MainWindow", u"Email List", None))
        self.headerGroup.setTitle(QCoreApplication.translate("MainWindow", u"Email Header", None))
        self.headerText.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Meiryo UI','Arial','sans-serif'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Segoe UI'; font-size:9pt;\"><br /></p></body></html>", None))
        self.contentGroup.setTitle(QCoreApplication.translate("MainWindow", u"Email Content Preview", None))
        self.create_button.setText(QCoreApplication.translate("MainWindow", u"Create", None))
    # retranslateUi

