#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/2 23:25


# item系列
class Foo:  # Dict
    def __init__(self, name):
        self.name = name

    def __getitem__(self, item):  # item = 'name'，获取
        # print('getitem...')
        return self.__dict__.get(item)

    def __setitem__(self, key, value):  # 设置
        print('setitem...')
        print(key, value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        # print('delitem...')
        # print(key)
        self.__dict__.pop(key)
        # 或者del self.__dict__[key]


obj = Foo('egon')
print(obj.__dict__)

# 查看属性：
# obj.属性名
# obj['name']  # obj.name
print(obj['namexxx'])

# 设置属性：
obj.sex = 'male'
obj['sex'] = 'male'

print(obj.__dict__)
print(obj.sex)

# 删除属性
del obj.name
del obj['name']
print(obj.__dict__)

# __str__方法
d = dict({'name': 'egon'})
# print(isinstance(d, dict))
print(d)


class People:
    def __init__(self, name, age):
        """在创建完对象之后 会自动调用, 它完成对象的初始化的功能"""
        self.name = name
        self.age = age

    def __str__(self):
        """返回一个对象的描述信息"""
        # print('====>str')
        return '<name:%s,age:%s>' % (self.name, self.age)


obj = People('egon', 18)
print(obj)  # obj.__str__()

# __del__
f = open('settings.py')
f.read()
f.close()  # 回收操作系统的资源
print(f)


class Open:
    def __init__(self, filename):
        print('open file......')
        self.filename = filename

    def __del__(self):
        print('回收操作系统资源：self.close()')


f = Open('settings.py')  # 实例化
# del f  # f.__del__()
print('----main----')  # del f  # f.__del__()
# __del__在对象被删除的时候，会自动先触发f.__del__()，再把对象删除
