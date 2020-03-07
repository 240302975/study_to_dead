#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/9 21:00

from socket import *

server = socket(AF_INET, SOCK_DGRAM)  # 数据报协议UDP
server.bind(('127.0.0.1', 8080))

while True:
    data, client_addr = server.recvfrom(1024)
    print(data)
    server.sendto(data.upper(), client_addr)
server.close()
