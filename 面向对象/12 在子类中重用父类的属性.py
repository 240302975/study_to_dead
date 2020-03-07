#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019/12/31 14:06


# 在子类派生出的新的方法中重用父类的方法，有两种实现方式
# 方式一：指名道姓（不依赖继承）
class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    camp = 'Demacia'

    def __init__(self, nickname, life_value, aggresivity, weapon):

        # self.nickname = nickname
        # self.life_value = life_value
        # self.aggresivity = aggresivity

        Hero.__init__(self, nickname, life_value, aggresivity)
        self.weapon = weapon

    def attack(self, enemy):  # 派生，添加新的属性，如果和父类重名，以自己为准
        Hero.attack(self, enemy)  # 指名道姓
        print('from Garen Class')


g1 = Garen('草丛伦', 100, 20, '金箍棒')
print(g1.__dict__)


# 方式二：super()（依赖继承）
class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    camp = 'Demacia'

    def __init__(self, nickname, life_value, aggresivity, weapon):
        super().__init__(nickname, life_value, aggresivity)
        self.weapon = weapon

    print('from Garen Class')


g1 = Garen('草丛伦', 100, 20, '金箍棒')
print(g1.__dict__)


class A:
    def f1(self):
        print('from A')
        super().f1()  # 参照mro


class B:
    def f1(self):
        print('from B')


class C(A, B):
    pass


print(C.mro())
# [<class '__main__.C'>,
# <class '__main__.A'>,
# <class '__main__.B'>,
# <class 'object'>]

c = C()
c.f1()
