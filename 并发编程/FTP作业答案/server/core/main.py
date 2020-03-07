#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:33

import configparser
import socket

from conf import settings
from core import handler_request, mythreadpool
from lib import common


class FTPServer:
    """FTP服务器."""
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    request_queue_size = 5

    max_pool_size = 5

    STATUS_CODE = settings.STATUS_CODE

    logger = common.load_my_logging_cfg()

    def __init__(self, management_instance, bind_address, bind_and_activate=True):
        self.management_instance = management_instance

        self.pool = mythreadpool.MyThreadPool(self.max_pool_size)

        self.bind_address = bind_address
        self.socket = socket.socket(self.address_family, self.socket_type)

        if bind_and_activate:
            try:
                self.server_bind()
                self.server_activate()
            except Exception:
                self.server_close()
                raise

    def server_bind(self):
        """服务器绑定IP,端口."""
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.bind_address)

    def server_activate(self):
        """服务器激活."""
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """关闭服务socket对象."""
        self.socket.close()

    def serve_forever(self):
        """服务器永远运行."""
        while True:  # 通信循环
            request, address = self.socket.accept()

            self.logger.info('----连接----# ip:%s port:%s' % address)

            # 来一个连接, 实例化一个处理用户请求的对象
            handler_response = handler_request.HandlerRequest(request, address)
            # 来了一个连接取走一个线程
            thread = self.pool.get_thread()
            # 同时再添加一个线程
            self.pool.put_thread()
            t = thread(target=handler_response.handle_request)
            t.start()

    @staticmethod
    def load_accounts():
        conf_obj = configparser.ConfigParser()
        conf_obj.read(settings.ACCOUNTS_FILE)
        return conf_obj
