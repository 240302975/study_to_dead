#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/7 10:47

import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口重用
phone.bind(('127.0.0.1', 8081))
phone.listen(1)

print('starting...')
conn, client_addr = phone.accept()
print(client_addr)

while True:
    try:
        data = conn.recv(1024)
        # if not data:
        #     break  # 适用于linux操作系统
        print('客户端的数据', data)

        conn.send(data.upper())
    except ConnectionResetError:  # 适用于windows操作系统
        break
conn.close()
phone.close()
