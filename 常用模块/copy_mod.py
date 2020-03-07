#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/19 10:01

import shutil
import os
import zipfile

shutil.copyfileobj(open("Json_mod.py"), open("json2_mod.py", "w"))  # 将文件内容拷贝到另一个文件中

shutil.copyfile("Json_mod.py", "json3_mod.py")  # 拷贝文件

shutil.copymode("time_mod.py", "json3_mod.py")  # 仅拷贝权限。内容、组、用户均不变
shutil.copystat("time_mod.py", "json3_mod.py")  # 仅拷贝状态的信息，包括：mode bits, atime, mtime, flags

shutil.copy("time_mod.py", "time2_mod.py")  # 拷贝文件和权限

shutil.copy2("time_mod.py", "time3_mod.py")  # 拷贝文件和状态信息

shutil.copytree("../day4_常用模块", "day4_代码", ignore=shutil.ignore_patterns("__init__.py", "result.*"))  # 递归的去拷贝文件夹
# 目标目录不能存在，注意对folder2目录父级目录要有可写权限，ignore的意思是排除

shutil.make_archive(base_name="/Users/alex/Downloads/day4_code",
                    format="zip", root_dir="../开发基础/",
                    owner="root")  # 创建压缩包并返回文件路径

# 压缩&解压缩
z = zipfile.ZipFile("test_compress.zip", "w")
z.write("os_mod.py")
z.write("pickle_load.py")

filelist = []
for root_dir, dirs, files in os.walk("备课用/my_proj"):
    for filename in files:
        filelist.append(os.path.join(root_dir, filename))

for i in filelist:
    print(i)
    z.write(i)

z.close()

z = zipfile.ZipFile('test_compress.zip', 'r')
z.extractall(path='/Users/alex/Documents/tt')

z.close()
