#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/12 21:19

# requests：用于爬取HTML页面，提交网络请求
"""
回调函数：add_done_callback
可以为进程池或线程池内的每个进程或线程绑定一个函数，
该函数在进程或线程的任务执行完毕后自动触发，并接收任务的返回值当作参数。
"""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import requests
import json
import os


def get_page(url):  # 获取
    print('<进程%s> get %s' % (os.getpid(), url))
    respone = requests.get(url)
    if respone.status_code == 200:
        return {'url': url, 'text': respone.text}


def parse_page(res):  # 解析
    res = res.result()
    print('<进程%s> parse %s' % (os.getpid(), res['url']))
    parse_res = 'url:<%s> size:[%s]\n' % (res['url'], len(res['text']))
    with open('db.txt', 'a') as f:
        f.write(parse_res)


if __name__ == '__main__':
    urls = [
        'https://www.baidu.com',
        'https://segmentfault.com/',
        'http://www.sina.com.cn/'
    ]

    p = ProcessPoolExecutor(3)
    for url in urls:
        p.submit(get_page, url).add_done_callback(parse_page)  # parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果
