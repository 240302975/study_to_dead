#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 21:01


import json
import logging
import os
import sys
from logging import handlers

core_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(core_path)
from core import withdraw

_username = 'alice'
_password = '123'
msg = '''
1. 账户信息
2. 转账
3. 提现
'''
json_path = os.path.join(core_path, 'account')
flag_login = False
logger = logging.getLogger('record')


def log_record():
    global logger
    logger.setLevel(logging.DEBUG)
    # fh = logging.FileHandler(os.path.join(core_path, 'logs/bank.log'),encoding='utf-8')
    fh = logging.handlers.TimedRotatingFileHandler(filename=os.path.join(core_path, 'logs/bank.log'), when='S',
                                                   interval=3, backupCount=3, encoding='utf-8')
    logger.addHandler(fh)
    f_formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fh.setFormatter(f_formatter)


def login(func):
    def inner():
        global flag_login
        if not flag_login:
            username = input('username:').strip()
            password = input('password:').strip()
            if username == _username and password == _password:
                print('登录成功！')
                flag_login = True
                logger.info('登录成功')
            else:
                print('用户名或密码有误！')
        else:
            print('用户已登录，通过认证')
        if flag_login is True:
            func()

    return inner


def print_info():
    # 账户信息
    luffy_data = json.load(open(os.path.join(json_path, 'luffy.json'), 'r', encoding='utf-8'))
    print('account_balance：', luffy_data['account_balance'])
    print('credit_account:', luffy_data['credit_account'])


@login
def transfer_account():
    # 转账
    luffy_data = json.load(open(os.path.join(json_path, 'luffy.json'), 'r', encoding='utf-8'))
    tesla_data = {'account_balance': 750000}
    luffy_data['account_balance'] = luffy_data['account_balance'] - tesla_data['account_balance'] * (1 + 0.05)
    json.dump(luffy_data, open(os.path.join(json_path, 'luffy.json'), 'w', encoding='utf-8'))
    json.dump(tesla_data, open(os.path.join(json_path, 'tesla.json'), 'w', encoding='utf-8'))
    print('转账成功！')
    logger.debug('转账成功')


@login
def withdraws_func():
    # 提现
    moneys = input('moneys>>>:').strip()
    if moneys.isdigit():
        moneys = int(moneys)
        withdraw.withdraws(moneys, json_path, logger)


def main():
    while True:
        print("Luffy Bank".center(30, '-'))
        print(msg)
        num = input('num(q表示退出)>>>:').strip()
        if not num:
            continue
        if num.isdigit():
            num = int(num)
            if num == 1:  # 账号信息
                print_info()
            elif num == 2:  # 转账
                transfer_account()
            elif num == 3:  # 提现
                withdraws_func()
        elif num == 'q':
            exit()


if __name__ == '__main__':
    log_record()
    main()
