# -*- coding: utf-8 -*-

'a server example which send hello to client.'

import time, threading, socket


class server(object):
    """docstring for server."""

    info = {
        'admin': {
            'password': '6666',
            'isconnet': False,
            'socket': None,
        },

        'admin2': {
            'password': '8888',
            'isconnet': False,
            'socket': None,
        },

        'admin3': {
            'password': '8888',
            'isconnet': False,
            'socket': None,
        },

    }

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(('127.0.0.1', 8880))
        self.s.listen(10)
        print('Waiting for connection...')
        self.isconnet = False

    def Accept(self):
        print('Accept')
        sock, addr = self.s.accept()
        return sock, addr

    def Verify(self, sock):
        print('Verify')
        time.sleep(0.5)
        name = sock.recv(1024).decode('utf-8').strip()
        print(name, type(name))
        time.sleep(0.5)
        password = sock.recv(1024).decode('utf-8')
        print(password, type(password))

        if name not in self.info.keys():
            time.sleep(0.5)
            sock.send(bytes('Failed!', 'utf-8'))
            sock.close()
            return None

        elif password != self.info[name]['password']:
            time.sleep(0.5)
            sock.send(bytes('Failed!', 'utf-8'))
            sock.close()
            return None

        else:
            time.sleep(0.5)
            sock.send(bytes('Welcome!', 'utf-8'))
            self.info[name]['socket'] = sock
            self.info[name]['isconnet'] = True

        return name

    # def FindChatObject(self, sock):
    #     print('FindChatObject')
    #     print('----------------\n', sock, '----------------\n')
    #     time.sleep(0.5)
    #     receiver = sock.recv(1024).decode('utf-8').strip()
    #     print('receiver:', receiver)
    #     for key in self.info.keys():
    #         print('key:', key)
    #         print(self.info[key]['socket'])
    #         if self.info[key]['socket'] and self.info[key]['socket'] == sock:
    #             sender = key
    #     # return self.info[sender]['socket'],self.info[receiver]['socket']
    #     # print (sender,receiver)
    #     return sender, receiver


    def sendToEveryone(self, str):
        for each in self.info.keys():
            if self.info[each]["isconnet"]:
                try:
                    tmpSock = self.info[each]["socket"]
                    tmpSock.send(bytes(str, "utf-8"))
                except BaseException as ex:
                    print(ex)
                    self.info[each]["isconnet"] = False
                    del self.info[each]["socket"]
                    self.info[each]["socket"] = None


    def TransferStation(self, sock, addr):
        print('Accept new connection from %s:%s...' % addr)
        time.sleep(2)
        print('----------------\n', sock, '----------------\n')

        # send_name, recv_name = self.FindChatObject(sock)
        # sender = self.info[send_name]['socket']
        # receiver = self.info[recv_name]['socket']
        try:
            while True:
                time.sleep(0.5)
                data = sock.recv(1024).decode('utf-8')
                print(data)  #
                self.sendToEveryone(threading.current_thread().getName() + ":\n"+data)
        except BaseException as ex:
            print(ex)
            self.info[threading.current_thread().getName()]["isconnet"] = False
            del self.info[threading.current_thread().getName()]["socket"]
            self.info[threading.current_thread().getName()]["socket"] = None
            # if data == 'exit':
            #     break
            # if not data:
            #     continue

            # time.sleep(0.5)
            # receiver.send(bytes(data, 'utf-8'))

        # sender.close()

        # for key in self.info.keys():
            # if self.info[key]['socket'] == sock:
            #     del self.info[key]['socket']

        print('Connection from %s:%s closed.' % addr)




        # sock, addr = s.accept()
        # 因为只发送了一次 s.connect 所以如果接着马上再次调用sock, addr = s.accept() 会无效


if __name__ == '__main__':
    aserver = server()
    cnt = 0
    while True:
        cnt += 1
        print(cnt)
        time.sleep(5)
        sock, addr = aserver.Accept()
        sender = aserver.Verify(sock)
        print('------main------\n', sock, '-------main-----\n')

        if sender is not None and sender in aserver.info.keys() and aserver.info[sender]['isconnet']:
            # 创建新线程来处理TCP连接:
            print(aserver.info)
            th = threading.Thread(target=aserver.TransferStation, args=(sock, addr))
            th.setName(sender)
            th.start()