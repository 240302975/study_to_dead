#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:33

import os


def base_dir(*args):
    return os.path.normpath(os.path.join(__file__, '..', '..', *args))


# 用户家目录存放路径
USER_HOME_DIR = base_dir('home')

# 用户账户信息文件路径
ACCOUNTS_FILE = base_dir('conf', 'accounts.ini')

# 本机测试的ip和port
HOST = '127.0.0.1'
PORT = 8080

# 状态码: 负责提供交互成功及失败的提示信息反馈
STATUS_CODE = {
    100: '用户名密码正确, 认证成功!',
    199: '用户名密码不正确, 认证失败!',
    200: '您的功能指定不能为空!',
    201: '没有该功能, 请查看帮助信息!',
    301: '本次返回结果包含命令大小.',
    400: '切换目录成功',
    498: '切换目录失败, 切换命令不规范',
    499: '切换目录失败, 目标地址不存在!',
    500: '创建目录成功!',
    598: '创建目录命令输入不规范!',
    599: '创建的目录已存在!',
    600: '删除目录成功!',
    699: '删除目录失败, 该目录不为空!',
    698: '删除目录失败, 不存在该目录!',
    697: '删除目录失败, 删除命令不规范!',
    700: '删除文件成功!',
    799: '删除文件失败, 不存在该文件!',
    800: '你可以上传文件, 在您上传之前, 您的目前空间:%s!',
    801: '上传文件成功, 您上传完后的剩余空间:%s!',
    850: '服务端检测您还有为上传完的文件, 是否继续上传!',
    851: '服务端检测您没有未上传完成的文件!',
    852: '您不能进行续传, 因为该文件是完整文件!',
    860: '您正在继续上传文件, 在您继传之前, 您的目前空间:%s!',
    869: '您选择文件路径中没有要续传的文件, 请核对!',
    894: '您不需要再对本路径下上传文件, 该文件在您的当前路径下已经存在!',
    895: '上传文件失败, md5效验不一致, 部分文件内容在网络中丢失, 请重新上传!',
    896: '上传文件失败, 您的空间不足, 您的上传虚假文件大小, 您的剩余空间:%s!',
    897: '上传文件失败, 您的空间不足, 您的剩余空间:%s!',
    898: '上传文件失败, 上传命令不规范!',
    899: '上传文件必须要有文件的md5值以及文件名!',
    900: '准备开始下载文件!',
    950: '准备开始续传文件!',
    998: '下载文件失败, 您要下载的文件路径不存在!',
    999: '下载文件失败, 您要下载的文件路径不规范!',
}

# log日志路径
ACCESS_LOG_PATH = base_dir('log', 'access.log')

# 定义log日志输出格式
standard_format = '%(asctime)s - %(threadName)s:%(thread)d - task_id:%(name)s - %(filename)s:%(lineno)d - ' \
                  '%(levelname)s - %(message)s'  # 其中name为getlogger指定的名字

simple_format = '\n%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(message)s\n'


# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format,
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'access': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': ACCESS_LOG_PATH,  # 日志文件
            # 'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['access', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,  # 向上（更高level的logger）传递
        },
    },
}
