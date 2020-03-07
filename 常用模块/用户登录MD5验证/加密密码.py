#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/20 20:02

import json
import hashlib
f = 'account.json'
fp = open(f, 'r+', encoding='utf-8')
j_user = json.load(fp)
md = hashlib.md5()
md.update('abc'.encode('utf-8'))
md_pwd = md.hexdigest()
print(md_pwd)
j_user["password"] = md_pwd
fp.seek(0)
fp.truncate()  # 清空文件内容
json.dump(j_user, fp)  # 写入md5密码信息
fp.close()
