#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:33

import json
import os
import shelve
import struct
import subprocess

from conf import settings
from lib import common


class HandlerRequest:
    """处理用户请求."""
    max_packet_size = 8192
    encoding = 'utf-8'

    struct_fmt = 'i'
    fixed_packet_size = 4

    logger = common.load_my_logging_cfg()

    def __init__(self, request, address):
        self.request = request
        self.address = address

        self.residual_space_size = None

        self.breakpoint_resume = None

        self.username = None
        self.user_obj = None
        self.user_current_dir = None

    def client_close(self):
        """关闭客户端连接."""
        self.request.close()

    def handle_request(self):
        """处理客户端请求."""
        count = 0
        while count < 3:  # 连接循环
            try:
                if self.auth():
                    # 收消息
                    user_dic = self.receive_header()
                    action_type = user_dic.get('action_type')
                    if action_type:
                        if hasattr(self, '_%s' % action_type):
                            func = getattr(self, '_%s' % action_type)
                            func(user_dic)
                        else:
                            self.send_header(status_code=201)
                    # 发消息
                    else:
                        self.send_header(status_code=200)
                else:
                    count += 1
                    self.send_header(status_code=199)
            except ConnectionResetError:
                break
        # 关闭客户端连接
        self.logger.info('----连接断开---- ip:%s port:%s' % self.address)
        self.client_close()

    def unfinished_file_check(self):
        self.logger.info('#执行unfinished_file_check命令# ip:%s port:%s' % self.address)

        if not list(self.breakpoint_resume.keys()):
            self.send_header(status_code=851)
            return

        #  self.breakpoint_resume[file_path] =
        #  {'file_size': _file_size, 'unfinished_file_path': unfinished_file_path, 'file_name': _file_name}
        msg_list = []

        for index, abs_path in enumerate(self.breakpoint_resume.keys(), 1):\

            user_path = '/'.join(abs_path.split(self.username)[-1].split(os.sep))
            print('abs_path:', user_path)
            file_name = self.breakpoint_resume[abs_path]['file_name']
            src_file_size = self.breakpoint_resume[abs_path]['file_size']
            unfinished_file_size = os.path.getsize(self.breakpoint_resume[abs_path]['unfinished_file_path'])
            percent = unfinished_file_size / src_file_size * 100

            msg = """
            数量: %s  文件路径: %s 文件名: %s
                文件原大小: %s字节 未完成的文件大小: %s字节 上传的百分比: %.2f%%
            """ % (index, user_path, file_name, src_file_size, unfinished_file_size, percent)

            msg_list.append(msg)
            # msg_dic['/03_函数调用的三种形式.mp4'] = 5772100
            # msg_dic[user_path] = unfinished_file_size
        # self.send_header(status_code=850, msg_list=msg_list, msg_dic=msg_dic)
        self.send_header(status_code=850, msg_list=msg_list)

    def auth(self):
        """用户登陆认证."""
        if self.user_current_dir:
            return True

        # 涉及到交叉导入
        from core import main
        # 收消息
        auth_dic = self.receive_header()

        user_name = auth_dic.get('username')
        user_password = auth_dic.get('password')
        md5_password = common.md5('password', password=user_password)

        # print(user_name, user_password,  md5_password)

        accounts = main.FTPServer.load_accounts()
        if user_name in accounts.sections():
            if md5_password == accounts[user_name]['password']:
                self.send_header(status_code=100)

                self.username = user_name
                self.user_obj = accounts[user_name]
                self.user_obj['home'] = os.path.join(settings.USER_HOME_DIR, user_name)
                self.user_current_dir = self.user_obj['home']

                # print('self.user_obj:', self.user_obj)
                # print("self.user_obj['home']:", self.user_obj['home'])

                self.residual_space_size = common.conversion_quota(
                    self.user_obj['quota']) - common.get_size(self.user_obj['home'])

                breakpoint_resume_dir_path = os.path.join(self.user_obj['home'], '.upload')
                if not os.path.isdir(breakpoint_resume_dir_path):
                    os.mkdir(breakpoint_resume_dir_path)
                self.breakpoint_resume = shelve.open(os.path.join(breakpoint_resume_dir_path, '.upload.shv'))
                self.unfinished_file_check()

                self.logger.info('#认证成功# ip:%s port:%s' % self.address)
                return True
        self.logger.info('#认证失败# ip:%s port:%s' % self.address)
        return False

    def _ls(self, cmd_dic):
        """
        运行dir命令将结果发送到客户端.
        :param cmd_dic: {'path': [], 'action_type': 'ls'}
                    或  {'path': ['目录1', '目录2', '目录xxx'], 'action_type': 'ls'}
                    或  {'path': ['?'], 'action_type': 'ls'}
        :return: None
        """
        # print('_ls:', cmd_dic)
        self.logger.info('#执行ls命令# ip:%s port:%s' % self.address)

        # 核验路径
        dir_path = self.verify_path(cmd_dic)
        if not dir_path:
            dir_path = self.user_current_dir

        if cmd_dic.get('path') == ['?']:  # 为用户提供ls /?命令
            dir_path = '/?'

        sub_obj = subprocess.Popen(
            'dir %s' % dir_path,
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        stderr_bytes, stdout_bytes = sub_obj.stderr.read(), sub_obj.stdout.read()
        cmd_size = len(stderr_bytes) + len(stdout_bytes)

        # 发报头
        self.send_header(status_code=301, cmd_size=cmd_size)
        # 发消息
        self.request.sendall(stderr_bytes)
        self.request.sendall(stdout_bytes)

    def _cd(self, cmd_dic):
        """
        根据用户的目标目录, 改变用户的当前目录的值.
        :param cmd_dic: {'action_type': 'cd', 'path': ['..']}
                     或 {'action_type': 'cd', 'path': ['目录1', '目录2', '目录xxx'], }
        :return: None
                 Z:\\pycharm\\开发FTP程序之路\\第2次FTP_第四模块作业\\FUCK_FTP\\server\\home\\egon\\目录1
        """
        # print('_cd:', cmd_dic)
        self.logger.info('#执行cd命令# ip:%s port:%s' % self.address)

        # 核验路径
        dir_path = self.verify_path(cmd_dic)
        if dir_path:
            if os.path.isdir(dir_path):  # 判断用户切换的路径是否存在
                self.user_current_dir = dir_path
                if dir_path == self.user_obj['home']:
                    current_dir = '~'
                else:
                    join_dir = ''.join(dir_path.split('%s' % self.username)[1:])
                    current_dir = '/'.join(join_dir.split('\\'))
                self.send_header(status_code=400, current_dir=current_dir)
            else:
                self.send_header(status_code=499)
        else:
            self.send_header(status_code=498)

    def _mkdir(self, cmd_dic):
        """
        更具用户的目标目录, 且目录不存在, 创建目录标目录, 生成多层递归目录.
        :param cmd_dic: {'action_type': 'mkdir', 'path': ['目录1']}
                    或  {'action_type': 'mkdir', 'path': ['目录2', '目录3', '目录xxx']}
        :return: None
        """
        # print('_mkdir:', cmd_dic)
        self.logger.info('#执行mkdir命令# ip:%s port:%s' % self.address)

        dir_path = self.verify_path(cmd_dic)
        if dir_path:
            if not os.path.isdir(dir_path):  # 判断用户要创建的目录时否存在
                os.makedirs(dir_path)
                self.send_header(status_code=500)
            else:
                self.send_header(status_code=599)
        else:
            self.send_header(status_code=598)

    def _rmdir(self, cmd_dic):
        """
        更具用户的目标目录, 删除不为空的目录.
        :param cmd_dic: {'path': ['目录1', '目录xxx', '空目录'], 'action_type': 'rmdir'}
        :return: None
        """
        # print('_rmdir:', cmd_dic)
        self.logger.info('#执行rmdir命令# ip:%s port:%s' % self.address)

        dir_path = self.verify_path(cmd_dic)
        if dir_path:
            if os.path.isdir(dir_path):
                if os.listdir(dir_path):
                    self.send_header(status_code=699)
                else:
                    os.rmdir(dir_path)
                    self.send_header(status_code=600)
            else:
                self.send_header(status_code=698)
        else:
            self.send_header(status_code=697)

    def _remove(self, cmd_dic):
        """
        更具用户的目标文件, 删除该文件
        :param cmd_dic: {'path': ['目录1', '目录xxx', '文件'], 'action_type': 'remove'}
        :return:
        """
        # print('_remove:', cmd_dic)
        self.logger.info('#执行remove命令# ip:%s port:%s' % self.address)
        file_path = self.verify_path(cmd_dic)

        if file_path:
            if os.path.isfile(file_path):
                # 判断用户删除的文件是否是要续传的文件, 如果是则先把把续传的记录删除
                if file_path in self.breakpoint_resume.keys:
                    del self.breakpoint_resume[file_path]
                os.remove(file_path)
                self.send_header(status_code=700)
            else:
                self.send_header(status_code=799)
        else:
            self.send_header(status_code=798)

    def _resume_upload(self, cmd_dic):
        """
        860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
        869: '您选择文件路径中没有要续传的文件, 请核对!',
        :param cmd_dic:
        :return:
        """
        # print('def _resume_upload ===> cmd_args', cmd_dic)
        self.logger.info('#执行resume_upload命令# ip:%s port:%s' % self.address)
        self._upload(cmd_dic, resume_upload=True)

    def _upload(self, cmd_dic, resume_upload=False):
        """客户端
            800: '你可以上传文件, 在您上传之前, 您的目前空间:%s!',
            801: '上传文件成功, 您上传完后的剩余空间:%s!',
            850: '您的还有为上传完的文件, 是否继续上传!',
            851: '检测您不存在未上传完成的文件!',
            852: '您不能进行续传, 因为该文件是完整文件!',
            860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
            869: '您选择文件路径中没有要续传的文件, 请核对!',
            894: '您不需要再对本路径下上传文件, 该文件在您的当前路径下已经存在!',
            895: '上传文件失败, md5效验不一致, 部分文件内容在网络中丢失, 请重新上传!',
            896: '上传文件失败, 您的空间不足, 您的上传虚假文件大小, 您的剩余空间:%s!',
            897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
            898: '上传文件失败, 上传命令不规范!',
            899: '上传文件必须要有文件的md5值以及文件名!',
        """
        # print('_upload:', cmd_dic)
        if not resume_upload:
            self.logger.info('#执行upload命令# ip:%s port:%s' % self.address)

        # 效验: 897, 898, 899
        _path, _file_md5, _file_name, _file_size = cmd_dic.get('path'), cmd_dic.get('file_md5'), cmd_dic.get(
            'file_name'), cmd_dic.get('file_size')
        file_path = self.verify_upload_action(cmd_dic, _path=_path, _file_md5=_file_md5, _file_name=_file_name,

                                              _file_size=_file_size)

        if resume_upload:   # 断点续传时执行
            if not file_path or file_path not in self.breakpoint_resume.keys():
                # 869: '您选择文件路径中没有要续传的文件, 请核对!',
                self.send_header(status_code=869)
                return

            # 找到之前未穿完的文件名
            unfinished_file_path = self.breakpoint_resume[file_path]['unfinished_file_path']
            already_upload_size = os.path.getsize(unfinished_file_path)

            # 效验成功通知续传信号
            # 860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
            self.send_header(status_code=860, residual_space_size=self.residual_space_size,
                             already_upload_size=already_upload_size)

            total_size = _file_size - already_upload_size
            mode = 'a'
        else:           # 正常上传执行
            if not file_path:
                return

            # 判断用户上传的文件是否重复
            if os.path.isfile(file_path):
                # 894: '您不需要再对本路径下上传文件, 该文件在您的当前路径下已经存在!',
                self.send_header(status_code=894)
                return
            else:
                unfinished_file_path = '%s.%s' % (file_path, 'upload')

            # 效验成功通知上传信号: 800
            # 800: '你可以上传文件, 在您上传之前, 您的目前空间:%s!',
            self.send_header(status_code=800, residual_space_size=self.residual_space_size)

            total_size = _file_size
            mode = 'w'

        # 记录断点的功能: 在服务端用户的路径, 记录文件大小, 加上后缀的路径, 文件名
        # 或再次为未传完的文件记录断点
        self.breakpoint_resume[file_path] = {'file_size': _file_size, 'unfinished_file_path': unfinished_file_path,
                                             'file_name': _file_name}

        # 开始接收文件
        receive_size = 0
        with open(unfinished_file_path, '%sb' % mode) as f:
            while receive_size < total_size:
                data_bytes = self.request.recv(self.max_packet_size)
                receive_size += len(data_bytes)
                f.write(data_bytes)
        # 接收完毕, 把后缀改成用户上传的文件名
        os.rename(unfinished_file_path, file_path)
        # 删除记录断点的功能
        del self.breakpoint_resume[file_path]

        # 801, 895, 896
        # 效验用户端发送的md5于本次上传完毕的md5值
        upload_file_md5 = common.md5(encryption_type='file', path=file_path)
        if upload_file_md5 != _file_md5:
            # print('def _upload ===> upload_file_md5:%s, _file_md5:%s' % (upload_file_md5, _file_md5))
            # 895: '上传文件失败, md5效验不一致, 部分文件内容在网络中丢失, 请重新上传!',
            self.send_header(status_code=895)
            os.remove(file_path)
            return

        # 安全性问题: 再次判断用户是否以假的文件大小来跳出服务端限制的配额
        if receive_size > self.residual_space_size:
            # 896: '上传文件失败, 您的空间不足, 您的上传虚假文件大小, 您的剩余空间:%s!',
            self.send_header(status_code=896, residual_space_size=self.residual_space_size)
            os.remove(file_path)
            return
        else:
            self.residual_space_size = self.residual_space_size - receive_size
            # print('def _upload ===> receive_size:', receive_size)
            # print('def _upload ===> os.path.getsize(file_path)', os.path.getsize('%s' % file_path))
            # 801: '上传文件成功, 您上传完后的剩余空间:%s!',
            self.send_header(status_code=801, residual_space_size=self.residual_space_size)

    def _resume_download(self, cmd_dic):
        self._download(cmd_dic, resume_download=True)

    def _download(self, cmd_dic, resume_download=False):
        self.logger.info('#执行download命令# ip:%s port:%s' % self.address)

        file_path = self.verify_path(cmd_dic)
        if not file_path:
            # 999: '下载文件失败, 您要下载的文件路径不规范!',
            self.send_header(status_code=999)
            return

        if not os.path.isfile(file_path):
            # 998: '下载文件失败, 您要下载的文件路径不存在!',
            self.send_header(status_code=998)
            return

        # 通知可以开始下载
        # 900: '准备开始下载文件!'.
        file_name = file_path.split(os.sep)[-1]
        file_size = os.path.getsize(file_path)
        file_md5 = common.md5('file', file_path)
        unfinished_file_size = cmd_dic.get('unfinished_file_size')
        if resume_download:
            # 950: '准备开始续传文件!',
            self.send_header(status_code=950, file_name=file_name, file_size=file_size, file_md5=file_md5)
        else:
            # 900: '准备开始下载文件!'.
            self.send_header(status_code=900, file_name=file_name, file_size=file_size, file_md5=file_md5)

        # 打开文件发送给客户端
        with open(file_path, 'rb') as f:
            if resume_download:
                f.seek(unfinished_file_size)
            for line in f:
                self.request.sendall(line)

    def verify_upload_action(self, cmd_dic, *, _path, _file_name, _file_md5, _file_size):
        """
        核验上传功能.
        897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
        898: '上传文件失败, 上传命令不规范!',
        899: '上传文件必须要有文件的md5值以及文件名!',
        """
        # _path=['03_函数调用的三种形式.mp4']
        if _path is None:
            if _file_name and _file_md5 and _file_size:
                if _file_size > self.residual_space_size:
                    # print('def _upload ===> self.residual_space_size:', self.residual_space_size)

                    # 897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
                    self.send_header(status_code=897, residual_space_size=self.residual_space_size)
                    return False
                else:
                    # Z:\pycharm\开发FTP程序之路\第2次FTP_第四模块作业\FUCK_FTP\server\home\egon\03_函数调用的三种形式.mp4
                    file_path = os.path.join(self.user_current_dir, _file_name)
            else:
                # 899: '上传文件必须要有文件的md5值以及文件名!',
                self.send_header(status_code=899)
                return False
        else:
            path = self.verify_path(cmd_dic)

            if not path:
                # 898: '上传文件失败, 上传命令不规范!',
                self.send_header(status_code=898)
                return False
            else:
                # Z:\pycharm\开发FTP程序之路\第2次FTP_第四模块作业\FUCK_FTP\server\home\egon\03_函数调用的三种形式.mp4
                file_path = os.path.join(path, _file_name)
        return file_path

    def verify_path(self, cmd_dic):
        """
        核验客户端传过来的路径.
        :param cmd_dic: {'action_type': 'ls', 'path': []}
                    或  {'action_type': 'ls', 'path': ['目录1', '目录xxx']}
                    或  {action_type': 'cd', 'path': ['目录2', '目录xxx']}
        :return: None
                 Z:\\pycharm\\开发FTP程序之路\\第2次FTP_第四模块作业\\FUCK_FTP\\server\\home\\egon\\目录1
                 Z:\\pycharm\\开发FTP程序之路\\第2次FTP_第四模块作业\\FUCK_FTP\\server\\home\\egon\\目录1
        """
        # print(cmd_dic)
        path = cmd_dic.get('path')
        if path:
            if isinstance(path, list):
                for element in path:
                    if not isinstance(element, str):
                        path = None
                        return path
                abspath = os.path.normpath(os.path.join(self.user_current_dir, *path))
                # print('def verify_path() ===> abspath:', abspath)
                if abspath.startswith(self.user_obj['home']):
                    path = abspath
                else:
                    path = None  # 用户目录超出限制
            else:
                path = None  # 不是列表类型例: '字符串'
        else:
            path = None  # []
        # print('def verify_path() ====> path', path)
        return path

    def receive_header(self):
        """
        接收客户端数据.
        :return: {'action_type': 'cd', 'path': ['目录1', '目录xxx']}
        """
        header_bytes = self.request.recv(self.fixed_packet_size)
        request_dic_json_length = struct.unpack(self.struct_fmt, header_bytes)[0]
        # print('request_dic_json_length:', request_dic_json_length)
        # 接收报头
        request_dic_json = self.request.recv(request_dic_json_length).decode(self.encoding)
        request_dic = json.loads(request_dic_json)

        # print('request_dic:', request_dic)

        if not request_dic:
            return {}
        # print("def receive_header():", request_dic)
        return request_dic

    def send_header(self, *, status_code, **kwargs):
        """
        发送数据给客户端.
        :param status_code: 400
        :param kwargs: {'current_dir': '/home/egon/目录1/目录xxx'}
        :return: None
        """
        # print(status_code)
        # print(kwargs)
        from core import main

        response_dic = kwargs
        response_dic['status_code'] = status_code
        response_dic['status_msg'] = main.FTPServer.STATUS_CODE[status_code]
        response_dic.update(kwargs)

        response_dic_json_bytes = json.dumps(response_dic).encode(self.encoding)
        response_dic_json_bytes_length = len(response_dic_json_bytes)
        header_bytes = struct.pack(self.struct_fmt, response_dic_json_bytes_length)

        # print('header_bytes:', header_bytes)

        # 发送报头
        self.request.sendall(header_bytes)
        # 发送json后bytes后的字典response_dic
        self.request.sendall(response_dic_json_bytes)
