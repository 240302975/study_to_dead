#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/6 13:46

from socket import *
from multiprocessing import Process


def talk(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


def server(ip, port):
    # 初始化
    server = socket(AF_INET, SOCK_STREAM)  # 基于TCP
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 重用IP和端口
    server.bind((ip, port))
    server.listen(5)

    while True:
        conn, addr = server.accept()  # 建立链接
        p = Process(target=talk, args=(conn,))
        p.start()  # 起进程
    server.close()


if __name__ == '__main__':
    server('127.0.0.1', 8080)
