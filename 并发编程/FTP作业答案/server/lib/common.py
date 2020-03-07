#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:55

import hashlib
import logging.config
import os

from conf import settings


def md5(encryption_type, path=None, password=None):
    """
    md5加密.
    :param encryption_type: 加密的类型, 支持file和password两种
    :param path: 文件或目录路径
    :param password: 明文密码
    :return: 加密后的md5值
    """
    md5_obj = hashlib.md5()
    if encryption_type == 'file':
        if os.path.isfile(path):
            with open(path, 'rb') as f:
                for line in f:
                    md5_obj.update(line)
            return md5_obj.hexdigest()
        for filename in os.listdir(path):
            current_path = os.path.join(path, filename)
            if os.path.isdir(current_path):
                md5(encryption_type, path=current_path)
            else:
                with open(current_path, 'rb') as f:
                    for line in f:
                        md5_obj.update(line)
    elif encryption_type == 'password':
        md5_obj.update(password.encode('utf-8'))
    return md5_obj.hexdigest()


def load_my_logging_cfg():
    """
    加载日志字典.
    :return: logger对象
    """
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(__name__)
    return logger


def get_size(path):
    """
    遍历用户path, 拿到path的路径大小, 该大小包含目录下的所有文件.
    :param path: 路径
    :return: 该路径下的所有文件的大小
    """
    initial_size = 0
    if os.path.isfile(path):
        return os.path.getsize(path)
    for filename in os.listdir(path):
        current_path = os.path.join(path, filename)
        if os.path.isdir(current_path):
            get_size(current_path)
        else:
            initial_size += os.path.getsize(current_path)
    return initial_size


def conversion_quota(quota_mb: str):
    """
    换算用户磁盘配额, 把MB换算成bytes.
    :param quota_mb:
    :return: 满足isdigit返回quota_bytes, 不满足设置默认的配额大小
    """
    if quota_mb.isdigit():
        quota_mb = int(quota_mb)
        quota_bytes = quota_mb * 1024 ** 2
        # print('def conversion_quota ===> quota_bytes:', quota_bytes)
        return quota_bytes
    else:
        default_quota_bytes = 50 * 1024 ** 2
        return default_quota_bytes
