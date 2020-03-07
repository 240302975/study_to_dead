#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 15:38

import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议

client.connect(('127.0.0.1', 9903))


client.send('hello'.encode('utf-8'))
# time.sleep(5)  # 去掉的话会粘包
client.send('world'.encode('utf-8'))
