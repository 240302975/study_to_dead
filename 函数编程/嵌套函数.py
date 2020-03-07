#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 22:25

name = "小猿圈"


# 每个函数里的变量是互相独立的，变量的查找顺序也是从当前层依次往上层找。
def change():
    name = "小猿圈，自学编程"

    def change2():
        # global name  如果声明了这句，下面的name改的是最外层的全局变层
        name = "小猿圈，自学编程不要钱"  # 这句注释掉的话，下面name打印的是哪个值？
        print("第3层打印", name)

    change2()  # 调用内层函数
    print("第2层打印", name)


change()
print("最外层打印", name)


# 这段代码
def calc(x, y):
    return x ** y


print(calc(2, 5))
# 换成匿名函数
calc = lambda x, y: x ** y
print(calc(2, 5))

res = map(lambda x: x ** 2, [1, 5, 7, 4, 8])
for i in res:
    print(i)
