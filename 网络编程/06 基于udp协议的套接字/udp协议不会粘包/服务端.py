#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/9 21:00

# from socket import *
#
# server = socket(AF_INET, SOCK_DGRAM)  # 数据报协议UDP
# server.bind(('127.0.0.1', 8080))
#
# res1 = server.recvfrom(1024)
# print('第一次', res1)
#
# res2 = server.recvfrom(1024)
# print('第二次', res2)
#
# server.close()


from socket import *

server = socket(AF_INET, SOCK_DGRAM)  # 数据报协议UDP
server.bind(('127.0.0.1', 8080))

res1 = server.recvfrom(1)
# OSError: [WinError 10040] 一个在数据报套接字上发送的消息大于内部消息缓冲区或其他一些网络限制，或该用户用于接收数据报的缓冲区比数据报小。
print('第一次', res1)

res2 = server.recvfrom(1024)
print('第二次', res2)

server.close()
