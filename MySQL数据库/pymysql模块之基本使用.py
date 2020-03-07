#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/24 22:26

# pip3 install pymysql
import pymysql

user = input('user>>: ').strip()
pwd = input('password>>: ').strip()

# 建立链接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='admin',
    db='db1',
    charset='utf8'
)

# 拿到游标
cursor = conn.cursor()

# 执行sql语句

sql = 'select * from userinfo where user = "%s" and pwd="%s"' % (user, pwd)
rows = cursor.execute(sql)

cursor.close()  # 关闭游标
conn.close()  # 关闭连接

# 进行判断
if rows:
    print('登录成功')
else:
    print('登录失败')
