# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './JackDawTool/gui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


def createActionHandler(action):
    return lambda _: action()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("JackDaw-Tool")
        MainWindow.resize(861, 636)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelZookeeper = QtWidgets.QLabel(self.centralwidget)
        self.labelZookeeper.setObjectName("labelZookeeper")
        self.verticalLayout.addWidget(self.labelZookeeper)
        self.lineEditZookeeper = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditZookeeper.setObjectName("lineEditZookeeper")
        self.verticalLayout.addWidget(self.lineEditZookeeper)
        self.labelBrokers = QtWidgets.QLabel(self.centralwidget)
        self.labelBrokers.setObjectName("labelBrokers")
        self.verticalLayout.addWidget(self.labelBrokers)
        self.lineEditBrokers = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBrokers.setObjectName("lineEditBrokers")
        self.verticalLayout.addWidget(self.lineEditBrokers)
        self.labelTopic = QtWidgets.QLabel(self.centralwidget)
        self.labelTopic.setObjectName("labelTopic")
        self.verticalLayout.addWidget(self.labelTopic)
        self.lineEditTopic = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTopic.setObjectName("lineEditTopic")
        self.verticalLayout.addWidget(self.lineEditTopic)
        self.buttoneConnect = QtWidgets.QPushButton(self.centralwidget)
        self.buttoneConnect.setObjectName("buttoneConnect")
        self.verticalLayout.addWidget(self.buttoneConnect)
        self.messages = QtWidgets.QTextBrowser(self.centralwidget)
        self.messages.setObjectName("messages")
        self.verticalLayout.addWidget(self.messages)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "JackDaw-Tool"))
        self.labelZookeeper.setText(_translate("MainWindow", "Zookeeper:"))
        self.labelBrokers.setText(_translate("MainWindow", "Brokers:"))
        self.labelTopic.setText(_translate("MainWindow", "Topic:"))
        self.buttoneConnect.setText(_translate("MainWindow", "Connect"))

    def setActions(self, action):
        self.buttoneConnect.clicked.connect(createActionHandler(action))
