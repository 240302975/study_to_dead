#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/21 21:02


import json
import os


def withdraws(moneys, json_path, logger):
    luffy_data = json.load(open(os.path.join(json_path, 'luffy.json'), 'r', encoding='utf-8'))
    if moneys <= luffy_data['credit_account']:
        luffy_data['credit_account'] = luffy_data['credit_account'] - moneys*(1+0.05)
        json.dump(luffy_data, open(os.path.join(json_path, 'luffy.json'), 'w', encoding='utf-8'))
        print('提现成功！')
        logger.warning('提现成功')
    else:
        print('\033[0;31m提现金额大于信用额度了！\033[0m')
        logger.error('提现金额大于信用额度')
