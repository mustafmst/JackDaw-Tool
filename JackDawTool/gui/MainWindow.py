# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './JackDawTool/gui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets



class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        self.window = MainWindow
        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.menubar = QtWidgets.QMenuBar(self.window)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.messages = QtWidgets.QTextBrowser(self.centralwidget)
        self.buttoneConnect = QtWidgets.QPushButton(self.centralwidget)
        self.lineEditTopic = QtWidgets.QLineEdit(self.centralwidget)
        self.labelTopic = QtWidgets.QLabel(self.centralwidget)
        self.lineEditBrokers = QtWidgets.QLineEdit(self.centralwidget)
        self.labelBrokers = QtWidgets.QLabel(self.centralwidget)
        self.lineEditZookeeper = QtWidgets.QLineEdit(self.centralwidget)
        self.labelZookeeper = QtWidgets.QLabel(self.centralwidget)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

    def setupUi(self):
        self.window.setObjectName("JackDaw-Tool")
        self.window.resize(861, 636)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelZookeeper.setObjectName("labelZookeeper")
        self.verticalLayout.addWidget(self.labelZookeeper)
        self.lineEditZookeeper.setObjectName("lineEditZookeeper")
        self.verticalLayout.addWidget(self.lineEditZookeeper)
        self.labelBrokers.setObjectName("labelBrokers")
        self.verticalLayout.addWidget(self.labelBrokers)
        self.lineEditBrokers.setObjectName("lineEditBrokers")
        self.verticalLayout.addWidget(self.lineEditBrokers)
        self.labelTopic.setObjectName("labelTopic")
        self.verticalLayout.addWidget(self.labelTopic)
        self.lineEditTopic.setObjectName("lineEditTopic")
        self.verticalLayout.addWidget(self.lineEditTopic)
        self.buttoneConnect.setObjectName("buttoneConnect")
        self.verticalLayout.addWidget(self.buttoneConnect)
        self.messages.setObjectName("messages")
        self.verticalLayout.addWidget(self.messages)
        self.window.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 30))
        self.menubar.setObjectName("menubar")
        self.window.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)
        self.window.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "JackDaw-Tool"))
        self.labelZookeeper.setText(_translate("MainWindow", "Zookeeper:"))
        self.labelBrokers.setText(_translate("MainWindow", "Brokers:"))
        self.labelTopic.setText(_translate("MainWindow", "Topic:"))
        self.buttoneConnect.setText(_translate("MainWindow", "Connect"))

    def setActions(self, action):
        self.buttoneConnect.clicked.connect(self.createActionHandler(action))

    def createActionHandler(self, action):
        return lambda _: action(
            self.lineEditZookeeper.text(),
            self.lineEditBrokers.text(),
            self.lineEditTopic.text())

    def write_message(self, message):
        self.messages.setText(message);
