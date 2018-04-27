# -*- coding: utf-8 -*-

import time, socket, threading, sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from ui_box import Ui_Box
from ui_object import Ui_Object
from ui_mainwindow import Ui_MainWindow

SIZE = 1024


class Client(object):
    def __init__(self):
        self.isClientConnect = False
        self.app = QtWidgets.QApplication(sys.argv)
        # self.gui = Gui()
        # self.gui.Box.show()
        self.box = Ui_Box()  # 对Ui_Box做了一些改动
        self.box.loginbutton.clicked.connect(self.loginBtnCliecked)  #
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.sendButton.clicked.connect(self.sendBtnClicked)

    def sendBtnClicked(self):
        try:
            self.s.send(bytes(self.mainWindow.lineEdit.text(), 'utf-8'))
            self.mainWindow.lineEdit.setText("")
        except BaseException as ex:
            print(ex)
            QtWidgets.QMessageBox.critical(QtWidgets.QMessageBox(), "登录错误", "无法登陆到服务器，请检查账号密码以及网络连接")

    def loginBtnCliecked(self):
        try:
            self.ConnectServer()
            time.sleep(0.5)
            self.login_client()
        except BaseException as e:
            QtWidgets.QMessageBox.critical(QtWidgets.QMessageBox(), "错误", str(e))
            return
        if(self.isClientConnect):
            self.box.hide()
            self.chat()
        else:
            QtWidgets.QMessageBox.critical(QtWidgets.QMessageBox(), "登录错误", "无法登陆到服务器，请检查账号密码以及网络连接")



    def ConnectServer(self):
        print('ConnectServer')
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(('127.0.0.1', 8880))

    def login_client(self):
        print('C_login_client')
        # --------------出问题------------------
        self.name = self.box.name.text()
        self.password = self.box.password.text()
        # --------------出问题------------------
        print(self.name, self.password)
        time.sleep(0.5)
        self.s.send(bytes(self.name, 'utf-8'))
        print('sended')
        time.sleep(0.5)
        self.s.send(bytes(self.password, 'utf-8'))
        receive = self.s.recv(SIZE).decode('utf-8')
        print(receive)

        if receive == 'Welcome!':
            self.isClientConnect = True

    # def ChatObject(self):
    #     print('ChatObjectClient')
    #     self.chatobject = input('who do you want to chat:')
    #     time.sleep(0.5)
        # self.s.send(bytes(name, 'utf-8'))

    def chat(self):
        self.mainWindow.show()

        def ReceiveMessage():
            model = QtGui.QStandardItemModel(self.mainWindow.listView)
            while True:
                try:
                    # time.sleep(0.5)
                    mesg = self.s.recv(SIZE).decode('utf-8')
                    tmp = QtGui.QStandardItem()
                    tmp.setText(mesg)
                    model.appendRow(tmp)
                    self.mainWindow.listView.setModel(model)
                    self.mainWindow.listView.update()
                except socket.error:
                    break
        subtrecv = threading.Thread(target=ReceiveMessage, args=())
        subtrecv.setDaemon(True)
        subtrecv.start()

        print('----------- Chat Ends -----------')





if __name__ == '__main__':


    a = Client()
    a.box.show()
    sys.exit(a.app.exec_())

    # a.login_client()
    # if a.isClientConnect == True:
    #     a.chat()
