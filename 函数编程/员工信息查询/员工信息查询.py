#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 9:43

DB_FILE = 'account.txt'
COLUMN_NAME = ['Username', 'Password', 'Name', 'Age', 'Job', 'Dept', 'Phone']
MENU = '''
1. 打印个人信息
2. 修改个人信息
3. 修改密码
[按q返回登录界面]
'''


# 打印信息
def print_log(msg, log_type="info"):
    if log_type == 'info':
        print("\033[32;1m%s\033[0m" % msg)
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m" % msg)


def load_db():
    """
    载入人员信息
    :return:
    """
    staff_data = {}
    # 构建字典空列表
    # {'Username': ['username','Password','Name','Age','Job','Dept'，'Phone'}
    # for d in COLUMN_NAME:
    #     staff_data[d] = []

    with open(DB_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            datas = line.split(",")
            # 构建员工信息字典
            datas[-1] = datas[-1].strip()  # 去掉回车

            staff_data[datas[0]] = datas

    return staff_data


def print_user_info(p_user):
    """
    打印用户信息
    :param p_user:
    :return:
    """
    person_data = STAFF_INFO[p_user]
    # 使用切片把username,Password过滤掉
    # 相当于深拷贝，如果数据量大，会占用大量内存空间
    # person_data = person_data[COLUMN_NAME.index('Name'):]
    for i in range(0, COLUMN_NAME.index('Name')):
        person_data.pop(0)
    # print(person_data)
    info = '''
    ------------------
    Name:   {}
    Age :   {}
    Job :   {}
    Dept:   {}
    Phone:  {}
    ------------------
    '''.format(*person_data)
    print_log(info)
    exit()


def save_db():
    """
    保存到文件中
    :return:
    """
    f = open(DB_FILE, "r+", encoding='utf-8')
    f.seek(0)
    f.truncate()  # 清空文件
    for v_data in STAFF_INFO.values():
        row_data = ','.join(v_data)
        f.write('%s\n' % row_data)

    f.close()


def change_user_info(p_user):
    """
    修改用户信息
    :param p_user: 用户名
    :return:
    """
    user_info = STAFF_INFO[p_user]
    for ind, val in enumerate(user_info):
        if ind > 1:
            msg = '%s, %s, %s' % (ind, COLUMN_NAME[ind], val)
            print_log(msg)
    while True:
        choice = input("输入要修改的列的序号").strip()
        if choice.isdigit():
            choice = int(choice)
            # if choice > len(user_info) and choice < 2:
            if 2 < choice < len(user_info):
                curr_val = user_info[choice]
                print_log('当前值为' + curr_val)
                new_val = input('input new_value->').strip()
                user_info[choice] = new_val
                STAFF_INFO[p_user] = user_info
                save_db()
                msg = '%s修改成功' % COLUMN_NAME[choice]
                print_log(msg)
                break
            else:
                print_log('输入要的序号不存在', 'error')

        else:
            print_log('输入错误，请输入2-6的数字', 'error')


def change_user_pwd():
    """
    修改密码
    :return:
    """
    while True:
        pwd1 = input("输入新密码->").strip()
        pwd2 = input("再输一次新密码->").strip()
        if pwd1 == pwd2:
            pwd_ind = COLUMN_NAME.index('Password')  # 得到密码索引
            STAFF_INFO[user][pwd_ind] = pwd2
            save_db()
            print_log('密码修改成功,已更改为%s' % pwd2)
            break
        else:
            print_log('密码两次输入不一致', 'error')


def login_auth(username, password):
    """
    用户名密码验证
    :param username:
    :param password:
    :return:
    """
    if username in STAFF_INFO:
        if password == STAFF_INFO[username][1]:
            return True
        else:
            print_log('用户名或密码错误', 'error')
            return False
    else:
        print_log('用户名不存在', 'error')
        return False


if __name__ == '__main__':
    STAFF_INFO = load_db()
    # print(STAFF_INFO)
    count = 0
    while count < 3:
        user = input('用户名:->')
        pwd = input('密码:->')
        if login_auth(user, pwd):
            print('welcome %s'.center(50, '-') % user)
            while True:  # 用户停留这一层
                print(MENU)
                user_choice = input(">>>:").strip()
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice == 1:
                        # 用户登录成功打印用户信息
                        print_user_info(user)
                    elif user_choice == 2:
                        change_user_info(user)
                    elif user_choice == 3:
                        change_user_pwd()
                elif user_choice == 'q':
                    break

        else:
            count += 1
    else:
        print_log("Too many attempts.", 'error')
