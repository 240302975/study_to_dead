#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/29 14:52


class Chinese:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('%s is eating' % self.name)


p1 = Chinese('egon', 18, 'male')
p2 = Chinese('alex', 38, 'female')
p3 = Chinese('wpq', 48, 'female')
# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)
p1.eat()
p2.eat()
p3.eat()


class Chinese:
    country = 'China'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        info = '''
        国籍:%s
        姓名:%s
        年龄:%s
        性别:%s
        ''' % (self.country, self.name, self.age, self.sex)
        print(info)


p1 = Chinese('egon', 18, 'male')
p2 = Chinese('alex', 38, 'female')
p3 = Chinese('wpq', 48, 'female')

# print(p1.country)
p1.tell_info()
