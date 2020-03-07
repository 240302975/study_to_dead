#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2020/1/15 22:25

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HOST = "0.0.0.0"
PORT = 9999

USER_HOME_DIR = os.path.join(BASE_DIR, 'home')

ACCOUNT_FILE = "%S/conf/accounts.ini" % BASE_DIR

MAX_SOCKET_LISTEN = 5
