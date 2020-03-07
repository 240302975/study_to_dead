#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/9 21:00

from socket import *

client = socket(AF_INET, SOCK_DGRAM)  # 数据报协议UDP

while True:
    msg = input('>>:').strip()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 8080))  # 数据bytes格式，ip地址以及端口，发给服务端

    data, server_addr = client.recvfrom(1024)
    print(data, server_addr)
client.close()
# 一个sendto对应一个resv
