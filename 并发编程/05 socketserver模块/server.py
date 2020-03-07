#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/14 11:08

from socket import *

ip_port = ('127.0.0.1', 8888)
tcp_socket_server = socket()
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)  # 最大连接数

while 1:  # 服务端持续等待链接
    conn, addr = tcp_socket_server.accept()
    print('客户端', addr)
    while 1:  # 持续发送消息
        client_data = conn.recv(1024)
        print(client_data.decode('utf-8'))
        if client_data.decode('utf-8') == 'exit':
            print('客户端断开连接，等待新的用户连接...')
            break
        print('接受数据>>>', str(client_data, 'utf-8'))
        response = input('响应数据>>>')
        conn.sendall(bytes(response, 'utf-8'))
    conn.close()
