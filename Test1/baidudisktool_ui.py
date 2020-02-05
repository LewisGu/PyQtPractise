# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baidudisktool_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 123)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 30, 471, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButtonBaiduOpen = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonBaiduOpen.setObjectName("pushButtonBaiduOpen")
        self.horizontalLayout.addWidget(self.pushButtonBaiduOpen)
        self.pushButtonBaiduCopy = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonBaiduCopy.setObjectName("pushButtonBaiduCopy")
        self.horizontalLayout.addWidget(self.pushButtonBaiduCopy)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 23))
        self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "优雅的百度网盘工具"))
        self.label.setText(_translate("MainWindow", "http://pan.baidu.com/s/"))
        self.pushButtonBaiduOpen.setText(_translate("MainWindow", "打开链接"))
        self.pushButtonBaiduCopy.setText(_translate("MainWindow", "复制链接"))
