# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ss.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 220)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(220, 220))
        MainWindow.setMaximumSize(QtCore.QSize(220, 220))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_ss = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ss.setGeometry(QtCore.QRect(20, 10, 181, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ss.setFont(font)
        self.btn_ss.setStyleSheet("background-color:rgb(255, 85, 0);\n"
"border-radius:50px;\n"
"box-shadow: 10px 10px;")
        self.btn_ss.setObjectName("btn_ss")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 220, 26))
        self.menubar.setObjectName("menubar")
        self.menuPath = QtWidgets.QMenu(self.menubar)
        self.menuPath.setObjectName("menuPath")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_path = QtWidgets.QAction(MainWindow)
        self.action_path.setObjectName("action_path")
        self.menuPath.addAction(self.action_path)
        self.menubar.addAction(self.menuPath.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SS"))
        self.btn_ss.setText(_translate("MainWindow", "S H O T ! ! !"))
        self.menuPath.setTitle(_translate("MainWindow", "PATH AREA"))
        self.action_path.setText(_translate("MainWindow", "WHATS PATH"))
