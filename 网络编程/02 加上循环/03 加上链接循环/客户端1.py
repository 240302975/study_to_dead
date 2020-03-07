#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 11:40

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议

phone.connect(('127.0.0.1', 8081))

while True:
    msg = input('>>:').strip()  # msg = ''
    if not msg:
        continue
    phone.send(msg.encode('utf-8'))  # phone.send(b'')
    # print('has send')
    data = phone.recv(1024)
    # print('has rcv')
    print(data.decode('utf-8'))

phone.close()
