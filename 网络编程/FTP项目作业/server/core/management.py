#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/15 20:31

from core import main


class ManagementTool(object):
    """负责对用户输入的指令进行解析并调用相应模块处理"""

    def __init__(self, sys_argv):
        self.sys_argv = sys_argv  # [createuser alex]
        print(self.sys_argv)
        self.verify_argv()

    def verify_argv(self):
        """验证指令合法性"""
        if len(self.sys_argv) < 2:
            self.help_msg()
        cmd = self.sys_argv[1]
        if not hasattr(self, cmd):  # 如果不存在
            print('invalid argument!')
            self.help_msg()  # 显示帮助信息

    def help_msg(self):
        msg = '''
        start       start FTP作业答案 server
        stop        stop FTP作业答案 server
        restart     restart FTP作业答案 server
        createuser  username   create a ftp user
        '''
        exit(msg)  # 执行之后退出

    def execute(self):  # self代表实例本身
        """解析并执行指令"""
        cmd = self.sys_argv[1]
        func = getattr(self, cmd)
        func()

    def start(self):
        """start ftp server"""
        server = main.FTPServer(self)
        server.run_forever()



    def createuser(self):
        print(self.sys_argv)
