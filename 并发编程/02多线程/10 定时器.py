#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/11 13:27

# 定时器
from threading import Timer


def task(name):
    print('hello %s' % name)


t = Timer(2, task, args=('egon',))
t.start()

from threading import Timer
import random


class Code:
    def __init__(self):
        self.make_cache()  # 先拿到验证码

    def make_cache(self, interval=2):
        self.cache = self.make_code()  # 缓存验证码
        print('验证码：%s' % self.cache)
        self.t = Timer(interval, self.make_cache)  # 定时器
        self.t.start()
        self.check()

    def make_code(self, n=4):  # 验证码
        res = ''
        for i in range(n):
            s1 = str(random.randint(0, 9))
            s2 = chr(random.randint(65, 90))
            res += random.choice([s1, s2])
        return res

    def check(self):
        while True:
            code = input('请输入你的验证码>>:\n').strip()
            if code.upper() == self.cache:
                print('验证码输入正确')
                self.t.cancel()
                break


obj = Code()
obj.check()
