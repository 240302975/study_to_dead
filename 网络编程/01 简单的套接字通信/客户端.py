#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 11:40

import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议
# print(phone)

# 2、拨号
phone.connect(('127.0.0.1', 8080))

# 3、发，收消息
phone.send('hello'.encode('utf-8'))
data = phone.recv(1024)
print(data)

# 4、关闭
phone.close()
