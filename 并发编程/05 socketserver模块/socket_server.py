#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/14 20:05

import socketserver

'''
socketserver使用模式：

1 功能类
    class Myserver(socketserver.BaseRequestHandler)
        def handle(self):
            pass
2   server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888),Myserver)
3   server.serve_forever()
'''


class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        """
        并发的业务逻辑
        conn:
        :return:
        """
        while 1:  # 持续发送消息
            client_data = self.request.recv(1024)
            print(client_data.decode('utf-8'))
            if client_data.decode('utf-8') == 'exit':
                print('客户端断开连接，等待新的用户连接...')
                break
            print('接受数据>>>', str(client_data, 'utf-8'))
            response = input('响应数据>>>')
            self.request.sendall(bytes(response, 'utf-8'))
        self.request.close()


# 1 self.socket  2 self.socket.bind()  3 self.socket.listen(5)
server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), Myserver)
server.serve_forever()
