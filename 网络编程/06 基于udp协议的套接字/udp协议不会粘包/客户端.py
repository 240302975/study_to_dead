#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/9 21:00

from socket import *

client = socket(AF_INET, SOCK_DGRAM)  # 数据报协议UDP

client.sendto(b'hello', ('127.0.0.1', 8080))
client.sendto(b'word', ('127.0.0.1', 8080))

client.close()
