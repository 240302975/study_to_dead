# class ParentClass1:
#     pass
#
#
# class ParentClass2:
#     pass
#
#
# class SubClass1(ParentClass1):
#     pass
#
#
# class SubClass2(ParentClass1, ParentClass2):
#     pass
#
#
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)


########################################################
class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = aggresivity

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity


class Garen(Hero):
    pass


class Riven(Hero):
    pass


g1 = Garen('草丛伦', 100, 20)

r1 = Riven('锐雯', 80, 50)

# print(r1.life_value)
# g1.attack(r1)
# print(r1.life_value)

print(g1.nickname)


########################################################
# 属性查找小练习（继承）
class Foo:
    def f1(self):
        print('from Foo.f1')

    def f2(self):
        print('from Foo.f2')
        self.f1()  # b.f1() 一层一层查找，类--父类


class Bar(Foo):
    def f1(self):
        print('from Bar.f3')


b = Bar()
b.f2()
