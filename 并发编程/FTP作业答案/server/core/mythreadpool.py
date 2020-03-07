#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/2/7 21:33

import os
import queue
from threading import Thread


class MyThreadPool:
    def __init__(self, max_workers=None):
        if not max_workers:
            max_workers = os.cpu_count() * 5
        if max_workers <= 0:
            raise ValueError('max_workers 必须大于0')

        self.queue = queue.Queue(max_workers)
        for count in range(max_workers):
            self.put_thread()

    def put_thread(self):
        self.queue.put(Thread)

    def get_thread(self):
        return self.queue.get()
