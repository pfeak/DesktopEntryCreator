# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.move(
            (QtWidgets.QApplication.desktop().width() - mainWindow.width()) / 2,
            (QtWidgets.QApplication.desktop().height() - mainWindow.height()) / 2,
        )
        mainWindow.resize(320, 200)
        mainWindow.setMinimumSize(QtCore.QSize(320, 200))
        mainWindow.setMaximumSize(QtCore.QSize(320, 200))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Exec = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Exec.setObjectName("lineEdit_Exec")
        self.gridLayout.addWidget(self.lineEdit_Exec, 3, 1, 1, 1)
        self.toolButton_Exec = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_Exec.setObjectName("toolButton_Exec")
        self.gridLayout.addWidget(self.toolButton_Exec, 3, 2, 1, 1)
        self.toolButton_Icon = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_Icon.setObjectName("toolButton_Icon")
        self.gridLayout.addWidget(self.toolButton_Icon, 4, 2, 1, 1)
        self.label_Icon = QtWidgets.QLabel(self.centralwidget)
        self.label_Icon.setObjectName("label_Icon")
        self.gridLayout.addWidget(self.label_Icon, 4, 0, 1, 1)
        self.label_Name = QtWidgets.QLabel(self.centralwidget)
        self.label_Name.setObjectName("label_Name")
        self.gridLayout.addWidget(self.label_Name, 3, 0, 1, 1)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.gridLayout.addWidget(self.lineEdit_Name, 1, 1, 1, 1)
        self.label_Command = QtWidgets.QLabel(self.centralwidget)
        self.label_Command.setObjectName("label_Command")
        self.gridLayout.addWidget(self.label_Command, 5, 0, 1, 1)
        self.label_Exec = QtWidgets.QLabel(self.centralwidget)
        self.label_Exec.setObjectName("label_Exec")
        self.gridLayout.addWidget(self.label_Exec, 1, 0, 1, 1)
        self.lineEdit_Icon = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Icon.setObjectName("lineEdit_Icon")
        self.gridLayout.addWidget(self.lineEdit_Icon, 4, 1, 1, 1)
        self.lineEdit_Command = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Command.setObjectName("lineEdit_Command")
        self.gridLayout.addWidget(self.lineEdit_Command, 5, 1, 1, 1)
        self.pushButton_Create = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Create.setObjectName("pushButton_Create")
        self.gridLayout.addWidget(self.pushButton_Create, 6, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Create ShortCut"))
        self.toolButton_Exec.setText(_translate("mainWindow", "..."))
        self.toolButton_Icon.setText(_translate("mainWindow", "..."))
        self.label_Icon.setText(_translate("mainWindow", "Icon"))
        self.label_Name.setText(_translate("mainWindow", "Exec"))
        self.label_Command.setText(_translate("mainWindow", "Command"))
        self.label_Exec.setText(_translate("mainWindow", "Name"))
        self.pushButton_Create.setText(_translate("mainWindow", "Create"))
