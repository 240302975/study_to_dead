#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/17 20:07

def run():
    count = 0
    while True:
        n = yield count
        print("-->", n, count)
        count += 1


g = run()
g.__next__()
g.send('alex')
g.send('jack')
g.send('room')
g.send('black')
