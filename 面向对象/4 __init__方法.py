#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/26 23:01

# __init__方法用来为对象定制自己独有得特征


class LuffyStudent:
    school = 'luffycity'

    def __init__(self, name, sex, age):
        self.Name = name
        self.Sex = sex
        self.Age = age

        # stu1.Name = 'alex'
        # stu1.Sex = 'sex'
        # stu1.Age = 'age'

    def learn(self):
        print('is learning')

    def eat(self):
        print('is eating')

    def sleep(self):
        print('is sleeping')


# 后产生对象
stu1 = LuffyStudent('alex', '男', 28)  # LuffyStudent.__init__(stu1,'alex','男','28')

# 加上__init__方法后，实例化的步骤
# 1、先生产一个空对象stu1
# 2、LuffyStudent.__init__(stu1,'alex','男','28')

# 查
print(stu1.__dict__)
print(stu1.Name)
print(stu1.Age)
print(stu1.Sex)

# 改
stu1.Name = 'TOM'
print(stu1.__dict__)
print(stu1.Name)

# 删
del stu1.Name
print(stu1.__dict__)

# 增
stu1.class_name = 'python开发'
print(stu1.__dict__)


stu2 = LuffyStudent('李三炮', '女', 20)  # Luffycity.__init__(stu2,'李三炮', '女', '20')
print(stu2.__dict__)
print(stu2.Name)
print(stu2.Age)
print(stu2.Sex)