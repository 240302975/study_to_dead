#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 10:47

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议
phone.bind(('127.0.0.1', 8080))  # 0-65535:0-1024给操作系统使用
phone.listen(5)

print('starting...')
conn, client_addr = phone.accept()  # 等待客户端的connect
print(client_addr)  # 打印客户端的IP和端口

while True:  # 通信循环
    data = conn.recv(1024)  # recv等待收
    print('客户端的数据', data)

    conn.send(data.upper())  # send发送

conn.close()
phone.close()
