#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:31

import os

BASE_DIR = os.path.normpath(os.path.join(__file__, '..', '..'))

FILES_PATH = os.path.join(BASE_DIR, 'files')
UNFINISHED_DOWNLOAD_FILES_PATH = os.path.join(FILES_PATH, '.download', 'unfinished.shv')

HOST = '127.0.0.1'
PORT = 8080


help_dic = {
    'ls --help': """
            查看当前目录下的文件:
                ls
            指定目录下的文件(只能查看到自己家目录的范围):
                ls /目录1/目录2
            查看ls的详细帮助:
                ls /?
            """,
    'cd --help': """
            相对路径切换:
                cd /目录1
                    cd /目录2
            绝对路径切换:
                cd /目录1/目录2
            切换到上一层目录:
                cd ..
            在当前目录下切当前目录:
                cd .
            """,
    'mkdir --help': """
            相对路径创建:
                mkdir /目录
            生成多层递归目录:
                mkdir /目录1/目录2
            """,
    'rmdir --help': """
            删除空目录:
                rmdir /目录1/空目录2
            """,
    'remove --help': """
            删除文件:
                remove /目录1/文件
            """,
    'upload --help': """
            上传到服务端当前路径:
                upload 文件名
            通过cd切换目录上传文件到该目录下:
                cd /目录1/目录2
                    upload 文件
            """,
    'resume_upload --help': """
                继续上传文件到服务端当前路径:
                    resume_upload 文件名
                通过cd切换目录, 到该目录下指定服务端的某个目录下继续上传:
                    cd /目录1/目录2
                        resume_upload 文件名
                """,
    None: """
            查看相对应的帮助信息:
                1.  ls + --help         
                2.  cd --help
                3.  mkdir --help
                4.  rmdir --help
                5.  remove --help
                6.  upload --help
                7.  resume_upload --help
            """,
}