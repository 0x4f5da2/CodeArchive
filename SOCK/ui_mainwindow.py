# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 615)
        MainWindow.setStyleSheet("background-color:#FCFCFC")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(20, 20, 341, 531))
        self.listView.setStyleSheet("    background-color: #FFFFFF;\n"
                                    "    color:#5E5E5E;\n"
                                    "    font: bold 15px;\n"
                                    "    border-radius:10px;\n"
                                    "border-style: solid;\n"
                                    "    border-width: 1px;\n"
                                    "    border-color: #929292;")
        self.listView.setObjectName("listView")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 563, 341, 40))
        self.lineEdit.setStyleSheet("    border-style: solid;\n"
                                    "    border-width: 1px;\n"
                                    "    border-color: #929292;\n"
                                    "    background-color: #FFFFFF;\n"
                                    "    color:#5E5E5E;\n"
                                    "    border-radius:10px;\n"
                                    "    font: bold 15px;\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;")
        self.lineEdit.setObjectName("lineEdit")
        self.sendButton = QtWidgets.QPushButton(self.centralWidget)
        self.sendButton.setGeometry(QtCore.QRect(295, 568, 61, 30))
        self.sendButton.setStyleSheet("\n"
                                      "QPushButton{\n"
                                      "    background-color: #4EC4F6;\n"
                                      "    color:white;\n"
                                      "    border-radius: 10px;\n"
                                      "    font: bold 15px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    color:white;\n"
                                      "    background-color: #1793C5\n"
                                      "}")
        self.sendButton.setObjectName("sendButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sendButton.setText(_translate("MainWindow", "send"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
