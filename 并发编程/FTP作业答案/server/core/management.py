#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:33

import sys

from conf import settings
from core import main


class ManagementTool(object):
    """管理服务器."""
    center_args1, center_args2 = 50, '-'

    def __init__(self):
        self.script_argv = sys.argv
        self.commands = None

    def start(self):
        """启动ftp服务."""
        print('FTP作业答案 started successfully!')
        server = main.FTPServer(self, (settings.HOST, settings.PORT))
        server.serve_forever()
