#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/2 21:39


# 反射：通过字符串映射到对象的属性
class People:
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)


obj = People('egon', 18)
obj.talk()

print(obj.name)  # obj.__dict__['name']
print(obj.talk)

choice = input('>>:')  # choice = 'name'
print(obj.choice)  # print(obj.'name'

# 判断是否存在
print(hasattr(obj, 'name'))  # obj.name #obj.__dict__['name']
print(hasattr(obj, 'talk'))  # obj.name #obj.__dict__['name']

# 取
print(getattr(obj, 'name', None))
print(getattr(obj, 'talk', None))

# 修改
setattr(obj, 'sex', 'male')  # obj.sex = 'male'
print(obj.sex)

# 删除
delattr(obj, 'age')  # del obj.age
print(obj.__dict__)

print(getattr(People, 'country'))  # People.country


# 反射的应用：
class Service:
    def run(self):
        while True:
            inp = input('>>:').strip()  # cmd = 'get a.txt'
            cmds = inp.split()  # cmds,args=['get','a.txt']
            # print(cmds)
            if hasattr(self, cmds[0]):  # 接受用户输入，触发反射
                func = getattr(self, cmds[0])
                func(cmds)

    def get(self, cmds):
        print('get......', cmds[1])

    def put(self, cmds):
        print('put......', cmds[1])


obj = Service()
obj.run()
