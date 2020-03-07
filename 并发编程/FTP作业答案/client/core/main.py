#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:31

import hashlib
import json
import os
import shelve
import socket
import struct

from conf import settings


class FTPClient:
    """FTP客户端."""
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    max_packet_size = 8192
    encoding = 'utf-8'
    windows_encoding = 'gbk'

    struct_fmt = 'i'
    fixed_packet_size = 4

    def __init__(self, server_address, connect=True):
        self.server_address = server_address
        self.socket = socket.socket(self.address_family, self.socket_type)

        self.breakpoint_resume = shelve.open(settings.UNFINISHED_DOWNLOAD_FILES_PATH)

        self.username = None
        self.current_dir = '~'
        if connect:
            try:
                self.client_connect()
            except Exception:
                self.client_close()
                raise

    def client_connect(self):
        """客户端连接服务端ip和port."""
        self.socket.connect(self.server_address)

    def client_close(self):
        """关闭连接通道."""
        self.socket.close()

    def interactive(self):
        """与服务端进行所有的交互."""
        if self.auth():
            self.unfinished_file_check()
            while True:
                self.show_str()
                msg = input('[%s@localhost %s]# ' % (self.username, self.current_dir)).strip()
                if not msg:
                    continue
                if not self.help_msg(msg):
                    continue
                # 核验命令参数
                cmd, path = self.verify_args(msg)
                if hasattr(self, '_%s' % cmd):
                    func = getattr(self, '_%s' % cmd)
                    func(path)
                else:
                    self.help_msg()

    @staticmethod
    def verify_args(msg):
        """
        效验参数.
        :param msg: ls       或 ls /路径       或 ls /路径1/路径2/
        :return:    (ls, []) 或 (ls, ['路径']) 或 (ls, ['路径1', '路径2'])
        """
        cmd_args = msg.split()
        cmd, path = cmd_args[0], cmd_args[1:]
        if path:
            path = ''.join(cmd_args[1:]).strip('//').split('/')
        # print('cmd, path:', cmd, path)
        return cmd, path

    def unfinished_file_check(self):
        if not list(self.breakpoint_resume.keys()):
            return

        print('检测到您本地还有未上传完成的文件')
        unfinished_path_list = []
        msg_list = []
        for unfinished_file_path in self.breakpoint_resume.keys():
            file_name = self.breakpoint_resume[unfinished_file_path]['file_name']
            file_size = self.breakpoint_resume[unfinished_file_path]['file_size']
            unfinished_file_size = os.path.getsize(unfinished_file_path)
            percent = unfinished_file_size / file_size * 100
            path = self.breakpoint_resume[unfinished_file_path]['path']
            dic = {'unfinished_file_size': unfinished_file_size, 'path': path}
            unfinished_path_list.append(dic)
            msg = """
            未完成的文件路径: %s    文件名: %s
            文件原大小: %s字节      已完成的文件大小: %s字节     上传的百分比: %.2f%%
            """ % (unfinished_file_path, file_name, file_size, unfinished_file_size, percent)
            msg_list.append(msg)

        while msg_list:
            print("未完成续传的数量: %s个".center(150, '-') % len(msg_list))
            for msg in msg_list:
                print('序号: %s' % (int(msg_list.index(msg) + 1)))
                print(msg)

            choice = input('[退出: q/Q]请根据序号选择您是否继续下载没有完成的文件>>:').strip()
            if choice.lower() == 'q':
                break
            if not choice.isdigit():
                continue
            choice = int(choice)
            if 0 < choice <= len(unfinished_path_list):  # len(unfinished_path_list)=3
                dic = unfinished_path_list[choice - 1]
                path, unfinished_file_size = dic['path'], dic['unfinished_file_size']

                print('开始续传......')
                self.__resume_download(path, unfinished_file_size)
                print('\n续传完毕!')

                unfinished_path_list.pop(choice-1)
                msg_list.pop(choice-1)
            else:
                print('您的选择超出了范围!')

    def auth(self):
        """
        登陆.
        100: '用户名密码正确, 认证成功!',
        199: '用户名密码不正确, 认证失败!',
        850: '您的还有为上传完的文件, 是否继续上传!',
        851: '检测您不存在未上传完成的文件!',
        """
        count = 0
        while count < 3:
            username = input('username>>:').strip()
            password = input('password>>:').strip()
            if not all([username, password]):
                print('用户名密码不能为空.')
                count += 1
                continue
            # 发报头
            self.send_header(action_type='auth', username=username, password=password)
            # 收报头
            response_dic = self.receive_header()
            status_code, status_msg = response_dic.get('status_code'), response_dic.get('status_msg')
            # 100: '用户名密码正确, 认证成功!',
            if status_code == 100:  # 100确认成功
                print(status_msg)
                self.username = username

                # 850: '您的还有为上传完的文件, 是否继续上传!',
                # 851: '检测您不存在未上传完成的文件!',
                response_dic = self.receive_header()
                status_code, status_msg, msg_list, msg_dic = response_dic.get('status_code'), response_dic.get(
                    'status_msg'), response_dic.get('msg_list'), response_dic.get('msg_dic')
                if msg_list:
                    print(status_msg)
                    for unfinished_msg in msg_list:
                        print(unfinished_msg)
                else:
                    print(status_msg)

                return True
            else:
                # 199: '用户名密码不正确, 认证失败!',
                print(status_msg)
                count += 1
        else:
            print('输入次数过多,强制退出!')
            return False

    def _ls(self, path):
        """
        显示目录的文件列表.
        :param path: [] 或 ['目录1', '目录2']
        :return: None
        """
        # 发送报头
        self.send_header(action_type='ls', path=path)
        # 接收报头
        response_dic = self.receive_header()
        status_code, status_msg, cmd_size = response_dic.get('status_code'), response_dic.get(
            'status_msg'), response_dic.get('cmd_size')
        if status_code == 301 and cmd_size:
            # print('status_msg:', status_msg)
            # print('cmd_size:', cmd_size)
            # 收消息
            windows_cmd = self.socket.recv(cmd_size).decode(self.windows_encoding)
            print(windows_cmd)
        else:
            print(status_msg)

    def _cd(self, path):
        """
        切换目录.
        :param path: ['..'] 或 ['路径1', '目录2']
        :return: None
        """
        # 发送报头
        self.send_header(action_type='cd', path=path)
        # 接收报头
        response_dic = self.receive_header()
        status_code, status_msg, current_dir = response_dic.get('status_code'), response_dic.get(
            'status_msg'), response_dic.get('current_dir')
        if status_code == 400:
            self.current_dir = current_dir
            print(status_msg)
        else:
            print(status_msg)

    def _mkdir(self, path):
        """
        新建目录.
        :param path: ['目录1']
                或   [目录2', '目录3']
        :return: None
        """
        # print(path)
        # 发送报头
        self.send_header(action_type='mkdir', path=path)
        # 接收报头
        response_dic = self.receive_header()
        status_code, status_msg = response_dic.get('status_code'), response_dic.get(
            'status_msg')
        if status_code == 500:
            print(status_msg)
        else:
            print(status_msg)

    def _rmdir(self, path):
        """
        删除空目录.
        :param path: ['', '12312都1的发']
        :return: None
        """
        # print(path)
        # 发送报头
        self.send_header(action_type='rmdir', path=path)
        # 接收报头
        response_dic = self.receive_header()
        status_code, status_msg = response_dic.get('status_code'), response_dic.get(
            'status_msg')
        if status_code == 600:
            print(status_msg)
        else:
            print(status_msg)

    def _remove(self, path):
        """
        删除文件.
        :param path: ['目录1', '文件1']
        :return:
        """
        # print(path)
        # 发送报头
        self.send_header(action_type='remove', path=path)
        # 接收报头
        response_dic = self.receive_header()
        status_code, status_msg = response_dic.get('status_code'), response_dic.get(
            'status_msg')
        if status_code == 700:
            print(status_msg)
        else:
            print(status_msg)

    def parser_path(self, action_type, path, **kwargs):
        """
        解析路径参数, 判断路径是文件名, 还是路径下的文件名.
        :param action_type: 用户上传的功能类型
        :param path: 用户路径例子: ['目录1', '文件1']  或 ['文件1']
        :param kwargs:
        :return: path列表长度合理的时候返回True, 不合理返回False
        """
        if len(path) > 1:
            self.send_header(action_type=action_type, **kwargs, file_name=path[-1],
                             path=path[:-1])
        elif len(path) == 1:
            self.send_header(action_type=action_type, **kwargs, file_name=path[-1],
                             path=None)
        else:
            print('必须指定路径, 或者文件名!')
            return False
        return True

    def _resume_upload(self, path):
        """
        upload的断点续传功能.
        860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
        869: '您选择文件路径中没有要续传的文件, 请核对!',
        """
        self._upload(path, resume_upload=True)

    def _upload(self, path, resume_upload=False):
        """
        上传文件到服务端.
        正常上传:
            800: '你可以上传文件, 在您上传之前, 您的目前空间:%s!',
            801: '上传文件成功, 您上传完后的剩余空间:%s!',
            852: '您不能进行续传, 因为该文件是完整文件!',
            894: '您不需要再本路径下上传文件, 该文件在您的当前路径下已经存在!',
            895: '上传文件失败, md5效验不一致, 部分文件内容在网络中丢失, 请重新上传!',
            896: '上传文件失败, 您的空间不足, 您的上传虚假文件大小, 您的剩余空间:%s!',
            897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
            898: '上传文件失败, 上传命令不规范!',
            899: '上传文件必须要有文件的md5值以及文件名!',
        续传:
            860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
            869: '您选择文件路径中没有要续传的文件, 请核对!',
        :param path: ['目录1', '文件1'] 或 ['文件1']
        :return: None
        """
        # 判断用户文件路径是否是FILES_PATH路径下的文件
        file_path = os.path.normpath(os.path.join(settings.FILES_PATH, *path))
        if not os.path.isfile(file_path):
            print('您要上传的文件不存在!')
            return

        # 解析用户路径, 并提交upload的相关功能
        file_size = os.path.getsize(file_path)
        file_md5 = self.md5(file_path)

        if resume_upload:  # 断点续传时执行
            action_type = 'resume_upload'
        else:  # 正常长传时执行
            action_type = 'upload'

        if not self.parser_path(action_type=action_type, file_md5=file_md5, file_size=file_size, path=path):
            return

        # 接收服务端相应字典
        # 正常: 800, 894, 897, 898, 899
        # 800: '你可以上传文件, 在您上传之前, 您的目前空间:%s!',
        # 894: '您不需要再本路径下上传文件, 该文件在您的当前路径下已经存在!',
        # 898: '上传文件失败, 上传命令不规范!',
        # 897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
        # 899: '上传文件必须要有文件的md5值以及文件名!',
        # 续传: 860, 869
        # 860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
        # 869: '您选择文件路径中没有要续传的文件, 请核对!',
        response_dic = self.receive_header()
        status_code, status_msg, residual_space_size, already_upload_size = response_dic.get(
            'status_code'), response_dic.get(
            'status_msg'), response_dic.get('residual_space_size'), response_dic.get('already_upload_size')

        # 判断状态码
        # 800: '你可以上传文件, 在您上传之前, 您的目前空间:%s!',
        # 860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
        if status_code == 800 or status_code == 860:  # 800正常发送文件确认  860续传文件确认
            print(status_msg % self.conversion_quota(residual_space_size))

            initial_size = 0
            if resume_upload:  # 断点续传时执行: 目前文件总大小要减去上次没有上传完位置的大小
                total_size = file_size - already_upload_size
            else:  # 正常上传时执行
                total_size = file_size
            with open(file_path, 'rb') as f:
                if resume_upload:  # 断点续传时执行: 光标移动到上次没有上传完位置
                    f.seek(already_upload_size)
                print('\nupload running...')
                for line in f:
                    self.socket.sendall(line)
                    initial_size += len(line)
                    percent = initial_size / total_size
                    self.progress_bar(percent)
                print('\nupload succeed!')

            # 第二次接收消息, 确认文件上传完毕
            # 801, 895, 896
            # 801: '上传文件成功, 您上传完后的剩余空间:%s!',
            # 895: '上传文件失败, md5效验不一致, 部分文件内容在网络中丢失, 请重新上传!',
            # 896: '上传文件失败, 您的空间不足, 您的上传虚假文件大小, 您的剩余空间:%s!',
            response_dic = self.receive_header()
            status_code, status_msg, residual_space_size = response_dic.get('status_code'), response_dic.get(
                'status_msg'), response_dic.get('residual_space_size')
            if residual_space_size:  # 801, 896
                print(status_msg % self.conversion_quota(residual_space_size))
            else:  # 895
                print(status_msg)
        else:
            # 正常: 894, 897, 898, 899
            # 894: '您不需要再本路径下上传文件, 该文件在您的当前路径下已经存在!',
            # 897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
            # 898: '上传文件失败, 上传命令不规范!',
            # 899: '上传文件必须要有文件的md5值以及文件名!',
            # 续传:
            # 869: '您选择文件路径中没有要续传的文件, 请核对!',
            if residual_space_size:  # 897
                print(status_msg % self.conversion_quota(residual_space_size))
            else:  # 869, 894, 898, 899
                print(status_msg)

    def __resume_download(self, path, unfinished_file_size):
        self._download(path, unfinished_file_size, resume_download=True)

    def _download(self, path, unfinished_file_size=None, resume_download=False):
        """

        900: '准备开始下载文件!',
        999: '下载文件失败, 您要下载的文件路径不规范!',
        :param path:
        :param resume_download:
        :return:
        """
        if resume_download:
            action_type = 'resume_download'
        else:
            action_type = 'download'
        self.send_header(action_type=action_type, path=path, unfinished_file_size=unfinished_file_size)

        # 接收服务端消息
        # self.send_header(status_code=900, file_name=file_name, file_size=file_size, file_md5=file_md5)
        response_dic = self.receive_header()
        status_code, status_msg, file_name, file_size, file_md5 = response_dic.get('status_code'), response_dic.get(
            'status_msg'), response_dic.get('file_name'), response_dic.get('file_size'), response_dic.get('file_md5')

        # 判断状态码
        # 900: '准备开始下载文件!',
        # 950: '准备开始续传文件!',
        # 998: '下载文件失败, 您要下载的文件路径不存在!',
        # 999: '下载文件失败, 您要下载的文件路径不规范!',
        if status_code == 900 or status_code == 950:

            file_path = os.path.join(settings.FILES_PATH, file_name)
            if resume_download and file_path in self.breakpoint_resume.keys():
                unfinished_file_path = self.breakpoint_resume[file_path]['unfinished_file_path']
            else:
                # 判断本次路径下是否有文件, 有文件则提示
                # file_path = os.path.join(settings.FILES_PATH, file_name)
                if os.path.isfile(file_path):
                    print('本次路径下文件已经存在, 不需要继续下载!')
                    return
                # 为没有下载完毕的文件名添加后缀
                unfinished_file_path = '%s.%s' % (file_path, 'download')

            # 为出现下载终端添加断点记录
            self.breakpoint_resume[unfinished_file_path] = {'file_name': file_name, 'file_size': file_size,
                                                            'path': path}

            # 开始进行下载
            receive_size = 0
            if resume_download:
                total_size = file_size - os.path.getsize(unfinished_file_path)
                mode = 'a'
            else:
                total_size = file_size
                mode = 'w'
            with open(unfinished_file_path, '%sb' % mode) as f:
                print('\ndownload run...')
                while receive_size < total_size:
                    data_bytes = self.socket.recv(self.max_packet_size)
                    f.write(data_bytes)
                    receive_size += len(data_bytes)
                    percent = receive_size / total_size
                    self.progress_bar(percent)
                print('\ndownload succeed!')
                f.flush()

            # 正常下载成功把后缀去除, 文件改名, 删除断点记录
            del self.breakpoint_resume[unfinished_file_path]
            os.rename(unfinished_file_path, file_path)

            # 效验md5值询问用户是否保存
            server_file_md5 = file_md5
            current_file_md5 = self.md5(file_path)
            if server_file_md5 != current_file_md5:
                print('您的文件不完成, 可能不能打开, 请重新下载!')
        else:
            # 998: '下载文件失败, 您要下载的文件路径不存在!',
            # 999: '下载文件失败, 您要下载的文件路径不规范!',
            print(status_msg)

    @staticmethod
    def conversion_quota(residual_space_size):
        """
        换算服务端发送过来的字节为MB, 人性化的展现用户的空间剩余.
        :param residual_space_size: 剩余空间字节数
        :return: MB为单位的字节
        """
        residual_space_mb = residual_space_size / (1024 ** 2)
        return '%.2fMB' % residual_space_mb

    def receive_header(self):
        """
        接收服务端发送过来的报头字典.
        :return: {'status_code': 100, 'status_msg': '认证成功', 'cmd_size': 199}
        """
        header_bytes = self.socket.recv(self.fixed_packet_size)
        header_dic_json_length = struct.unpack(self.struct_fmt, header_bytes)[0]
        # 接收报头
        header_dic_json = self.socket.recv(header_dic_json_length).decode(self.encoding)
        header_dic = json.loads(header_dic_json)
        return header_dic

    def send_header(self, *, action_type, **kwargs):
        """
        发送报头字典给客户端.
        :param action_type: action_type='auth'
        :param kwargs: {'username': 'egon', 'password': '123'}
        :return: None
        """
        request_dic = kwargs
        request_dic['action_type'] = action_type
        request_dic.update(request_dic)

        request_dic_json_bytes = json.dumps(request_dic).encode(self.encoding)
        request_dic_json_bytes_length = len(request_dic_json_bytes)
        header_bytes = struct.pack(self.struct_fmt, request_dic_json_bytes_length)

        # 发送报头
        self.socket.sendall(header_bytes)
        # 发送json后bytes后的字典request_dic
        self.socket.sendall(request_dic_json_bytes)

    @staticmethod
    def md5(file_path):
        """
        md5加密哈希文件.
        :param file_path: files下的文件路径
        :return: 文件hash值
        """
        md5_obj = hashlib.md5()
        with open(file_path, 'rb') as f:
            for line in f:
                md5_obj.update(line)
        return md5_obj.hexdigest()

    @staticmethod
    def progress_bar(percent, width=50, symbol='#'):
        """进度条功能."""
        if percent > 1:
            percent = 1
        show_str = ('[%%-%ds]' % width) % (int(width * percent) * symbol)
        print('\r%s %.2f%%' % (show_str, percent * 100), end='')

    @staticmethod
    def show_str():
        """显示客户端flies中的文件列表."""
        print('\n------您的files文件夹下所含有的文件------')
        for index, filename in enumerate(os.listdir(settings.FILES_PATH), 1):
            print('%s: %s' % (index, filename))
        print()

    @staticmethod
    def help_msg(msgs=None):
        """帮助信息."""
        if msgs in settings.help_dic:
            print(settings.help_dic[msgs])
        else:
            return True
