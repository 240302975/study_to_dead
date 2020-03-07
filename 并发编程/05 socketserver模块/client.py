#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/14 11:10

import socket

ip_port = ('127.0.0.1', 8888)
sock = socket.socket()
sock.connect(ip_port)
print('客户端启动：')

while True:
    inp = input('发送数据>>>')
    sock.sendall(bytes(inp, 'utf-8'))
    if inp == 'exit':
        break
    server_response = sock.recv(1024)
    print('服务端响应数据>>>', str(server_response, 'utf-8'))
sock.close()
