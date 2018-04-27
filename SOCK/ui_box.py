# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'box.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Box(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Box, self).__init__()
        self.setupUi(self)

    def setupUi(self, Box):
        Box.setObjectName("Box")
        Box.resize(300, 400)
        Box.setStyleSheet("background-color:#FCFCFC")
        self.loginbutton = QtWidgets.QPushButton(Box)
        self.loginbutton.setEnabled(True)
        self.loginbutton.setGeometry(QtCore.QRect(40, 290, 220, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginbutton.sizePolicy().hasHeightForWidth())
        self.loginbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loginbutton.setStyleSheet("QPushButton{\n"
                                       "    background-color: #4EC4F6;\n"
                                       "    color:white;\n"
                                       "    border-radius: 5px;\n"
                                       "    font: bold 15px;\n"
                                       "    min-width: 10em;\n"
                                       "    padding: 6px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color:white;\n"
                                       "    background-color: #1793C5\n"
                                       "}")
        self.loginbutton.setAutoDefault(False)
        self.loginbutton.setDefault(False)
        self.loginbutton.setFlat(False)
        self.loginbutton.setObjectName("loginbutton")
        self.name = QtWidgets.QLineEdit(Box)
        self.name.setGeometry(QtCore.QRect(40, 170, 220, 40))
        self.name.setStyleSheet("QLineEdit{\n"
                                "    border-style: solid;\n"
                                "    border-width: 1px;\n"
                                "    border-color: #929292;\n"
                                "    background-color: #FFFFFF;\n"
                                "    color:#5E5E5E;\n"
                                "    border-top-left-radius: 5px;\n"
                                "    border-top-right-radius: 5px;\n"
                                "    font: bold 15px;\n"
                                "    min-width: 10em;\n"
                                "    padding: 6px;\n"
                                "}")
        self.name.setObjectName("name")
        self.password = QtWidgets.QLineEdit(Box)
        self.password.setGeometry(QtCore.QRect(40, 209, 220, 40))
        self.password.setStyleSheet("QLineEdit{\n"
                                    "    border-style: solid;\n"
                                    "    border-width: 1px;\n"
                                    "    border-color: #929292;\n"
                                    "    background-color: #FFFFFF;\n"
                                    "    color:#5E5E5E;\n"
                                    "    border-bottom-left-radius: 5px;\n"
                                    "    border-bottom-right-radius: 5px;\n"
                                    "    font: bold 15px;\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}\n"
                                    "")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(Box)
        self.label.setGeometry(QtCore.QRect(40, 40, 171, 71))
        self.label.setStyleSheet("font:bold 40px;\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Box)
        self.label_2.setGeometry(QtCore.QRect(42, 100, 211, 41))
        self.label_2.setStyleSheet("font:20px;\n"
                                   "")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Box)
        # self.loginbutton.clicked.connect(Box.accept)
        QtCore.QMetaObject.connectSlotsByName(Box)

    def retranslateUi(self, Box):
        _translate = QtCore.QCoreApplication.translate
        Box.setWindowTitle(_translate("Box", "Dialog"))
        self.loginbutton.setText(_translate("Box", "登 录"))
        self.name.setPlaceholderText(_translate("Box", "账号"))
        self.password.setPlaceholderText(_translate("Box", "密码"))
        self.label.setText(_translate("Box", "Hello"))
        self.label_2.setText(_translate("Box", "Nice to see you again"))

    def showMessageWarning(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Box = QtWidgets.QDialog()
    ui = Ui_Box()
    ui.setupUi(Box)
    Box.show()
    sys.exit(app.exec_())
