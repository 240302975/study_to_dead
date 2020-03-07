#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 10:47

import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议
# print(phone)

# 2、绑定手机卡
phone.bind(('127.0.0.1', 8080))  # 0-65535:0-1024给操作系统使用

# 3、开机
phone.listen(5)  # 开始监听，5代表在允许有5个连接排队，更多的新连接连进来时就会被拒绝

# 4、等电话链接
print('starting...')
conn, client_addr = phone.accept()  # 接收链接，accept对应connect

# 5、收，发消息
data = conn.recv(1024)  # 1、单位：bytes 2、1024代表最大接受1024个字节
print('客户端的数据', data)

conn.send(data.upper())

# 6、挂电话
conn.close()

# 7、关机
phone.close()
