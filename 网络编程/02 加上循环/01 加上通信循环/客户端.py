#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 11:40

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议

phone.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>:').strip()
    phone.send(msg.encode('utf-8'))  # 客户端发送
    data = phone.recv(1024)  # 等待服务端数据
    print(data)

phone.close()
