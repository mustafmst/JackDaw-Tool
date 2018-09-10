# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JackDawTool/gui/MainWindowLayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 693)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelZookeeper = QtWidgets.QLabel(self.centralwidget)
        self.labelZookeeper.setObjectName("labelZookeeper")
        self.verticalLayout_3.addWidget(self.labelZookeeper)
        self.lineEditZookeeper = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditZookeeper.setObjectName("lineEditZookeeper")
        self.verticalLayout_3.addWidget(self.lineEditZookeeper)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelBrokers = QtWidgets.QLabel(self.centralwidget)
        self.labelBrokers.setObjectName("labelBrokers")
        self.verticalLayout_5.addWidget(self.labelBrokers)
        self.lineEditBrokers = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditBrokers.setObjectName("lineEditBrokers")
        self.verticalLayout_5.addWidget(self.lineEditBrokers)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.buttonConnect = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.buttonConnect.sizePolicy().hasHeightForWidth())
        self.buttonConnect.setSizePolicy(sizePolicy)
        self.buttonConnect.setObjectName("buttonConnect")
        self.verticalLayout_4.addWidget(self.buttonConnect)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        self.horizontalLayout_2.addWidget(self.treeWidget)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 826, 30))
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
        self.lineEditZookeeper.setText(_translate("MainWindow", "localhost:2181"))
        self.labelBrokers.setText(_translate("MainWindow", "Brokers:"))
        self.lineEditBrokers.setText(_translate("MainWindow", "localhost:9092"))
        self.buttonConnect.setText(_translate("MainWindow", "Connect"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Topics"))

