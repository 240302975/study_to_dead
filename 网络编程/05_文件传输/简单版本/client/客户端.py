#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/8 16:50

import socket
import struct
import json

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于网络通信，基于TCP协议

phone.connect(('127.0.0.1', 9909))

while True:
    # 1、发命令
    cmd = input('>>:').strip()  # get a.txt
    if not cmd:
        continue
    phone.send(cmd.encode('gbk'))

    # 2、以写的方式打开一个新文件，接收服务端发来的文件的内容写入客户的新文件
    # 第一步:先收报头
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_bytes = phone.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息（数据长度）
    header_json = header_bytes.decode('gbk')
    header_dic = json.loads(header_json)
    '''
                header_dic = {
                'filename': filename,  # 'filename':'a.txt'
                'md5': 'xxdxxx',
                'file_size': os.path.filename  # 获取文件大小
            }
    '''
    print(header_dic)
    total_size = header_dic['file_size']
    filename = header_dic['filename']

    # 第四步：接收真实的数据
    with open(filename, 'wb')as f:
        recv_size = 0
        while recv_size < total_size:
            line = phone.recv(1024)  # 1024是一个坑
            f.write(line)
            recv_size += len(line)
            print('总大小：%s 已下载大小：%s' % (total_size, recv_size))

phone.close()
