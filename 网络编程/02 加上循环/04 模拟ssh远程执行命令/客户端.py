#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 11:40

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议

phone.connect(('127.0.0.1', 9900))

while True:
    # 1、发命令
    cmd = input('>>:').strip()
    if not cmd:
        continue
    phone.send(cmd.encode('gbk'))

    # 2、拿命令的结果，并打印
    data = phone.recv(1024)  # 1024是一个坑
    print(data.decode('gbk'))

phone.close()
