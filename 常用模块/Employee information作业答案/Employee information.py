#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 17:41


def table_info():
    # 读取文件，并转化为列表
    date_file = open('staff_table', 'r', encoding='utf-8')
    lines = date_file.readlines()
    data = []
    for line in lines:
        data.append(line.split(','))
    return data
    # date_file.close()


table_info()


def qurey1():  # 查询方式1，find name,age from staff_table where age > 22
    count = 0
    for line in table_info():
        if line[2] > '22':
            d1[count] = [line[1], line[2]]
            count += 1
    print('name', ' ', 'age')
    for i in d1.keys():
        print(d1[i][0], ',', d1[i][1])
    print('满足本次查询的个数为：', count)


def qurey2(x):  # 查询方式2，find * from staff_table where dept = "IT"
    count = 0
    element = x[1:3]
    for line in table_info():
        if line[4] == element:
            d1[count] = line
            count += 1
    for i in d1.values():
        for m in i:
            print(m, end=' ')
    print('满足本次查询的个数为：', count)


def qurey3(x):  # 查询方式3，find * from staff_table where enroll_date like "2013"
    count = 0
    element = x[1:5]
    for line in table_info():
        if line[-1][:4] == element:
            d1[count] = line
            count += 1
    for i in d1.values():
        for m in i:
            print(m, end=' ')
    print('满足本次查询的个数为：', count)


def delete():  # 删除
    while True:
        count = 0
        print("""支持以下语句删除员工信息：
        del from staff_table where id = 10
        退出请按Q""")
        input1 = input('请输入删除命令的SQL语句：').strip()
        input_del = input1.split(' ')
        if input1 == "Q" or input1 == 'q':
            break
        else:
            del_id = input_del[-1].split('=')[-1]
            with open('staff_table', 'r', encoding='utf-8') as f_read:
                lines = f_read.readlines()
            with open('staff_table', 'w', encoding='utf-8') as f_wirte:
                for line in lines:
                    if del_id == line.split(',')[0]:
                        count += 1
                        continue
                    else:

                        f_wirte.write(line)
            print('本次删除的数目为：', count)


def new():  # 创建
    while True:
        user = True
        print("""支持以下语句新建员工信息：)
        add staff_table Shanshan Du,26,13698424612,Operation,2017-07-02
        退出请按Q""")
        input_a = input('请输入新建命令的SQL语句：').strip()
        input_adds = input_a.split(',')
        # ['add staff_table Shanshan Du', '26', '13698424612', 'Operation', '2017-07-02']
        input_add = input_adds[0].split(' ', 2)
        input_add.extend(input_adds[1:0])  # ['add', 'staff_table', 'Shanshan Du']
        if input_a == 'Q' or input_a == 'q':
            print('返回到第一层！')
            break
        else:
            name = input_add[2]
            age = input_adds[1]
            phone = input_adds[2]
            department = input_adds[3]
            start_time = input_adds[4]
            count = 0
            num = 0
            for line in table_info():
                count += 1
                if int(line[3]) == int(phone):
                    print('\033[1;35m您输入的用户已存在\033[0m')
                    user = False
                    break
            if user:
                newstr = str(count + 1) + ',' + name + ',' + age + ',' + phone + ',' + department + ',' + start_time
                f = open('staff_table', 'a', encoding='utf-8')
                f.writelines('\n')
                f.writelines(newstr)
                f.close()
                num += 1
                print('\033[1;35m用户已添加\033[0m'.center(10, '.'))
                print('本次操作的命令行数为', num)


def modify():  # 修改
    while True:
        print("""支持以下语句修改员工信息，包括部门名称与年龄:
        UPDATE staff_table SET dept="Market" WHERE dept = "IT"
        UPDATE staff_table SET age=25 WHERE name = "Alex Li"
        退出请按Q""")
        print('请输入您要操作的语句：')
        user_mod = input('<<<:').strip()
        if user_mod == "q" or user_mod == "Q":
            print('退出到上一层！')
            break
        user_msg = user_mod.split(' ')[3].split('=')
        # 提取年龄
        if user_msg[0] == 'age':
            aft = user_msg[1]
            name = user_mod.split('"')[-2]
            count = 0
            with open('staff_table', 'r+', encoding='utf-8') as f1:
                lines = f1.readlines()
            with open('staff_table', 'w', encoding='utf-8') as f2:
                for line in lines:
                    if name in line:
                        bef = line.split(',')[2]
                        line = line.replace(bef, aft)
                        # print(1)
                        count += 1
                    f2.write(line)
                print('信息已更新！')
                print('本次更新信息数目为：', count)
        else:
            input_update = user_mod.split('"')
            before = input_update[3]
            after = input_update[1]
            count = 0
            with open('staff_table', 'r+', encoding='utf-8') as f1:
                lines = f1.readlines()
            with open('staff_table', 'w', encoding='utf-8') as f2:
                for line in lines:
                    if before in line:
                        line = line.replace(before, after)
                        count += 1
                    f2.write(line)
                print('信息已更新！')
                print('本次更新信息数目为：', count)


print('欢迎来到员工查询系统'.center(40, '*'))
while True:
    print('''请根据以下提示输入对应指令序号：
        1.查询员工信息
        2.创建员工信息
        3.删除员工信息
        4.修改员工信息''')
    input_num = int(input('>>>:').strip())
    if input_num == 1:
        while True:
            print('退出请按Q')
            print('我们支持以下查询语句'.center(40, '-'))
            print('''
            find name,age from staff_table where age > 22
            find * from staff_table where dept = "IT"
            find * from staff_table where enroll_date like "2013"
            请输入您的查询语句：''')

            input_sent = input('<<<:').strip()
            input_sent1 = input_sent.split(' ')
            d1 = {}
            print("本次查询的结果如下：".center(20, "-"))

            if input_sent == 'find name,age from staff_table where age > %s' % (input_sent1[-1]):
                qurey1()
            elif input_sent == 'find * from staff_table where dept = %s' % (input_sent1[-1]):
                qurey2(input_sent1[-1])
            elif input_sent == 'find * from staff_table where enroll_date like %s' % (input_sent1[-1]):
                qurey3(input_sent1[-1])
            elif input_sent == "Q" or input_sent == 'q':
                break
            else:
                print('您的输入格式有误，请重新输入！')
    elif input_num == 2:
        new()

    elif input_num == 3:
        delete()

    elif input_num == 4:
        modify()
    else:
        print('您输入有误，请重新输入')
