#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/24 23:30

import pymysql

# 链接
conn = pymysql.connect(host='localhost', user='root', password='123', database='egon')
# 游标
cursor = conn.cursor()

# 执行sql语句
# 增、删、改
# part1
sql = 'insert into userinfo(name,password) values("root","123456");'
res = cursor.execute(sql)  # 执行sql语句，返回sql影响成功的行数
print(res)

# part2
sql = 'insert into userinfo(name,password) values(%s,%s);'
res = cursor.execute(sql, ("root", "123456"))  # 执行sql语句，返回sql影响成功的行数
print(res)

# part3
sql = 'insert into userinfo(name,password) values(%s,%s);'
res = cursor.executemany(sql, [("root", "123456"), ("lhf", "12356"), ("eee", "156")])  # 执行sql语句，返回sql影响成功的行数
print(res)

conn.commit()  # 提交后才发现表中插入记录成功
cursor.close()
conn.close()

# 2、查询
import pymysql

# 建立链接
conn = pymysql.connect(
    host='192.168.10.15',
    port=3306,
    user='root',
    password='123',
    db='db9',
    charset='utf8'
)

# 拿游标
cursor = conn.cursor(pymysql.cursors.DictCursor)  # 基于字典的游标

# 执行sql
# 查询
rows = cursor.execute('select * from userinfo;')
print(rows)  # 受影响行数
print(cursor.fetchone())  # 每次取一行
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

print(cursor.fetchmany(2))  # 每次取2行

print(cursor.fetchall())  # 全取
print(cursor.fetchall())  # []

cursor.scroll(3, mode='absolute')  # 相对绝对位置移动
print(cursor.fetchone())  # 从头取
cursor.scroll(2, mode='relative')  # 相对当前位置移动
print(cursor.fetchone())  # 当前取

# 关闭
cursor.close()
conn.close()
