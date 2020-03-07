#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 15:38

import socket
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9903))
server.listen(5)

conn, addr = server.accept()  # 建立连接

# 第一次接收
res1 = conn.recv(1)  # b'hello'
print('第一次', res1)

# 第二次接收
res2 = conn.recv(1024)
print('第二次', res2)
