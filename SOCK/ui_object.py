# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'object.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Object(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Object, self).__init__()
        self.setupUi(self)

    def setupUi(self, Object):
        Object.setObjectName("Object")
        Object.resize(300, 400)
        Object.setStyleSheet("background-color:#FCFCFC")
        self.objectbox = QtWidgets.QLineEdit(Object)
        self.objectbox.setGeometry(QtCore.QRect(40, 190, 220, 40))
        self.objectbox.setStyleSheet("QLineEdit{\n"
                                     "    border-style: solid;\n"
                                     "    border-width: 1px;\n"
                                     "    border-color: #929292;\n"
                                     "    background-color: #FFFFFF;\n"
                                     "    color:#5E5E5E;\n"
                                     "    border-radius: 5px;\n"
                                     "    font: bold 15px;\n"
                                     "    min-width: 10em;\n"
                                     "    padding: 6px;\n"
                                     "}")
        self.objectbox.setObjectName("objectbox")
        self.startconv = QtWidgets.QPushButton(Object)
        self.startconv.setEnabled(True)
        self.startconv.setGeometry(QtCore.QRect(40, 290, 220, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startconv.sizePolicy().hasHeightForWidth())
        self.startconv.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.startconv.setFont(font)
        self.startconv.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startconv.setStyleSheet("QPushButton{\n"
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
        self.startconv.setAutoDefault(False)
        self.startconv.setDefault(False)
        self.startconv.setFlat(False)
        self.startconv.setObjectName("startconv")
        self.label_2 = QtWidgets.QLabel(Object)
        self.label_2.setGeometry(QtCore.QRect(42, 100, 211, 41))
        self.label_2.setStyleSheet("font:20px;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Object)
        self.label.setGeometry(QtCore.QRect(40, 40, 171, 71))
        self.label.setStyleSheet("font:bold 40px;\n"
                                 "")
        self.label.setObjectName("label")

        self.retranslateUi(Object)
        # self.startconv.clicked.connect(Object.accept)
        QtCore.QMetaObject.connectSlotsByName(Object)

    def retranslateUi(self, Object):
        _translate = QtCore.QCoreApplication.translate
        Object.setWindowTitle(_translate("Object", "Dialog"))
        self.objectbox.setPlaceholderText(_translate("Object", "您想和谁聊天？"))
        self.startconv.setText(_translate("Object", "开始聊天"))
        self.label_2.setText(_translate("Object", "in touch with friends"))
        self.label.setText(_translate("Object", "Stay"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Object = QtWidgets.QDialog()
    ui = Ui_Object()
    ui.setupUi(Object)
    Object.show()
    sys.exit(app.exec_())
